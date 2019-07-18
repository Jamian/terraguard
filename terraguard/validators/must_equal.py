MUST_EQUAL = 'must_equal'


def must_equal(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_EQUAL)
    if isinstance(rule, dict):
        for item, options in rule.items():
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
        expected_value = rule
        tf_value = resource.config['values'][lookup_key]
        if tf_value is not expected_value:
            error_message = 'Incorrect value [{lookup_key}] must equal \'{expected_value}\' but found \'{tf_value}\''.format(
                lookup_key=lookup_key,
                expected_value=expected_value,
                tf_value=tf_value
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)
