import sys

from isort import isort


def main(argv=None):
    print sys.argv
    argv = argv if argv is not None else sys.argv[1:]
    print argv

    # isort.SortImports('./', show_diff=True)
    return 0

if __name__ == '__main__':
    exit(main())
