from terraguard.resources.aws.resource import Resource
from terraguard.validators import must_not_contain


class AWSNetworkInterface(Resource):

    resource_type = 'aws_network_interface'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSecurityGroup(Resource):

    resource_type = 'aws_security_group'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSecurityGroupRule(Resource):

    resource_type = 'aws_security_group_rule'

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        # Custom validation content
        if self.resource_type in rulesets:
            ruleset = rulesets[self.resource_type]
            for i, _ in enumerate(ruleset):
                rule = ruleset[i]
                if rule['expression'] == 'cidr_blocks':
                    if 'must_not_contain' in rule:
                        must_not_contain(rule, 'cidr_blocks', self)

        super().validate(rulesets)
