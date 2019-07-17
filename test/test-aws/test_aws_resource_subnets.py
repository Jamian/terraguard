from terraguard.resources.aws.aws_vpc import AWSDefaultSubnet, AWSSubnet


def test_subnet_ipv6_rulesets():
    rulesets = {'aws_subnet': [{
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

    subnet = AWSSubnet(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_equal': ["Incorrect value [assign_ipv6_address_on_creation] must equal 'False' but found 'True'"]}

    rulesets = {'aws_subnet': [{
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

    subnet = AWSSubnet(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_equal': ["Incorrect value [assign_ipv6_address_on_creation] must equal 'False' but found 'True'"]}


def test_default_subnet_ipv6_rulesets():
    rulesets = {'aws_default_subnet': [{
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

    subnet = AWSDefaultSubnet(terraform_config)
    subnet.validate(rulesets)
    assert len(subnet.violations) == 1
    assert subnet.violations == {'someaddress.must_equal': ["Incorrect value [assign_ipv6_address_on_creation] must equal 'False' but found 'True'"]}
