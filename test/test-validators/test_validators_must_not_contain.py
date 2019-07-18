from terraguard.validators import must_not_contain
from terraguard.resources.aws.resource import Resource


def test_must_not_contain_validator_with_correct_config_returns_empty_violations():
    rule = ['TestTag']

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'AnotherTag': 'Boop'
            }
        }
    }
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, lookup_key, resource)
    assert(resource.violations == {})


def test_must_not_contain_validator_with_bad_config_returns_expected_violations():
    rule = ['TestTag']

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'AnotherTag': 'Boop',
                'TestTag': 'Boop'
            }
        }
    }

    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, lookup_key, resource)
    assert('test_address.must_not_contain') in resource.violations
    assert(len(resource.violations['test_address.must_not_contain']) == len(rule))
    for violation, expected_violation in zip(resource.violations['test_address.must_not_contain'], rule):
        assert(violation == 'Found tags [{expected_violation}] defined in testresource'.format(expected_violation=expected_violation))

