from setuptools import setup, find_packages, tests
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(name='scholarec',
      version='0.5',
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
