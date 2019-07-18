MUST_CONTAIN = 'must_contain'


def must_contain(rule, lookup_key, resource):
    address = resource.config['address']
    full_address = '{address}.{validator}'.format(
        address=address,
        validator=MUST_CONTAIN)
    if isinstance(rule, list):
        for item in rule:
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
