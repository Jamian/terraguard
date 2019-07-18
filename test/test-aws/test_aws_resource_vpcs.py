from terraguard.resources.aws.aws_vpc import AWSSecurityGroupRule, AWSDefaultVPC, AWSVPC


def test_vpc_ipv6_rulesets():
    rulesets = {AWSVPC.resource_type: {
        'attributes': {
            'assign_ipv6_address_on_creation': {
                'must_equal': False
            }
        }
    }}

    terraform_config = {
        'address': 'someaddress',
        'values': {
            'tags': {'test': 'bleepbloop'},
            'assign_ipv6_address_on_creation': True
        }
    }

    subnet = AWSVPC(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_equal': ["Incorrect value [assign_ipv6_address_on_creation] must equal 'False' but found 'True'"]}

    rulesets = {AWSVPC.resource_type: {
        'attributes': {
            'assign_ipv6_address_on_creation': {
                'must_equal': False
            },
            'tags': {
                'must_equal': {
                    'test': 'bleepbloop'
                }
            }
        }
    }}

    terraform_config = {
        'address': 'someaddress',
        'values': {
            'tags': {'test': 'bleepbloop'},
            'assign_ipv6_address_on_creation': True
        }
    }

    subnet = AWSVPC(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_equal': ["Incorrect value [assign_ipv6_address_on_creation] must equal 'False' but found 'True'"]}


def test_default_vpc_ipv6_rulesets():
    rulesets = {AWSDefaultVPC.resource_type: {
        'attributes': {
            'assign_ipv6_address_on_creation': {
                'must_equal': False
            }
        }
    }}

    terraform_config = {
        'address': 'someaddress',
        'values': {
            'tags': {'test': 'bleepbloop'},
            'assign_ipv6_address_on_creation': True
        }
    }

    subnet = AWSDefaultVPC(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_equal': ["Incorrect value [assign_ipv6_address_on_creation] must equal 'False' but found 'True'"]}


def test_default_vpc_security_group_rule_cidr_rulesets():
    rulesets = {AWSSecurityGroupRule.resource_type: {
        'attributes': {
            'cidr_blocks': {
                'must_not_contain': '0.0.0.0/0'
            }
        }
    }}

    terraform_config = {
        'address': 'someaddress',
        'values': {
            'cidr_blocks': ['0.0.0.0/0']
        }
    }

    subnet = AWSSecurityGroupRule(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_not_contain': ["Found cidr_blocks [0.0.0.0/0] defined in aws_security_group_rule"]}
