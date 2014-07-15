from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tostadas',
      version=version,
      description="Ejemplos de conjuntos de Tostadas",
      long_description="""\
Ejemplos de conjuntos de Tostadas, para demostrar como crear un paquete Egg Python""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python egg conjuntos tostadas',
      author='Yanina Muradas M',
      author_email='yaninamuradas@gmail.com',
      url='https://github.com/Yani18/tostadas',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
