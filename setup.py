# coding=utf-8

from setuptools import setup

try:
	import octoprint_setuptools
except:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
	      "the same python installation that OctoPrint is installed under?")
	import sys
	sys.exit(-1)


########################################################################################################################

plugin_identifier = "jamsentry"
plugin_package = "octoprint_jamsentry"
plugin_name = "OctoPrint-JamSentry"
plugin_version = "2.0.1"
plugin_description = """Responds to filament jam alerts from JamSentry"""
plugin_author = "Michael Ford"
# Plugin originally written by: Stephen Hayes
plugin_url = "https://github.com/hotbutteredhtml/OctoPrint-JamSentry"
plugin_license = "AGPLv3"
plugin_requires = []
plugin_additional_data = []
plugin_additional_packages = []
plugin_ignored_packages = []
additional_setup_parameters = {}

########################################################################################################################



setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
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
