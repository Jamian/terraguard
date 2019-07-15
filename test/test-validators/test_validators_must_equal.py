from terraguard.validators import must_equal
from terraguard.resources.aws.resource import Resource


def test_must_equal_validator_with_correct_config_returns_empty_violations():
    rule = {
        'expression': 'tags',
        'must_equal': {
            'TestTag': 'Bloop'
        }
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
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_equal(rule, lookup_key, resource)
    assert(resource.violations == {})


def test_must_equal_validator_with_bad_tag_value_returns_empty_violations():
    rule = {
        'expression': 'tags',
        'must_equal': {
            'TestTag': 'Bleep'
        }
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
    resource = Resource(config)
    resource.resource_type = 'testresource'

    must_equal(rule, lookup_key, resource)
    assert(resource.violations == {'test_address.must_equal': ["Tags [TestTag] must equal 'Bleep' but found 'Bloop'"]})
