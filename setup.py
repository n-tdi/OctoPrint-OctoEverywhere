# coding=utf-8

from setuptools import setup

# The plugin's identifier, has to be unique
plugin_identifier = "octoeverywhere"

# The plugin's python package, should be "octoprint_<plugin identifier>", has to be unique
plugin_package = "octoprint_octoeverywhere"

# The plugin's human readable name. Can be overwritten within OctoPrint's internal data via __plugin_name__ in the
# plugin module
plugin_name = "OctoEverywhere"

# The plugin's version. Can be overwritten within OctoPrint's internal data via __plugin_version__ in the plugin module
plugin_version = "1.10.10"

# The plugin's description. Can be overwritten within OctoPrint's internal data via __plugin_description__ in the plugin
# module
plugin_description = """Access OctoPrint remotely over the internet anywhere! Including full webcam streaming. Free. Simple. Secure."""

# The plugin's author. Can be overwritten within OctoPrint's internal data via __plugin_author__ in the plugin module
plugin_author = "Quinn Damerell"

# The plugin's author's mail address.
plugin_author_email = "quinnd@outlook.com"

# The plugin's homepage URL. Can be overwritten within OctoPrint's internal data via __plugin_url__ in the plugin module
plugin_url = "http://www.OctoEverywhere.com"

# The plugin's license. Can be overwritten within OctoPrint's internal data via __plugin_license__ in the plugin module
plugin_license = "AGPLv3"

# Any additional requirements besides OctoPrint should be listed here
# Note! Some older version of OctoPrint seems to have a system dependency that locks websocket_client to exactly 0.56.0. When we tried to update to a newer version,
# this broke that dependency and made all of OctoPrint unhappy. So don't update the version unless we really need to.
#
# UPDATE on ^ - As of October 14th 2022 - OctoPrint uses websocket-client as >=1.0.0,<2.0.0, so it installs whatever version is latests and that's 1.x. (I think the logic above applies to PY2 versions of OctoPrint?)
# BUT in websocket-client 1.4.0, there seems to be a bug where some ssl ws connections fail due to said bug: https://github.com/websocket-client/websocket-client/issues/857
# To work around this, we pin websocket client < 1.4.0. This bug mostly seems to be effecting octo4a users, maybe because their installs always pull the latest of packages?
# TODO - In the future, we should remove the lock to <1.4.0, but make sure we avoid version that have problems.
#
# We don't require a version of pillow because we don't want to mess with other plugins and we use basic, long lived APIs.
#
# Note! These need to stay in sync with .github/pylint.yml decencies.
plugin_requires = ["websocket_client>=0.56.0,<1.4.0", "requests>=2.24.0", "octoflatbuffers==2.0.3", "pillow", "certifi", "rsa", "sentry-sdk" ]

### --------------------------------------------------------------------------------------------------------------------
### More advanced options that you usually shouldn't have to touch follow after this point
### --------------------------------------------------------------------------------------------------------------------

# Additional package data to install for this plugin. The sub folders "templates", "static" and "translations" will
# already be installed automatically if they exist. Note that if you add something here you'll also need to update
# MANIFEST.in to match to ensure that python setup.py sdist produces a source distribution that contains all your
# files. This is sadly due to how python's setup.py works, see also http://stackoverflow.com/a/14159430/2028598
plugin_additional_data = []

# Any additional python packages you need to install with your plugin that are not contained in <plugin_package>.*
plugin_additional_packages = []

# Any python packages within <plugin_package>.* you do NOT want to install with your plugin
plugin_ignored_packages = []

# Additional parameters for the call to setuptools.setup. If your plugin wants to register additional entry points,
# define dependency links or other things like that, this is the place to go. Will be merged recursively with the
# default setup parameters as provided by octoprint_setuptools.create_plugin_setup_parameters using
# octoprint.util.dict_merge.
#
# Example:
#     plugin_requires = ["someDependency==dev"]
#     additional_setup_parameters = {"dependency_links": ["https://github.com/someUser/someRepo/archive/master.zip#egg=someDependency-dev"]}
additional_setup_parameters = {}

########################################################################################################################

try:
    import octoprint_setuptools
except Exception:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
        "the same python installation that OctoPrint is installed under?")
    import sys
    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires,
	additional_packages=plugin_additional_packages,
	ignored_packages=plugin_ignored_packages,
	additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
