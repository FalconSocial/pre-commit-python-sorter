from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_python_sort',
    description='A pre-commit hook to sort your python imports.',
    url='https://github.com/pre-commit/pre-commit-hooks',
    version='0.0.1-dev',

    author='Kasper Jacobsen',
    author_email='k@mackwerk.dk',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        'isort',
    ],
    entry_points={
        'console_scripts': [
            'python-import-sorter = pre_commit_hook.sort:main',
        ],
    },
)
