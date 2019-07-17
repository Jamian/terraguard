from terraguard.resources.aws.resource import Resource


class AWSIAMAccessKey(Resource):

    resource_type = "aws_iam_access_key"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMAccountAlias(Resource):

    resource_type = "aws_iam_account_alias"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMAccountPasswordPolicy(Resource):

    resource_type = "aws_iam_account_password_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMGroup(Resource):

    resource_type = "aws_iam_group"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMGroupMembership(Resource):

    resource_type = "aws_iam_group_membership"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMGroupPolicy(Resource):

    resource_type = "aws_iam_group_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMGroupPolicyAttachment(Resource):

    resource_type = "aws_iam_group_policy_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMInstanceProfile(Resource):

    resource_type = "aws_iam_instance_profile"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMOpenIDConnectProvider(Resource):

    resource_type = "aws_iam_openid_connect_provider"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMPolicy(Resource):

    resource_type = "aws_iam_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMPolicyAttachment(Resource):

    resource_type = "aws_iam_policy_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMRole(Resource):

    resource_type = "aws_iam_role"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMRolePolicy(Resource):

    resource_type = "aws_iam_role_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMRolePolicyAttachment(Resource):

    resource_type = "aws_iam_role_policy_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMSAMLProvider(Resource):

    resource_type = "aws_iam_saml_provider"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMServerCertificate(Resource):

    resource_type = "aws_iam_server_certificate"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMServiceLinkedRole(Resource):

    resource_type = "aws_iam_service_linked_role"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMUser(Resource):

    resource_type = "aws_iam_user"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMUserGroupMembership(Resource):

    resource_type = "aws_iam_user_group_membership"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMUserLoginProfile(Resource):

    resource_type = "aws_iam_user_login_profile"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMUserPolicy(Resource):

    resource_type = "aws_iam_user_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMUserPolicyAttachment(Resource):

    resource_type = "aws_iam_user_policy_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSIAMUserSSHKey(Resource):

    resource_type = "aws_iam_user_ssh_key"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)
