
if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='AoC run stuff')
    parser.add_argument('-d', default=[], nargs='+', required=True,)
    parser.add_argument('-y', default=24, required=False, type=int)
    args = parser.parse_args()
    days = args.d
    year = args.y
    if 'all' in days:
        for day in range(1, 26):
            try:
                exec("from y{}.d{} import day{}".format(year, day, day))
                exec("day{}.main()".format(day))
            except Exception:
                print("No implementation for day {}".format(day))
    else:
        for day in days:
            exec("from y{}.d{} import day{}".format(year, day, day))
            exec("day{}.main()".format(day))