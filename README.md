A simple `config` loading library. Allows access to config items using
dot-notation, which I find easier to read. The config object can be created by
passing a dictionary to the constructor, or via a static function that
loads config from a json-formatted file. Also has built-in support for decoding
base64 config items.

## Examples

### Sample config file
```
{
  "some_username": "foo"
  "some_password": "bar",
  "some_secret_key": "TxPHiAEyU0qlUivc71HVB5gj2USpVvMH",
  "b64:some_complicated_thing": "dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZwo=",
}
```

### Loading the config data
```
from configinator import Config

config = Config.load_from_file('/app/secrets/config.json')

print(config.some_username)
# foo

print(config.some_password)
# bar

print(config.some_secret_key)
# TxPHiAEyU0qlUivc71HVB5gj2USpVvMH

print(config.some_complicated_thing)
# the quick brown fox jumps over the lazy dog
```
