from setuptools import find_packages, tests, setup
#from distutils.core import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

import os

# Use the VERSION file to get ScholaRec version
# version_file = os.path.join(os.path.dirname(__file__), 'scholarec', 'VERSION')
version_file = os.path.abspath(os.path.join(os.path.split(__file__)[0], 'scholarec', 'VERSION'))

with open(version_file) as fh:
    scholarec_version = fh.read().strip()

setup(name='scholarec',
      version=scholarec_version,
      description='Recommendation engine for scholarly works',
      url='https://github.com/arcolife/scholarec.git',
      packages = find_packages(),
      author='Archit Sharma',
      author_email='archit.py@gmail.com',
      #test_suite="tests",
      license='GPL v3',
      install_requires=reqs,
      #packages=['scholarec'],
      zip_safe=False)
