import pytest

from terraguard.resources.aws.aws_ec2 import AWSInstance
from terraguard.resources.aws.aws_lb import AWSLB
from terraguard.resources.aws.aws_sqs import AWSSQSQueue

from terraguard.resources.aws import AWSResourceManager


def test_correct_resource_created_based_on_terraform_address():
    aws_manager = AWSResourceManager()

    classes_to_test = {
        'aws_instance': AWSInstance,
        'aws_sqs_queue': AWSSQSQueue,
        'aws_lb': AWSLB,
        'aws_alb': AWSLB
    }

    terraform_config = {
        'address': 'someaddress',
        'values': {'tags': {'test': 'bleepbloop'}}
    }
    for terraform_address, expected_class in classes_to_test.items():
        resource = aws_manager.get_resource(terraform_address, terraform_config)
        assert isinstance(resource, expected_class)


def test_unknown_resource_raises_not_implemented_error():
    aws_manager = AWSResourceManager()
    terraform_config = {
        'address': 'someaddress',
        'values': {'tags': {'test': 'bleepbloop'}}
    }

    with pytest.raises(NotImplementedError):
        aws_manager.get_resource('unknown_thing', terraform_config)
