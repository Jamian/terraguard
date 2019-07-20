from terraguard.validators import must_contain, must_not_contain, must_equal
from terraguard.resources.aws.taggable_resources import taggable_resources


class AWSResource:

    name = ""
    resource_type = 'resource'
    taggable = False

    def __init__(self, resource_type, config):
        self.config = config
        self.violations = {}
        self.name = self.config['address']

        self.resource_type = resource_type
        if resource_type in taggable_resources:
            self.taggable = True

    def validate(self, rulesets):
        rulesets_to_apply = ['global'] if 'global' in rulesets else []
        if self.resource_type in rulesets:
            rulesets_to_apply.append(self.resource_type)
        for resource in rulesets_to_apply:
            ruleset = rulesets[resource]
            for key in ruleset:
                if key == 'must_contain':
                    must_contain(ruleset['must_contain'], self)
                if key == 'must_not_contain':
                    must_not_contain(ruleset['must_not_contain'], self)
                if key == 'must_equal':
                    must_equal(ruleset['must_equal'], self)
                if key == 'attributes':
                    for attribute_key in ruleset['attributes']:
                        if attribute_key == 'tags' and not self.taggable:
                            continue
                        else:
                            for rule in ruleset['attributes'][attribute_key]:
                                rule_definition = ruleset['attributes'][attribute_key][rule]
                                if rule == 'must_contain':
                                    must_contain(rule_definition, self, attribute_key)
                                elif rule == 'must_not_contain':
                                    must_not_contain(rule_definition, self, attribute_key)
                                elif rule == 'must_equal':
                                    must_equal(rule_definition, self, attribute_key)

    def add_violation(self, full_address, violation):
        if full_address not in self.violations:
            self.violations[full_address] = []
        self.violations[full_address].append(violation)
