import sys
from setuptools import find_packages
from setuptools import setup

install_requires = ['isort>=4.1.1,<5']
if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='pre_commit_python_sort',
    description='A pre-commit hook to sort your python imports.',
    url='https://github.com/FalconSocial/pre-commit-python-sorter',
    version='1.0.3',

    author='Kasper Jacobsen',
    author_email='k@mackwerk.dk',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'python-import-sorter = pre_commit_hook.sort:main',
        ],
    },
)
