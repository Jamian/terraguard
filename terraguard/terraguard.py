import click
import crayons
import json
import os
import subprocess   # nosec: this is controlled enough to ignore warnings and we need it to call Terraform
import yaml

from terraguard.resources.aws import AWSResourceManager


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
    print('----------------------------------------------------------------')
    print(crayons.yellow('Finished Analyzing.'))
    print('')
    print(crayons.yellow('Total ruleset violations - ') + crayons.red(total_violations) + crayons.yellow(' accross ') + crayons.cyan(len(resources)) + crayons.yellow(' resources.'))
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


@click.command()
@click.option('--plan-file', required=False, help='Name of the plan file to check')
@click.option('--out', required=False, help='Output the results to a file')
def validate(plan_file, out):
    """Check the plan for any defined rulesets and policies"""
    violations = []

    try:
        config = yaml.safe_load(open(os.path.join(os.getcwd(), 'terraguard.yaml')))
    except FileNotFoundError as exception:
        print(crayons.red("No terraguard.yaml configuration file found. Please create one. "))
        raise

    if not plan_file:
        generate_plan()
        plan_file = DEFAULT_PLAN_FILE_NAME

    plan = load_plan(plan_file)
    planned_values_resources = plan['planned_values']['root_module']['resources']
    total_resources = 0

    print('----------------------------------------------------------------')
    print(crayons.yellow('Terraguard will now check for ruleset violations...'))
    print('')

    resources = []

    aws_resource_manager = AWSResourceManager()

    for resource in planned_values_resources:
        address = resource['address']
        print(crayons.green('Analyzing {address}'.format(address=address)))
        resource_type = resource["address"].split('.')[0]

        resource_obj = aws_resource_manager.get_resource(resource_type, resource)
        resource_obj.validate(config["rulesets"])
        resources.append(resource_obj)

        total_resources += 1

    print_results(resources)


def main():
    validate()
