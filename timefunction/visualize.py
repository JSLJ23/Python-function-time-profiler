from timer import get_function_statistics


def main():
    print(get_function_statistics("nested_sleep", "./track_time.csv"))


if __name__ == '__main__':
    main()
