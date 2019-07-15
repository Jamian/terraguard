from terraguard.resources.aws.resource import Resource


class AWSAppCookieStickinessPolicy(Resource):

    resource_type = "aws_app_cookie_stickiness_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSELB(Resource):

    resource_type = "aws_elb"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSELBAttachment(Resource):

    resource_type = "aws_elb_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBCookieStickinessPolicy(Resource):

    resource_type = "aws_lb_cookie_stickiness_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLBSSLNegotationPolicy(Resource):

    resource_type = "aws_lb_ssl_negotiation_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLoadBalancerBackendServerPolicy(Resource):

    resource_type = "aws_load_balancer_backend_server_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLoadBalancerListenerPolicy(Resource):

    resource_type = "aws_load_balancer_listener_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLoadBalancerPolicy(Resource):

    resource_type = "aws_load_balancer_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSProxyProtolPolicy(Resource):

    resource_type = "aws_proxy_protocol_policy"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)
