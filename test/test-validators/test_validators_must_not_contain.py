from terraguard.validators import must_not_contain
from terraguard.resources.aws import AWSResource


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
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, resource, lookup_key)
    assert(resource.violations == {})


def test_must_not_contain_validator_resource_level_does_nothing():
    rule = 'TestTag'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'AnotherTag': 'Boop'
            }
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, resource)
    assert(resource.violations == {})


def test_must_not_contain_validator_for_string_in_stringcorrectly_adds_violations():
    rule = 'foo'

    config = {
        'address': 'test_address',
        'values': {
            'description': 'foo bar'
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, resource, 'description')
    assert(len(resource.violations) == 1)
    assert(resource.violations == {'test_address.must_not_contain': ['[description] contains foo in defined in testresource']})


def test_must_not_contain_validator_for_string_in_list_correctly_adds_violations():
    rule = '0.0.0.0/0'

    config = {
        'address': 'test_address',
        'values': {
            'cidr_blocks': ['10.0.0.0/8', '0.0.0.0/0']
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, resource, 'cidr_blocks')
    assert(len(resource.violations) == 1)
    assert(resource.violations == {'test_address.must_not_contain': ['Found cidr_blocks [0.0.0.0/0] defined in testresource']})


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

    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_not_contain(rule, resource, lookup_key)
    assert('test_address.must_not_contain') in resource.violations
    assert(len(resource.violations['test_address.must_not_contain']) == len(rule))
    for violation, expected_violation in zip(resource.violations['test_address.must_not_contain'], rule):
        assert(violation == 'Found tags [{expected_violation}] defined in testresource'.format(expected_violation=expected_violation))
