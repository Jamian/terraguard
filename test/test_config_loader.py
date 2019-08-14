import mock

from terraguard.terraguard import load_configs


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="{'rulesets': {}}")
def test_empty_configs_return_empty_config_with_no_errors(mock_open):

    config = load_configs()
    assert(config == {'rulesets': {}})
