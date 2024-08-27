# ----------------------------------------------------------------------------
# Copyright (c) 2024, {{ cookiecutter.author_name }}.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup

import versioneer

setup(
    version=versioneer.get_version(),
)
