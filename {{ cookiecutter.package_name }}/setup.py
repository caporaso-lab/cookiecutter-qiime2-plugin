# ----------------------------------------------------------------------------
# Copyright (c) 2024, {{ cookiecutter.author_name }}.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import find_packages, setup

import versioneer

description = ("A template QIIME 2 plugin.")

setup(
    name="{{ cookiecutter.package_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description=description,
    url="{{ cookiecutter.project_url }}",
    entry_points={
        "qiime2.plugins": [
            "{{ cookiecutter.module_name }}="
            "{{ cookiecutter.module_name }}"
            ".plugin_setup:plugin"]
    },
    package_data={
        "{{ cookiecutter.module_name }}": ["citations.bib"],
        "{{ cookiecutter.module_name }}.tests": ["data/*"],
    },
    zip_safe=False,
)
