#!/usr/bin/env python

import json
import sys
from pathlib import Path
import urllib.request
import yaml

url = 'https://raw.githubusercontent.com/qiime2/distributions/dev/data.yaml'

with urllib.request.urlopen(url) as response:
    yaml_file = response.read()
    distributions_data = yaml.safe_load(yaml_file)

stable_epoch = distributions_data['released_epoch']
latest_epoch = distributions_data['active_epoch']

with Path("cookiecutter.json") as config:
    data = json.loads(config.read_text())
    data["target_epoch"] = [stable_epoch, latest_epoch]
    data["__prompts__"]["target_epoch"] = \
        f"Are you targeting the stable ({stable_epoch}) or latest development ({latest_epoch}) QIIME 2 release?"
    config.write_text(json.dumps(data, indent=4))