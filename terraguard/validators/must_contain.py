MUST_CONTAIN = 'must_contain'


def resource_must_contain(rule, resource, full_address):
    if isinstance(rule, str):
        if rule not in resource.config['values']:
            error_message = 'Missing required [{rule}] attribute from {resource_type}'.format(
                rule=rule,
                resource_type=resource.resource_type
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)


def attribute_must_contain(rule, resource, attribute_name, full_address):
    if isinstance(rule, str):
        if rule not in resource.config['values']:
            error_message = 'Missing required [{rule}] attribute from {resource_type}'.format(
                rule=rule,
                resource_type=resource.resource_type
            )
            if full_address not in resource.violations:
                resource.violations[full_address] = []
            if error_message not in resource.violations[full_address]:
                resource.violations[full_address].append(error_message)
    if isinstance(rule, list):
        for item in rule:
            # If the attribute_name doesn't exist as all
            if attribute_name not in resource.config['values']:
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                resource.violations[full_address] = ['Missing {attribute_name} block and [{item}] required defined in {resource_type}'.format(
                    attribute_name=attribute_name.capitalize(),
                    item=item,
                    resource_type=resource.resource_type
                )]
                break
            # If the attribute_name exists, but is set to a null value
            if resource.config['values'][attribute_name] is None:
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                resource.violations[full_address] = ['Null {attribute_name} block and [{item}] required defined in {resource_type}'.format(
                    attribute_name=attribute_name.capitalize(),
                    item=item,
                    resource_type=resource.resource_type
                )]
                break
            # Lookup key exists so let's look at each individual item
            if item not in resource.config['values'][attribute_name]:
                error_message = 'Missing {attribute_name} [{item}] defined in {resource_type}'.format(
                    attribute_name=attribute_name.capitalize(),
                    item=item,
                    resource_type=resource.resource_type
                )
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                if error_message not in resource.violations[full_address]:
                    resource.violations[full_address].append(error_message)


def must_contain(rule, resource, attribute_name=None):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_CONTAIN)

    if not attribute_name:
        resource_must_contain(rule, resource, full_address)
    else:
        attribute_must_contain(rule, resource, attribute_name, full_address)
