#!/usr/bin/env python
#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

test_reqs = ["nose>=1.3.7", "parameterized>=0.6.1"]

requirements = ["numpy>=1.9.2", "pandas>=0.16.1", "six", "pandas-datareader>=0.2"]

extras_requirements = {"dev": ["nose==1.3.7", "parameterized==0.6.1", "flake8==2.5.1"]}


if __name__ == "__main__":
    setup(
        name="merq_empyrical_noscipy",
        version="1.0.1",
        packages=["empyrical"],
        install_requires=requirements,
    )
