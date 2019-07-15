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
    assert(resource.violations == {'test_address.must_not_contain': ['Found Tags [TestTag] defined in testresource']})



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
