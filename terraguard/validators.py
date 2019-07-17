"""Common and resource agnostic validators."""
MUST_EQUAL = 'must_equal'
MUST_CONTAIN = 'must_contain'
MUST_NOT_CONTAIN = 'must_not_contain'


def must_not_contain(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_NOT_CONTAIN)
    for item in rule[MUST_NOT_CONTAIN]:
        if lookup_key not in resource.config['values']:
            continue
        if not resource.config['values'][lookup_key]:
            continue
        if item in resource.config['values'][lookup_key]:
            error_message = 'Found {lookup_key} [{item}] defined in {resource_type}'.format(
                lookup_key=lookup_key.capitalize(),
                item=item,
                resource_type=resource.resource_type
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)


def must_equal(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_EQUAL)
    if isinstance(rule[MUST_EQUAL], dict):
        for item, options in rule[MUST_EQUAL].items():
            if lookup_key not in resource.config['values']:
                continue
            if not resource.config['values'][lookup_key]:
                continue
            # Lookup key exists so let's look at each individual item
            if item in resource.config['values'][lookup_key]:
                tf_value = resource.config['values'][lookup_key][item]
                if tf_value not in options:
                    if isinstance(options, list):
                        error_message = '{lookup_key} [{item}] must match one of {options} but found \'{tf_value}\''.format(
                            lookup_key=lookup_key.capitalize(),
                            item=item,
                            options=options,
                            tf_value=tf_value
                        )
                    else:
                        error_message = '{lookup_key} [{item}] must equal \'{options}\' but found \'{tf_value}\''.format(
                            lookup_key=lookup_key.capitalize(),
                            item=item,
                            options=options,
                            tf_value=tf_value
                        )
                    if full_address not in resource.violations:
                        resource.violations[full_address] = []
                    if error_message not in resource.violations[full_address]:
                        resource.violations[full_address].append(error_message)
    else:
        expected_value = rule[MUST_EQUAL]
        tf_value = resource.config['values'][lookup_key]
        if tf_value is not expected_value:
            error_message = '(Incorrect value [{lookup_key}] must equal \'{expected_value}\' but found \'{tf_value}\''.format(
                lookup_key=lookup_key.capitalize(),
                expected_value=expected_value,
                tf_value=tf_value
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)


def must_contain(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_CONTAIN)
    for item in rule[MUST_CONTAIN]:
        # If the lookup key doesn't exist as all
        if lookup_key not in resource.config['values']:
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            resource.violations[full_address] = ['Missing {lookup_key} block and [{item}] required defined in {resource_type}'.format(
                lookup_key=lookup_key.capitalize(),
                item=item,
                resource_type=resource.resource_type
            )]
            break
        # If the lookup key exists, but is set to a null value
        if resource.config['values'][lookup_key] is None:
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            resource.violations[full_address] = ['Null {lookup_key} block and [{item}] required defined in {resource_type}'.format(
                lookup_key=lookup_key.capitalize(),
                item=item,
                resource_type=resource.resource_type
            )]
            break
        # Lookup key exists so let's look at each individual item
        if item not in resource.config['values'][lookup_key]:
            error_message = 'Missing {lookup_key} [{item}] defined in {resource_type}'.format(
                lookup_key=lookup_key.capitalize(),
                item=item,
                resource_type=resource.resource_type
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)
