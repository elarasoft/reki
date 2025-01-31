from setuptools import setup, find_packages

# https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications

setup(
    name="reki",
    version="0.1",

    description='''This is a template description for a new project.''',

    author='Rekimart',
    author_email='support@rekimart.com',

    url='https://github.com/elarasoft/reki',

    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),


    packages=find_packages(exclude=['test*', 'Test*']),

    package_data={
        '': ['README.md', 'LICENSE'],
        'reki': ['config.yaml.sample']
      },


    scripts=['main.py'],

    entry_points={
          'console_scripts': [
              'reki = main:main',
          ],
      },

    install_requires=[
        'PyYAML==4.2b1',
      ],


)
