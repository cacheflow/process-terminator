from setuptools import setup, find_packages

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name='pk',
  version='0.1',
  packages=find_packages(),
  include_package_data=True,
  entry_points='''
    [console_scripts]
    pk=index:run
  ''',
)