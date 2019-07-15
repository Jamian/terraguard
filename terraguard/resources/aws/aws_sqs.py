from terraguard.resources.aws.resource import Resource


class AWSSQSQueue(Resource):

    resource_type = 'aws_sqs_queue'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSQSQueuePolicy(Resource):

    resource_type = 'aws_sqs_queue_policy'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)
