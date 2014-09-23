import argparse

from isort import isort


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--diff-only', action='store_true', dest='diff_only')
    parser.set_defaults(diff_only=True)
    args = parser.parse_args(argv)

    for filename in args.filenames:
        isort.SortImports(filename, show_diff=args.diff_only)
    return 0

if __name__ == '__main__':
    exit(main())
