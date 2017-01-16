[![Build Status](https://travis-ci.org/FalconSocial/pre-commit-python-sorter.svg?branch=master)](https://travis-ci.org/FalconSocial/pre-commit-python-sorter)
[![Coverage Status](https://img.shields.io/coveralls/FalconSocial/pre-commit-python-sorter.svg)](https://coveralls.io/r/FalconSocial/pre-commit-python-sorter)


Pre-commit python module sorter
===============================

This is a [pre-commit](https://github.com/pre-commit) hook that will sort your
imports for you (or show you how it should be done).

* [pre-commit](https://github.com/pre-commit)
* [isort](https://github.com/timothycrosley/isort)


Add this to your ``.pre-commit-config.yaml`` file

    - repo: git://github.com/FalconSocial/pre-commit-python-sorter
      sha: 1.0.4
      hooks:
      - id: python-import-sorter
        args: ['--silent-overwrite']

Available flags:

* ``--silent-overwrite``: The hook won't fail if it has to change files. It will
    just do it.
* ``--check-only``: The hook will not change any files.
* ``--diff``: If imports are not ordered correctly, print a diff of required
    changes to fix the import order.

The hook supports [isort's configuration files](https://github.com/timothycrosley/isort#configuring-isort) - Please refer to the isort documentation for reference

Development: ``pip install -r requirements-dev.txt``

Testing: ``py.test --cov pre_commit_hook tests/``
