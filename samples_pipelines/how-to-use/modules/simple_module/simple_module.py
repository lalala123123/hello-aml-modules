# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import os
import sys
import argparse
import logging
import traceback
import pkg_resources
from azureml.core import Run

# get run from context
azureml_run = Run.get_context(allow_offline=False)

# report fake metrics
azureml_run.log("dummy_metric", 99.9)
azureml_run.log_row("dummy_metric_row", foo=42, bar="whatever")

# print python version
print(f"Probe has python version {sys.version_info}")

# print all python packages and their versions
for i in pkg_resources.working_set:
    print("Probe has python package {} installed with version {}".format(i.key, i.version))

# lists all the available environment variables
for k in os.environ:
    print("Probe env variable {}={}".format(k, os.environ[k]))