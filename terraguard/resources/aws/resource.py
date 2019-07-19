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
            ruleset = rulesets[resource]
            for key in ruleset:
                if key == 'must_contain':
                    must_contain(ruleset['must_contain'], self)
                if key == 'attributes':
                    if 'tags' in ruleset['attributes'] and self.taggable:
                        for rule in ruleset['attributes']['tags']:
                            rule_definition = ruleset['attributes']['tags'][rule]
                            if rule == 'must_contain':
                                must_contain(rule_definition, self, 'tags')
                            elif rule == 'must_not_contain':
                                must_not_contain(rule_definition, self, 'tags')
                            elif rule == 'must_equal':
                                must_equal(rule_definition, self, 'tags')
