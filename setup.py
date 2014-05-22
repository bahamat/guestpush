# -*- coding: utf-8 -*-

# Copyright 2014 Brian Bennett
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Setup script for the 'guestpush' distribution."""

from setuptools import setup

pkg = 'guestpush'

setup(name=pkg,
      version='0.1',
      description='Send push notifications using guest APIs',
      url='http://github.com/bahamat/%s' % pkg,
      author='Brian Bennett',
      author_email='bahamat@digitalelf.net',
      license='Apache 2.0',
      packages=['%s' % pkg],
      install_requires=[
          'requests',
      ],
      scripts=['bin/gpush'],
      zip_safe=True)
