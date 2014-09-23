Pre-commit python module sorter
===============================

This is a [pre-commit](https://github.com/pre-commit) hook that will sort your imports for you (or show you how it should be done).

* [pre-commit](https://github.com/pre-commit)
* [isort](https://github.com/timothycrosley/isort)


Add this to your ``.pre-commit-config.yaml`` file

    - repo: git@github.com:FalconSocial/pre-commit-python-sorter.git
      sha: cfc218a
      hooks:
      - id: python-import-sorter
        args: ['--diff-only']  # Will show only the diff and let you know that something is up

Development: ``pip install -r requirements-dev.txt``
Testing: ``py.test --cov pre_commit_hook tests/``
