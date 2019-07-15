from terraguard.resources.aws.resource import Resource


class AWSAMI(Resource):

    resource_type = "aws_ami"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSAMICopy(Resource):

    resource_type = "aws_ami_copy"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSAMIFromInstance(Resource):

    resource_type = "aws_ami_from_instance"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSAMILaunchPermission(Resource):

    resource_type = "aws_ami_from_instance"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEBSDefaultKMSKey(Resource):

    resource_type = "aws_ebs_default_kms_key"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEBSEncryptionByDefault(Resource):

    resource_type = "aws_ebs_encryption_by_default"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEBSSnapshot(Resource):

    resource_type = "aws_ebs_snapshot"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEBSSnapshotCopy(Resource):

    resource_type = "aws_ebs_snapshot_copy"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEBSVolume(Resource):

    resource_type = "aws_ebs_volume"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2CapacityReservation(Resource):

    resource_type = "aws_ec2_capacity_reservation"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2ClientVPNEndpoint(Resource):

    resource_type = "aws_ec2_client_vpn_endpoint"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2ClientVPNNetworkAssociation(Resource):

    resource_type = "aws_ec2_client_vpn_network_association"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2Fleet(Resource):

    resource_type = "aws_ec2_fleet"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGateway(Resource):

    resource_type = "aws_ec2_transit_gateway"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGatewayRoute(Resource):

    resource_type = "aws_ec2_transit_gateway_route"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGatewayRouteTable(Resource):

    resource_type = "aws_ec2_transit_gateway_route_table"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGatewayRouteTableAssociation(Resource):

    resource_type = "aws_ec2_transit_gateway_route_table_association"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGatewayRouteTablePropagation(Resource):

    resource_type = "aws_ec2_transit_gateway_route_table_propagation"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGatewayVPCAttachment(Resource):

    resource_type = "aws_ec2_transit_gateway_vpc_attachment"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEC2TransitGatewayVPCAttachmentAccepter(Resource):

    resource_type = "aws_ec2_transit_gateway_vpc_attachment_accepter"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEIP(Resource):

    resource_type = "aws_eip"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSEIPAssociation(Resource):

    resource_type = "aws_eip_association"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSInstance(Resource):

    resource_type = "aws_instance"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSKeyPair(Resource):

    resource_type = "aws_key_pair"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLaunchConfiguration(Resource):

    resource_type = "aws_launch_configuration"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSLaunchTemplate(Resource):

    resource_type = "aws_launch_template"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSPlacmentGroup(Resource):

    resource_type = "aws_placement_group"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSnapshotCreateVolumePermission(Resource):

    resource_type = "aws_snapshot_create_volume_permission"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSpotDatafeedSubscription(Resource):

    resource_type = "aws_spot_datafeed_subscription"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSpotFleetRequest(Resource):

    resource_type = "aws_spot_fleet_request"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSSpotInstanceRequest(Resource):

    resource_type = "aws_spot_instance_request"
    taggable = True

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)


class AWSVolumeAttachment(Resource):

    resource_type = "aws_volume_attachment"
    taggable = False

    def __init__(self, config):
        self.violations = {}
        super().__init__(config)

    def validate(self, rulesets):
        return super().validate(rulesets)
