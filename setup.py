from setuptools import setup, find_packages

setup(name='scholarec',
      version='0.1',
      description='Recommendation engine for scholarly works',
      url='https://github.com/arcolife/scholarec.git',
      packages = find_packages(),
      author='Archit Sharma',
      author_email='archit.py@gmail.com',
      test_suite="tests",
      license='GPL v3',
      #packages=['scholarec'],
      zip_safe=False)
