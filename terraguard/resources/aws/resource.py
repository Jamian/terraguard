from terraguard.validators import must_contain, must_not_contain, must_equal


class Resource:

    name = ""
    resource_type = 'resource'
    taggable = False

    def __init__(self, config):
        self.config = config
        self.violations = {}
        self.name = self.config['address']

    def validate(self, rulesets):
        rulesets_to_apply = ['global'] if 'global' in rulesets else []
        if self.resource_type in rulesets:
            rulesets_to_apply.append(self.resource_type)

        for resource in rulesets_to_apply:
            if 'attributes' in rulesets[resource]:
                if 'tags' in rulesets[resource]['attributes'] and self.taggable:
                    for rule in rulesets[resource]['attributes']['tags']:
                        rule_definition = rulesets[resource]['attributes']['tags'][rule]
                        if rule == 'must_contain':
                            must_contain(rule_definition, 'tags', self)
                        elif rule == 'must_not_contain':
                            must_not_contain(rule_definition, 'tags', self)
                        elif rule == 'must_equal':
                            must_equal(rule_definition, 'tags', self)
