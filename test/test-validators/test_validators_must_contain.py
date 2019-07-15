from terraguard.validators import must_contain
from terraguard.resources.aws.resource import Resource


def test_must_contain_validator_with_correct_config_returns_empty_violations():
    rule = {
        'expression': 'Tags',
        'must_contain': ['TestTag']
    }

    lookup_key = 'Tags'

    config = {
        'address': 'test_address',
        'values': {
            'Tags': {
                'TestTag': 'NA'
            }
        }
    }
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_contain(rule, lookup_key, resource)
    assert(resource.violations == {})


def test_must_contain_validator_with_bad_config_returns_expected_violations():
    rule = {
        'expression': 'Tags',
        'must_contain': ['TestTag', 'AnotherTag']
    }

    lookup_key = 'Tags'

    config = {
        'address': 'test_address',
        'values': {
            'Tags': {
                'NotTestTag': 'NA',
            }
        }
    }
    resource = Resource(config)

    must_contain(rule, lookup_key, resource)
    assert('test_address.must_contain') in resource.violations
    assert(len(resource.violations['test_address.must_contain']) == len(rule['must_contain']))
    for violation, expected_violation in zip(resource.violations['test_address.must_contain'], rule['must_contain']):
        assert(violation == 'Missing Tags [{expected_violation}] defined in resource'.format(expected_violation=expected_violation))


def test_must_contain_validator_with_bad_config_with_no_key_returns_expected_violations():
    rule = {
        'expression': 'Tags',
        'must_contain': ['TestTag']
    }

    lookup_key = 'Tags'

    config = {
        'address': 'test_address',
        'values': {}
    }
    resource = Resource(config)

    must_contain(rule, lookup_key, resource)
    assert(len(resource.violations['test_address.must_contain']) == len(rule['must_contain']))
    for violation, expected_violation in zip(resource.violations['test_address.must_contain'], rule['must_contain']):
        assert(violation == 'Missing Tags block and [{expected_violation}] required defined in resource'.format(expected_violation=expected_violation))

    # We also have to handle when the tag key exists but is a null value
    config['values']['Tags'] = None
    must_contain(rule, lookup_key, resource)
    assert(len(resource.violations['test_address.must_contain']) == len(rule['must_contain']))
    for violation, expected_violation in zip(resource.violations['test_address.must_contain'], rule['must_contain']):
        assert(violation == 'Null Tags block and [{expected_violation}] required defined in resource'.format(expected_violation=expected_violation))
