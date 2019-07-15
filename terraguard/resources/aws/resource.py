from terraguard.validators import must_contain, must_equal


class Resource:

    name = ""
    resource_type = 'resource'
    taggable = False

    def __init__(self, config):
        self.config = config
        self.violations = {}
        self.name = self.config['address']

    def validate(self, rulesets):
        rulesets_to_apply = ['global']
        if self.resource_type in rulesets:
            rulesets_to_apply.append(self.resource_type)

        for ruleset_key in rulesets_to_apply:
            for i, _ in enumerate(rulesets[ruleset_key]):
                for i, _ in enumerate(rulesets[ruleset_key]):
                    rule = rulesets[ruleset_key][i]
                    if rule['expression'] == 'tags' and self.taggable:
                        if 'must_contain' in rule:
                            must_contain(rule, 'tags', self)
                        if 'must_equal' in rule:
                            must_equal(rule, 'tags', self)
