from terraguard.resources.aws.resource import Resource


class AWSLB(Resource):

    resource_type = "aws_lb"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBListener(Resource):

    resource_type = "aws_lb_listener"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBListenerCertificate(Resource):

    resource_type = "aws_lb_listener_certificate"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBListenerRule(Resource):

    resource_type = "aws_lb_listener_rule"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBTargetGroup(Resource):

    resource_type = "aws_lb_target_group"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBTargetGroupAttachment(Resource):

    resource_type = "aws_lb_target_group_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)
