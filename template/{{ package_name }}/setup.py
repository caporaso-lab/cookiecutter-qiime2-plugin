# ----------------------------------------------------------------------------
# Copyright (c) 2024, {{ author_name }}.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = (
    "{{ plugin_short_description }}"
)

setup(
    name="{{ package_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="{{ author_name }}",
    author_email="{{ author_email }}",
    description=description,
    url="{{ project_url }}",
    entry_points={
        "qiime2.plugins": [
            "{{ package_name }}="
            "{{ module_name }}"
            ".plugin_setup:plugin"]
    },
    package_data={
        "{{ module_name }}": ["citations.bib"],
        "{{ module_name }}.tests": ["data/*"],
    },
    zip_safe=False,
)
