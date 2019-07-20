from terraguard.validators import must_equal
from terraguard.resources.aws import AWSResource


def test_must_equal_validator_with_correct_config_returns_empty_violations():
    rule = {
        'TestTag': 'Bloop'
    }

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'TestTag': 'Bloop'
            }
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_equal(rule, resource, lookup_key)
    assert(resource.violations == {})


def test_must_equal_validator_with_bad_tag_value_returns_empty_violations():
    rule = {
        'TestTag': 'Bleep'
    }

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'TestTag': 'Bloop'
            }
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_equal(rule, resource, lookup_key)
    assert(resource.violations == {'test_address.must_equal': ["Tags [TestTag] must equal 'Bleep' but found 'Bloop'"]})


def test_must_equal_validator_with_dict():
    rule = {
        'TestTag': 'Bleep'
    }

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'TestTag': 'Bloop'
            }
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_equal(rule, resource, lookup_key)
    assert(resource.violations == {'test_address.must_equal': ["Tags [TestTag] must equal 'Bleep' but found 'Bloop'"]})


def test_must_equal_validator_with_str():
    rule = 'testvalue'

    lookup_key = 'test'

    config = {
        'address': 'test_address',
        'values': {
            'test': 'foo'
        }
    }
    resource = AWSResource('TestTag', config)
    resource.resource_type = 'testresource'

    must_equal(rule, resource, lookup_key)
    assert(resource.violations == {'test_address.must_equal': ["Incorrect value [test] must equal 'testvalue' but found 'foo'"]})
