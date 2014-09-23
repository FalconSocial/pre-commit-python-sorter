import argparse
import sys

from isort import isort


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    args = parser.parse_args(argv)
    print args
    # argv = argv if argv is not None else sys.argv[1:]
    # for filename in argv:
    #     isort.SortImports(filename, show_diff=True)
    return 0

if __name__ == '__main__':
    exit(main())
