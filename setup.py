"""Script for building the CusDeb Anonymous package. """

from setuptools import setup

try:
    import pypandoc

    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (ImportError, OSError):
    # OSError is raised when pandoc is not installed.
    LONG_DESCRIPTION = ('CusDeb Anonymous is a microservice intended for issuing JWT tokens for '
                        'anonymous access to CusDeb.')

with open('requirements.txt') as outfile:
    REQUIREMENTS_LIST = outfile.read().splitlines()

setup(name='cusdeb_anonymous',
      version='0.1',
      description='CusDeb Anonymous package',
      long_description=LONG_DESCRIPTION,
      url='https://github.com/tolstoyevsky/cusdeb-anonymous',
      author='Evgeny Golyshev <eugulixes@gmail.com>',
      maintainer='Evgeny Golyshev',
      maintainer_email='Evgeny Golyshev <eugulixes@gmail.com>',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      scripts=['bin/server.py'],
      packages=['cusdeb_anonymous'],
      include_package_data=True,
      data_files=[('', ['requirements.txt', 'LICENSE'])],
      install_requires=REQUIREMENTS_LIST)
