import click
import crayons
import json
import os
import subprocess   # nosec: this is controlled enough to ignore warnings and we need it to call Terraform
import yaml

from terraguard.resources.aws import AWSResource

DEFAULT_PLAN_FILE_NAME = 'terraguard-plan.json'


def print_results(resources):
    total_violations = 0
    print('')
    print(crayons.yellow('The following violations have been found:'))
    for resource in resources:
        for address, violation in resource.violations.items():
            print(crayons.cyan('    {address}:'.format(address=address)))
            for violation in violation:
                print(crayons.red('        {violation}'.format(violation=violation)))
                total_violations += 1
            print('')
    print('')
    print('----------------------------------------------------------------')
    print(crayons.yellow('Finished Analyzing.'))
    print('')
    print(crayons.yellow('Total resources - {}'.format(len(resources))))
    print(crayons.yellow('Total ruleset violations - {}'.format(total_violations)))
    print('----------------------------------------------------------------')


def load_plan(plan_file):
    """Open and load the plan using JSON so that we can work with it"""
    current_dir = os.getcwd()
    plan_file = os.path.join(current_dir, plan_file)
    return json.load(open(plan_file))


def generate_plan():
    print(crayons.yellow("No plan file defined. Generating one now..."))
    with open(os.devnull, 'w') as devnull:
        subprocess.call(["terraform", "plan", "-out", "terraguard-plan"], stdout=devnull, stderr=subprocess.STDOUT)  # nosec: this is controlled enough to ignore warnings
    output = subprocess.check_output(["terraform", "show", "-json", "terraguard-plan"])   # nosec: this is controlled enough to ignore warnings
    with open('terraguard-plan.json', 'wb') as file:
        file.write(output)


def load_configs(config_path=None):
    if config_path:
        try:
            master_config = yaml.safe_load(open(config_path))
        except FileNotFoundError:
            print(crayons.red('Master config not found at the given path. Please check your --config argument.'))
            raise
    else:
        master_config = {'rulesets': {}}

    try:
        config = yaml.safe_load(open(os.path.join(os.getcwd(), 'terraguard.yaml')))
    except FileNotFoundError:
        if master_config:
            print(crayons.red('No project level terraguard.yaml configuration file found. Continuing with master.'))
            config = {'rulesets': {}}
        else:
            print(crayons.red('No project level terraguard.yaml configuration file found and no master defined. Exiting.'))
            raise

    # This is pretty rudimentary and allows sub projects to override any key but it is all of nothing.
    # TODO: Maybe it would be nice to be able to add, not just override?
    master_config['rulesets'].update(config['rulesets'])
    return master_config


@click.command()
@click.option('--json-plan-file', required=False, help='Name of the JSON plan file to check')
@click.option('--out', required=False, help='Output the results to a file')
@click.option('--master-config', required=False, help='Path to the terraguard config file')
def validate(json_plan_file, out, master_config):
    """Check the plan for any defined rulesets and policies"""

    config = load_configs(master_config)

    if not json_plan_file:
        generate_plan()
        json_plan_file = DEFAULT_PLAN_FILE_NAME

    plan = load_plan(json_plan_file)
    planned_values_resources = plan['planned_values']['root_module']['resources']
    total_resources = 0

    print('----------------------------------------------------------------')
    print(crayons.yellow('Terraguard will now check for ruleset violations...'))
    print('')

    resources = []

    for resource_config in planned_values_resources:
        address = resource_config['address']
        print(crayons.green('Analyzing {address}'.format(address=address)))
        resource_type = resource_config["address"].split('.')[0]

        resource_obj = AWSResource(resource_type, resource_config)
        resource_obj.validate(config["rulesets"])
        resources.append(resource_obj)

        total_resources += 1

    print_results(resources)


def main():
    validate()
