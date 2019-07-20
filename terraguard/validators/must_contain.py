MUST_CONTAIN = 'must_contain'


def resource_must_contain(rule, resource, full_address):
    error_message = None
    if isinstance(rule, str):
        if rule not in resource.config['values']:
            error_message = 'Missing required [{rule}] attribute from {resource_type}'.format(
                rule=rule,
                resource_type=resource.resource_type
            )
        elif not resource.config['values'][rule]:
            error_message = 'Missing required [{rule}] attribute from {resource_type}'.format(
                rule=rule,
                resource_type=resource.resource_type
            )

    if error_message:
        resource.add_violation(full_address, error_message)


def attribute_must_contain(rule, resource, attribute_name, full_address):
    error_message = None
    if isinstance(rule, str):
        if rule not in resource.config['values']:
            error_message = 'Missing required [{rule}] attribute from {resource_type}'.format(
                rule=rule,
                resource_type=resource.resource_type
            )
    elif isinstance(rule, list):
        for item in rule:
            # If the attribute_name doesn't exist as all
            if attribute_name not in resource.config['values']:
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                error_message = ['Missing {attribute_name} block and [{item}] required defined in {resource_type}'.format(
                    attribute_name=attribute_name.capitalize(),
                    item=item,
                    resource_type=resource.resource_type
                )]
            # If the attribute_name exists, but is set to a null value
            elif resource.config['values'][attribute_name] is None:
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                error_message = ['Null {attribute_name} block and [{item}] required defined in {resource_type}'.format(
                    attribute_name=attribute_name.capitalize(),
                    item=item,
                    resource_type=resource.resource_type
                )]
            # Lookup key exists so let's look at each individual item
            elif item not in resource.config['values'][attribute_name]:
                error_message = 'Missing {attribute_name} [{item}] defined in {resource_type}'.format(
                    attribute_name=attribute_name.capitalize(),
                    item=item,
                    resource_type=resource.resource_type
                )
    if error_message:
        resource.add_violation(full_address, error_message)


def must_contain(rule, resource, attribute_name=None):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_CONTAIN)

    if not attribute_name:
        resource_must_contain(rule, resource, full_address)
    else:
        attribute_must_contain(rule, resource, attribute_name, full_address)
