# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>
import argparse

from . import identify


def main():
    parser = argparse.ArgumentParser("stateplane", "Calculate the local state plane projection for a point")

    parser.add_argument("point", nargs=2, help="x, y point in WGS84 coordinates", type=float)
    parser.add_argument("-s", "--statefp", help="state FIPS code (speeds up processing)", type=str)
    parser.add_argument("-c", "--countyfp", help="county FIPS code (speeds up processing)", type=str)
    parser.add_argument("-o", "--output-type", help="Output type", choices=("epsg", "short"))

    args = parser.parse_args()

    print(identify(*args.point, fmt=args.output_type, statefp=args.statefp, countyfp=args.countyfp))


if __name__ == "__main__":
    main()
