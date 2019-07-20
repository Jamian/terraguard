from terraguard.resources.aws import AWSResource


def test_validation_at_resource_level():
    """Testing validation at a resource level, e.g. not under attributes key."""
    ruleset = {
        'aws_subnet': {
            'must_contain': 'tags'
        }
    }

    config = {
        'address': 'aws_subnet',
        'values': {}
    }
    resource = AWSResource('aws_subnet', config)
    resource.validate(ruleset)
    print(resource.violations)
