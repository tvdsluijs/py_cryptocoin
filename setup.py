from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='py_cryptocoin',
      version='1.0.1',
      description='Python3 CryptoCoin data parser',
      long_description=readme(),
      url='https://bitbucket.org/tvdsluijs/py_cryptocoin',
      author='Theo van der Sluijs',
      author_email='theo@vandersluijs.nl',
      license='CC BY-NC-SA 4.0',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
        ],
      keywords='crypto cryptocoin coins cryptocoins blockchain',
      packages=['py_cryptocoin'],
      zip_safe=False)