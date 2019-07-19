MUST_NOT_CONTAIN = 'must_not_contain'


def must_not_contain(rule, resource, lookup_key=None):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_NOT_CONTAIN)
    if isinstance(rule, list):
        for item in rule:
            if lookup_key not in resource.config['values']:
                continue
            if not resource.config['values'][lookup_key]:
                continue
            if item in resource.config['values'][lookup_key]:
                error_message = 'Found {lookup_key} [{item}] defined in {resource_type}'.format(
                    lookup_key=lookup_key,
                    item=item,
                    resource_type=resource.resource_type
                )
                if full_address not in resource.violations:
                    resource.violations[full_address] = []
                if error_message not in resource.violations[full_address]:
                    resource.violations[full_address].append(error_message)
    elif isinstance(rule, str):
        if isinstance(resource.config['values'][lookup_key], list):
            for tf_value in resource.config['values'][lookup_key]:
                if rule == tf_value:
                    error_message = 'Found {lookup_key} [{rule}] defined in {resource_type}'.format(
                        lookup_key=lookup_key,
                        rule=rule,
                        resource_type=resource.resource_type
                    )
                    if full_address not in resource.violations:
                        resource.violations[full_address] = []
                    if error_message not in resource.violations[full_address]:
                        resource.violations[full_address].append(error_message)
