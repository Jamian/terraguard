from terraguard.resources.aws.resource import Resource
from terraguard.validators import must_not_contain


class AWSCustomerGateway(Resource):

    resource_type = 'aws_customer_gateway'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSDefaultNetworkACL(Resource):

    resource_type = 'aws_default_network_acl'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSDefaultRouteTable(Resource):

    resource_type = 'aws_default_route_table'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSDefaultSubnet(Resource):

    resource_type = 'aws_default_subnet'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSDefaultVPC(Resource):

    resource_type = 'aws_default_vpc'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSDefaultVPCDHCPOptions(Resource):

    resource_type = 'aws_default_vpc_dhcp_options'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEgressOnlyInternetGateway(Resource):

    resource_type = 'aws_egress_only_internet_gateway'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSFlowLog(Resource):

    resource_type = 'aws_flow_log'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSInternetGateway(Resource):

    resource_type = 'aws_internet_gateway'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSMainRouteTableAssociation(Resource):

    resource_type = 'aws_main_route_table_association'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSNATGateway(Resource):

    resource_type = 'aws_nat_gateway'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSNetworkACL(Resource):

    resource_type = 'aws_network_acl'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSNetworkACLRule(Resource):

    resource_type = 'aws_network_acl_rule'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSNetworkInterface(Resource):

    resource_type = 'aws_network_interface'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSNetworkInterfaceAttachment(Resource):

    resource_type = 'aws_network_interface_attachment'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSRoute(Resource):

    resource_type = 'aws_route'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSRouteTable(Resource):

    resource_type = 'aws_route_table'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSRouteTableAssociation(Resource):

    resource_type = 'aws_route_table_association'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSDefaultSecurityGroup(Resource):

    resource_type = 'aws_default_security_group'
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


class AWSNetworkInterfaceSGAttachment(Resource):

    resource_type = 'aws_network_interface_sg_attachment'
    taggable = False

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


class AWSSubnet(Resource):

    resource_type = 'aws_subnet'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPC(Resource):

    resource_type = 'aws_vpc'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCDCHPOptions(Resource):

    resource_type = 'aws_vpc_dhcp_options'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCDCHPOptionsAssociation(Resource):

    resource_type = 'aws_vpc_dhcp_options_association'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCEndpoint(Resource):

    resource_type = 'aws_vpc_endpoint'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCEndpointConnectionNotification(Resource):

    resource_type = 'aws_vpc_endpoint_connection_notification'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCEndpointRouteTableAssociation(Resource):

    resource_type = 'aws_vpc_endpoint_route_table_association'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCEndpointService(Resource):

    resource_type = 'aws_vpc_endpoint_service'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCEndpointServiceAllowedPrincipal(Resource):

    resource_type = 'aws_vpc_endpoint_service_allowed_principal'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCEdnpointSubnetAssociation(Resource):

    resource_type = 'aws_vpc_endpoint_subnet_association'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCIPv4CIDRBlockAssociation(Resource):

    resource_type = 'aws_vpc_ipv4_cidr_block_association'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCPeeringConnection(Resource):

    resource_type = 'aws_vpc_peering_connection'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCPeeringConnectionAccepter(Resource):

    resource_type = 'aws_vpc_peering_connection_accepter'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPCPeeringConnectionOptions(Resource):

    resource_type = 'aws_vpc_peering_connection_options'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPNConnection(Resource):

    resource_type = 'aws_vpn_connection'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPNConnectionRoute(Resource):

    resource_type = 'aws_vpn_connection_route'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPNGateway(Resource):

    resource_type = 'aws_vpn_gateway'
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPNGatewayAttachment(Resource):

    resource_type = 'aws_vpn_gateway_attachment'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVPNGatewayRoutePropagation(Resource):

    resource_type = 'aws_vpn_gateway_route_propagation'
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)