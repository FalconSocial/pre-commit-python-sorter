import argparse

from isort import isort


def main(argv=None):
    def imports_incorrect(filename):
        return isort.SortImports(filename, check=True).incorrectly_sorted

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--diff-only', action='store_true', dest='diff_only')
    parser.add_argument('--silent-overwrite', action='store_true', dest='silent')
    parser.set_defaults(diff_only=False)
    parser.set_defaults(silent=False)
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:
        if args.diff_only:
            isort.SortImports(filename, show_diff=True)
            if imports_incorrect(filename) is True:
                return_value = 1
        elif args.silent is False:
            if imports_incorrect(filename) is True:
                return_value = 1
        else:
            isort.SortImports(filename)
    return return_value

if __name__ == '__main__':
    exit(main())
