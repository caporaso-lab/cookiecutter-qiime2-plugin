# ----------------------------------------------------------------------------
# Copyright (c) 2024, {{ cookiecutter.author_name }}.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Citations, Plugin
from q2_types.feature_table import FeatureTable, Frequency
from {{ cookiecutter.module_name }} import __version__
from {{ cookiecutter.module_name }}._methods import duplicate_table

citations = Citations.load("citations.bib", package="{{ cookiecutter.module_name }}")

plugin = Plugin(
    name="{{ cookiecutter.plugin_name }}",
    version=__version__,
    website="{{ cookiecutter.project_url}}",
    package="{{ cookiecutter.module_name }}",
    description="{{ cookiecutter.plugin_description }}",
    short_description="{{ cookiecutter.plugin_short_description }}",
    # The plugin-level citation of 'Caporaso-Bolyen-2024' is provided as
    # an example. You can replace this with citations to other references 
    # in citations.bib.
    citations=[citations['Caporaso-Bolyen-2024']]
)

plugin.methods.register_function(
    function=duplicate_table,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    outputs=[('new_table', FeatureTable[Frequency])],
    input_descriptions={'table': 'The feature table to be duplicated.'},
    parameter_descriptions={},
    output_descriptions={'new_table': 'The duplicated feature table.'},
    name='Duplicate table',
    description=("Create a copy of a feature table with a new uuid. "
                 "This is for demonstration purposes only. 🧐"),
    citations=[]
)
