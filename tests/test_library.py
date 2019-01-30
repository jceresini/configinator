import pytest
import json
from mock import patch, mock_open

from configinator import Config


test_config_data = {
    'some_username': 'admin',
    'some_password': 'foofoo123',
    'b64:some_secret': 'dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZwo=',
    'nope:some_thing': 'qwerty32',
    'nested': {
        'item': 'data',
        'item2': 'moardata'
    }
}

test_config_json = json.dumps(test_config_data)

def test_create_from_dict():
    config = Config(test_config_data)
    assert config.some_username == 'admin'
    assert 'brown fox' in config.some_secret

def test_nested_data():
    config = Config(test_config_data)
    assert config.nested.__class__ == Config
    assert config.nested.item == 'data'

def test_bad_attribute():
    config = Config(test_config_data)

    with pytest.raises(AttributeError):
        config.fake_item

def test_use_as_dict():
    config = Config(test_config_data)
    with pytest.raises(TypeError):
        config['some_username']

@patch("builtins.open", create=True)
def test_load_from_file(m):
    m.side_effect = mock_open(read_data=test_config_json)

    config = Config.load_from_file('fake_name')
    assert config.some_username == 'admin'
    assert 'brown fox' in config.some_secret

@patch("builtins.open", create=True)
def test_load_from_non_existant_file(m):
    m.side_effect = [
        IOError
    ]
    with pytest.raises(IOError):
        config = Config.load_from_file('fake_name')
