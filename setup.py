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

setup(
  name="scholarec",
  version=scholarec_version,
  author="Archit Sharma",
  author_email="archit.py@gmail.com",
  description="Recommendation engine for scholarly works",
  license = "GPL v3",
  keywords = "python ArXiv API recommendation",
  url="https://github.com/arcolife/scholarec",
  install_requires=install_reqs,
  packages = find_packages(),
  package_data = {'scholarec': ['VERSION']},
  zip_safe=False,
  long_description = local_file('README.md').read(),
  #test_suite="tests",
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers'
    ]
)
