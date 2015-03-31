from __future__ import print_function
import argparse
from . import stateplane


def main():
    parser = argparse.ArgumentParser('stateplane', 'Calculate the local state plane projection for a point')

    parser.add_argument('point', nargs=2, help='x, y point in WGS84 coordinates', type=float)
    parser.add_argument('-o', '--output-type', help='Output type', choices=('proj4', 'epsg', 'short'))

    args = parser.parse_args()

    print(stateplane.select(*args.point, fmt=args.output_type))

if __name__ == '__main__':
    main()
