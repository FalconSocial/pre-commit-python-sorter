import argparse

from isort import isort


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--diff-only', action='store_true', dest='diff_only')
    parser.add_argument('--dont-check', action='store_false', dest='check')
    parser.set_defaults(diff_only=False)
    parser.set_defaults(check=True)
    args = parser.parse_args(argv)

    result = []

    for filename in args.filenames:
        isort.SortImports(filename, show_diff=args.diff_only)
        if args.check:
            f = isort.SortImports(filename, check=args.check)
            if f.incorrectly_sorted is True:
                result.append(filename)
    return len(result)

if __name__ == '__main__':
    exit(main())
