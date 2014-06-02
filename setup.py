from setuptools import find_packages, tests, setup
#from distutils.core import setup
from pip.req import parse_requirements
import os
import codecs

def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]

# Use the VERSION file to get ScholaRec version
version_file = os.path.join(os.path.dirname(__file__), 'scholarec', 'VERSION')
with open(version_file) as fh:
    scholarec_version = fh.read().strip()

setup(name='scholarec',
      version=scholarec_version,
      description='Recommendation engine for scholarly works',
      url='https://github.com/arcolife/scholarec.git',
      packages = find_packages(),
      package_data = {'scholarec': [ 'VERSION']},
      author='Archit Sharma',
      author_email='archit.py@gmail.com',
      #test_suite="tests",
      license='GPL v3',
      install_requires=install_reqs,
      #packages=['scholarec'],
      zip_safe=False)
