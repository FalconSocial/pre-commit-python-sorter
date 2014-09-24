import argparse

from isort import isort


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--diff-only', action='store_true', dest='diff_only')
    parser.set_defaults(diff_only=False)
    args = parser.parse_args(argv)

    fail = False

    for filename in args.filenames:
        if args.diff_only:
            isort.SortImports(filename, show_diff=True)
            output = isort.SortImports(filename, check=True)
            fail = output.incorrectly_sorted
        else:
            isort.SortImports(filename)
    if fail is True:
        return 1
    return 0

if __name__ == '__main__':
    exit(main())
