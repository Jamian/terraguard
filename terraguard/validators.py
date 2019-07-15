"""Common and resource agnostic validators."""


def must_not_contain(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = f'{address}.must_not_contain'
    for item in rule['must_not_contain']:
        if lookup_key not in resource.config['values']:
            continue
        if not resource.config['values'][lookup_key]:
            continue
        if item in resource.config['values'][lookup_key]:
            rule_expression = rule['expression']
            error_message = f'Found {lookup_key} [{item}] defined in {resource.resource_type}'
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[f'{address}.must_not_contain']:
                resource.violations[full_address].append(error_message)


def must_equal(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = f'{address}.must_equal'
    for item, options in rule['must_equal'].items():
        if lookup_key not in resource.config['values']:
            continue
        if not resource.config['values'][lookup_key]:
            continue
        # Lookup key exists so let's look at each individual item
        if item in resource.config['values'][lookup_key]:
            tf_value = resource.config['values'][lookup_key][item]
            if tf_value not in options:
                rule_expression = rule['expression']
                if isinstance(options, list):
                    error_message = f'{lookup_key.capitalize()} [{item}] must match one of {options} but found \'{tf_value}\''
                else:
                    error_message = f'{lookup_key.capitalize()} [{item}] must equal \'{options}\' but found \'{tf_value}\''
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                if error_message not in resource.violations[full_address]:
                    resource.violations[full_address].append(error_message)


def must_contain(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = f'{address}.must_contain'
    for item in rule['must_contain']:
        # If the lookup key doesn't exist as all
        if lookup_key not in resource.config['values']:
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            resource.violations[full_address] = [f'Missing {lookup_key} block and [{item}] required defined in {resource.resource_type}']
            break
        # If the lookup key exists, but is set to a null value
        if resource.config['values'][lookup_key] is None:
            if f'{address}.must_contain' not in resource.violations:
                resource.violations[full_address] = []
            resource.violations[full_address] = [f'Null {lookup_key} block and [{item}] required defined in {resource.resource_type}']
            break
        # Lookup key exists so let's look at each individual item
        if item not in resource.config['values'][lookup_key]:
            rule_expression = rule['expression']
            error_message = f'Missing {lookup_key} [{item}] defined in {resource.resource_type}'
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)
