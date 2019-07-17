from terraguard.resources.aws.aws_vpc import AWSDefaultVPC, AWSVPC


def test_vpc_ipv6_rulesets():
    rulesets = {AWSVPC.resource_type: [{
        'expression': 'assign_ipv6_address_on_creation',
        'must_equal': False
    }]}

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

    rulesets = {AWSVPC.resource_type: [{
        'expression': 'assign_ipv6_address_on_creation',
        'must_equal': False
    }, {
        'expression': 'tags',
        'must_equal': {
            'test': 'bleepbloop'
        }
    }]}

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
    rulesets = {AWSDefaultVPC.resource_type: [{
        'expression': 'assign_ipv6_address_on_creation',
        'must_equal': False
    }]}

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
