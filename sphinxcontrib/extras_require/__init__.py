#!/usr/bin/env python3
#
#  __init__.py
"""
A Sphinx directive to specify that a module has extra requirements, and show how to install them.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#
#      * Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
#      * Redistributions in binary form must reproduce the above copyright notice,
#        this list of conditions and the following disclaimer in the documentation
#        and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
#  OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# stdlib
from typing import Any, Dict

# 3rd party
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

# this package
from sphinxcontrib.extras_require.directive import ExtrasRequireDirective
from sphinxcontrib.extras_require.sources import sources

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"
__license__: str = "BSD"
__version__: str = "0.1.1"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["purge_extras_requires", "setup"]

# For type hinting install docutils-stubs


def purge_extras_requires(app: Sphinx, env: BuildEnvironment, docname: str) -> None:
	"""
	Remove all redundant extras_require nodes.

	:param app:
	:param env:
	:type env:
	:param docname: The name of the document to remove nodes for.

	:return:
	"""

	if not hasattr(env, "all_extras_requires"):
		return

	env.all_extras_requires = [  # type: ignore
		todo for todo in env.all_extras_requires  # type: ignore
		if todo["docname"] != docname
		]


def setup(app: Sphinx) -> Dict[str, Any]:
	"""
	Setup Sphinx Extension.

	:param app:

	:return:
	"""

	# Location of package source directory relative to documentation source directory
	app.add_config_value("package_root", None, "html")

	app.add_directive("extras-require", ExtrasRequireDirective)
	app.connect("env-purge-doc", purge_extras_requires)

	return {
			"version": __version__,
			"parallel_read_safe": True,
			"parallel_write_safe": True,
			}
