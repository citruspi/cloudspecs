#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
from cloudspecs import data_file


type_ids = [
    't2.micro',
    't2.nano',
    't2.small',
    't2.medium',
    't2.large',
    'm3.medium',
    'm3.large',
    'm3.xlarge',
    'm3.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge'
]

instance_details = {}

for instance_type in type_ids:
    data_file_path = 'aws/ec2/instances/{}.json'.format(instance_type)
    instance_details[instance_type] = json.load(data_file(data_file_path))
