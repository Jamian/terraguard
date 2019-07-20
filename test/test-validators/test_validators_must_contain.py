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
