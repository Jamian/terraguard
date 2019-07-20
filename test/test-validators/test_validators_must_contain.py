from terraguard.validators import must_contain
from terraguard.resources.aws import AWSResource


def test_must_contain_validator_with_correct_config_returns_empty_violations():
    rule = {
        'tags': {
            'TestTag': 'NA'
        }
    }

    lookup_key = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': {
                'TestTag': 'NA'
            }
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, lookup_key)
    assert(resource.violations == {})


def test_must_contain_validator_with_correct_resource_level_config_returns_empty_violations():
    rule = 'tags'

    lookup_key = 'tags'

    config = {
        'address': 'aws_s3_bucket',
        'values': {
            'tags': {
                'TestTag': 'NA'
            }
        }
    }
    resource = AWSResource('aws_s3_bucket', config)

    must_contain(rule, resource, lookup_key)
    assert(resource.violations == {})
