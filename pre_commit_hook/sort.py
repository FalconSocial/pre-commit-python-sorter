import argparse

from isort import isort


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--diff-only', action='store_true', dest='diff_only')
    parser.set_defaults(diff_only=False)
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:
        if args.diff_only:
            isort.SortImports(filename, show_diff=True)
            output = isort.SortImports(filename, check=True)
            if output.incorrectly_sorted is True:
                return_value = 1
        else:
            isort.SortImports(filename)
    return return_value

if __name__ == '__main__':
    exit(main())
