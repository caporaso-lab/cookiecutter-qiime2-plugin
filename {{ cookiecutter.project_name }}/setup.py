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
    name="{{ cookiecutter.project_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD-3-Clause",
    packages=find_packages(),
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description=description,
    url="{{ cookiecutter.project_url }}",
    entry_points={
        "qiime2.plugins": ["{{ cookiecutter.project_name }}={{ cookiecutter.project_slug }}.plugin_setup:plugin"]
    },
    package_data={
        "{{ cookiecutter.project_slug }}": ["citations.bib"],
        "{{ cookiecutter.project_slug }}.tests": ["data/*"],
    },
    zip_safe=False,
)
