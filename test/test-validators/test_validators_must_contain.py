from terraguard.validators import must_contain
from terraguard.resources.aws import AWSResource


def test_must_contain_validator_with_correct_config_returns_empty_violations():
    rule = {
        'tags': {
            'TestTag': 'NA'
        }
    }

    attribute_name = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': {
                'TestTag': 'NA'
            }
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, attribute_name)
    assert(resource.violations == {})


def test_must_contain_validator_with_missing_attributes_rule_adds_correct_violation():
    rule = 'tags'

    attribute_name = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {}
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, attribute_name)
    assert(resource.violations == {'aws_s3_bucket.must_contain': ['Missing required [tags] attribute from aws_s3_bucket']})


def test_must_contain_validator_with_attribute_rule_as_null_adds_correct_violation():
    rule = ['tags']

    attribute_name = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': None
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, attribute_name)
    assert(resource.violations == {'aws_s3_bucket.must_contain': ['Null Tags block and [tags] required defined in aws_s3_bucket']})

    config = {
        'address': 'aws_s3_bucket',
        'values': {}
    }
    resource = AWSResource('aws_s3_bucket', config)
    must_contain(rule, resource, attribute_name)
    assert(resource.violations == {'aws_s3_bucket.must_contain': ['Missing Tags block and [tags] required defined in aws_s3_bucket']})


def test_must_contain_validator_with_list_of_rules_adds_all_expected_violations():
    rule = ['foo', 'bar', 'foobar']

    attribute_name = 'tags'

    # Test against a dictionary of values.
    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': {
                'foobar': 3
            }
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, attribute_name)
    expected_violations = ['Missing Tags [foo] defined in aws_s3_bucket', 'Missing Tags [bar] defined in aws_s3_bucket']
    key = 'aws_s3_bucket.must_contain'
    assert key in resource.violations
    for violation in expected_violations:
        assert(violation in resource.violations[key])


def test_must_contain_validator_with_correct_resource_level_config_returns_empty_violations():
    rule = 'tags'

    attribute_name = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': {
                'TestTag': 'NA'
            }
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, attribute_name)
    assert(resource.violations == {})


def test_must_contain_validator_null_value():
    rule = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': None
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource)
    assert(resource.violations == {'aws_s3_bucket.must_contain': ['Missing required [tags] attribute from aws_s3_bucket']})
