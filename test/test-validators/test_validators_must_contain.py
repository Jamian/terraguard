from terraguard.validators import must_contain
from terraguard.resources.aws.resource import Resource


def test_must_contain_validator_with_correct_config_returns_empty_violations():
    rule = {
        'expression': 'tags',
        'must_contain': ['TestTag']
    }

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
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
        'expression': 'tags',
        'must_contain': ['TestTag']
    }

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {
            'tags': {
                'NotTestTag': 'NA'
            }
        }
    }
    resource = Resource(config)

    must_contain(rule, lookup_key, resource)
    assert(resource.violations == {'test_address.must_contain': ['Missing tags [TestTag] defined in resource']})


def test_must_contain_validator_with_bad_config_with_no_key_returns_expected_violations():
    rule = {
        'expression': 'tags',
        'must_contain': ['TestTag']
    }

    lookup_key = 'tags'

    config = {
        'address': 'test_address',
        'values': {}
    }
    resource = Resource(config)

    must_contain(rule, lookup_key, resource)
    assert(resource.violations == {'test_address.must_contain': ['Missing tags block and [TestTag] required defined in resource']})

    # We also have to handle when the tag key exists but is a null value
    config['values']['tags'] = None
    must_contain(rule, lookup_key, resource)
    assert(resource.violations == {'test_address.must_contain': ['Null tags block and [TestTag] required defined in resource']})
