from terraguard.resources.aws.resource import Resource


class AWSECRLifecyclePolicy(Resource):

    resource_type = "aws_ecr_lifecycle_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSECRRepository(Resource):

    resource_type = "aws_ecr_repository"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSECRRepositoryPolicy(Resource):

    resource_type = "aws_ecr_repository_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)
