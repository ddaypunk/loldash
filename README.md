loldash
=====

Compiled jsx files (placed in `static/scripts/build/`) are not in source control.
To automatically compile jsx files:
* `npm install -g react-tools`
* `jsx --watch static/scripts/jsx/ static/scripts/build/`

`vagrant up` will start a server running nginx with an ip of 192.168.50.10. Django should be run locally for debugging via PyCharm.

Before the Django project can be run, a `loldash/loldash/settings_local.py` file must be created. Copy `loldash/loldash/default_settings_local.py` and replace any missing values with the appropriate settings.

Django urls will all be prefixed with `api/`. When a new Django app is added to the project, a reference to its urls should be placed in the base_patterns list located in `loldash/urls.py`.

=====
This product is not endorsed, certified or otherwise approved in any way by Riot Games, Inc. or any of its affiliates.
