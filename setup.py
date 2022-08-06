from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_medium',
    version='0.1',
    license='MIT',
    author="Toby Osborne",
    author_email='toby.osborne@fsae.co.nz',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/UOA-FSAE/functionBox',
    keywords='function box',
    install_requires=[
          'scikit-learn',
      ],

)
