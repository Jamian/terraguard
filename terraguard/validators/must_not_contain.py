import crayons

MUST_NOT_CONTAIN = 'must_not_contain'


def must_not_contain(rule, resource, attribute_name=None):
    error_message = None
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_NOT_CONTAIN)

    if not attribute_name:
        print(crayons.yellow('Trying to assert must_not_contain at a resource root level will not work.'))
        print(crayons.yellow('    All planned resources have all values.'))
        print(crayons.yellow('    Try using must_equal a null value instead.'))
        return

    if isinstance(rule, list):
        for item in rule:
            if attribute_name not in resource.config['values']:
                continue
            if not resource.config['values'][attribute_name]:
                continue
            if item in resource.config['values'][attribute_name]:
                error_message = 'Found {attribute_name} [{item}] defined in {resource_type}'.format(
                    attribute_name=attribute_name,
                    item=item,
                    resource_type=resource.resource_type
                )
    elif isinstance(rule, str):
        if isinstance(resource.config['values'][attribute_name], list):
            for tf_value in resource.config['values'][attribute_name]:
                if rule == tf_value:
                    error_message = 'Found {attribute_name} [{rule}] defined in {resource_type}'.format(
                        attribute_name=attribute_name,
                        rule=rule,
                        resource_type=resource.resource_type
                    )
        if isinstance(resource.config['values'][attribute_name], str):
            if rule in resource.config['values'][attribute_name]:
                error_message = '[{attribute_name}] contains {rule} in defined in {resource_type}'.format(
                    attribute_name=attribute_name,
                    rule=rule,
                    resource_type=resource.resource_type
                )
    if error_message:
        resource.add_violation(full_address, error_message)
