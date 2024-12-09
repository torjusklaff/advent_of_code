
if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='AoC run stuff')
    parser.add_argument('-d', default=[], nargs='+', required=True, type=int)
    parser.add_argument('-y', default=24, required=False, type=int)
    args = parser.parse_args()
    days = args.d
    year = args.y
    for day in days:
        exec("from y{}.d{} import day{}".format(year, day, day))
        exec("day{}.main()".format(day))