from terraguard.validators import must_not_contain
from terraguard.resources.aws.resource import Resource


def test_must_not_contain_validator_with_correct_config_returns_empty_violations():
    rule = {
        'expression': 'Tags',
        'must_not_contain': ['TestTag']
    }

    lookup_key = 'Tags'

    config = {
        'address': 'test_address',
        'values': {
            'Tags': {
                'AnotherTag': 'Boop'
            }
        }
    }
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, lookup_key, resource)
    assert(resource.violations == {})


def test_must_not_contain_validator_with_bad_config_returns_expected_violations():
    rule = {
        'expression': 'Tags',
        'must_not_contain': ['TestTag']
    }

    lookup_key = 'Tags'

    config = {
        'address': 'test_address',
        'values': {
            'Tags': {
                'AnotherTag': 'Boop',
                'TestTag': 'Boop'
            }
        }
    }
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, lookup_key, resource)
    assert('test_address.must_not_contain') in resource.violations
    assert(len(resource.violations['test_address.must_not_contain']) == len(rule['must_not_contain']))
    for violation, expected_violation in zip(resource.violations['test_address.must_not_contain'], rule['must_not_contain']):
        assert(violation == 'Found Tags [{expected_violation}] defined in testresource'.format(expected_violation=expected_violation))


def test_must_not_contain_validator_with_bad_config_with_no_key_returns_expected_violations():
    rule = {
        'expression': 'Tags',
        'must_not_contain': ['TestTag']
    }

    lookup_key = 'Tags'

    config = {
        'address': 'test_address',
        'values': {
        }
    }
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, lookup_key, resource)
    assert(resource.violations == {})
