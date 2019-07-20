MUST_EQUAL = 'must_equal'


def resource_must_equal(rule, resource, full_address):
    for item, options in rule.items():
        # Lookup key exists so let's look at each individual item
        if item in resource.config['values']:
            tf_value = resource.config['values'][item]
            if tf_value == options:
                continue
            if tf_value not in options:
                if isinstance(options, list):
                    error_message = '[{item}] must match {options} but found \'{tf_value}\''.format(
                        item=item,
                        options=options,
                        tf_value=tf_value
                    )
                else:
                    error_message = '[{item}] must equal \'{options}\' but found \'{tf_value}\''.format(
                        item=item,
                        options=options,
                        tf_value=tf_value
                    )
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                if error_message not in resource.violations[full_address]:
                    resource.violations[full_address].append(error_message)


def attribute_must_equal(rule, resource, attribute_name, full_address):
    if isinstance(rule, dict):
        for item, options in rule.items():
            if not attribute_name:
                attribute_name = item
            if attribute_name not in resource.config['values']:
                continue
            if not resource.config['values'][attribute_name]:
                continue
            # Lookup key exists so let's look at each individual item
            if item in resource.config['values'][attribute_name]:
                tf_value = resource.config['values'][attribute_name][item]
                if tf_value not in options:
                    if isinstance(options, list):
                        error_message = '{attribute_name} [{item}] must match one of {options} but found \'{tf_value}\''.format(
                            attribute_name=attribute_name.capitalize(),
                            item=item,
                            options=options,
                            tf_value=tf_value
                        )
                    else:
                        error_message = '{attribute_name} [{item}] must equal \'{options}\' but found \'{tf_value}\''.format(
                            attribute_name=attribute_name.capitalize(),
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
        tf_value = resource.config['values'][attribute_name]
        if tf_value is not expected_value:
            error_message = 'Incorrect value [{attribute_name}] must equal \'{expected_value}\' but found \'{tf_value}\''.format(
                attribute_name=attribute_name,
                expected_value=expected_value,
                tf_value=tf_value
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)


def must_equal(rule, resource, attribute_name=None):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_EQUAL)

    if not attribute_name:
        resource_must_equal(rule, resource, full_address)
    else:
        attribute_must_equal(rule, resource, attribute_name, full_address)
