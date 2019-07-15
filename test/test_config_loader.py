import os
import yaml

from click.testing import CliRunner

from terraguard.terraguard import validate

# def test_no_config_raises_an_error():

#     with pytest.raises(Exception):
#         validate()


# @mock.patch('terraguard.')
# def test_config_loads_if_exists():
#     config = {
#         'rulesets': {
#             'global': [
#                 {
#                     'expression': 'tags',
#                     'must_contain': ['Customer', 'Service']
#                 }
#             ]
#         }
#     }

#     file_full_path = os.path.join(os.getcwd(), 'terraguard.yaml')
#     with open(file_full_path, 'w') as config_file:
#         yaml.dump(config, config_file)

#     runner = CliRunner()
#     result = runner.invoke(validate, [])
#     assert result.exit_code == 0
