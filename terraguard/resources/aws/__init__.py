from terraguard.resources.aws import aws_ec2
from terraguard.resources.aws import aws_ecr
from terraguard.resources.aws import aws_elb
from terraguard.resources.aws import aws_lb
from terraguard.resources.aws import aws_sqs
from terraguard.resources.aws import aws_vpc


class AWSResourceManager:

    def __init__(self):
        self.class_map = {}
        self.class_map.update(dict([(cls.resource_type, cls) for name, cls in aws_elb.__dict__.items() if isinstance(cls, type)]))
        self.class_map.update(dict([(cls.resource_type, cls) for name, cls in aws_ec2.__dict__.items() if isinstance(cls, type)]))
        self.class_map.update(dict([(cls.resource_type, cls) for name, cls in aws_ecr.__dict__.items() if isinstance(cls, type)]))
        self.class_map.update(dict([(cls.resource_type, cls) for name, cls in aws_lb.__dict__.items() if isinstance(cls, type)]))
        self.class_map.update(dict([(cls.resource_type, cls) for name, cls in aws_sqs.__dict__.items() if isinstance(cls, type)]))
        self.class_map.update(dict([(cls.resource_type, cls) for name, cls in aws_vpc.__dict__.items() if isinstance(cls, type)]))

    def get_resource(self, resource_type, terraform_resource_config):
        try:
            # Quick fix for the multiple valid address types for load balancing v2.
            if 'aws_alb' in resource_type:
                resource_type = resource_type.replace('aws_alb', 'aws_lb')

            return self.class_map[resource_type](terraform_resource_config)
        except KeyError:
            raise NotImplementedError('Trying to analyze resource [{resource_type}] that is not supported.'.format(
                resource_type=resource_type))
