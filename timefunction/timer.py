from time import perf_counter
import pandas as pd
import os


def time_it(f):
    """
    time_it() decorator which can be added to any function to time its run time and output its run time to
    a tab delimited file.
    :param f:
    :return:
    """
    # Initialize a counter to keep track of how many time_it() functions are running and set that to 0.
    time_it.actively_running = 0

    def time_exact(*args, **kwargs):  # The function time_exact() is run.
        # Add 1 to the counter tracking how many times the time_it() function is running to determine nesting level.
        time_it.actively_running += 1
        start_time = perf_counter()
        # The number of tabs to add is equivalent to the level of nesting,
        # which is then equivalent to the number of running instances of the time_it() function.
        tabs = '\t'*(time_it.actively_running - 1)
        # Name variable is set to the function of which this decorator is placed above.
        name = f.__name__
        # Open the time logging results file as append mode and write a new line with the executed function name.
        with open(f"{os.getcwd()}/time_logging.txt", "a+") as logs:
            logs.write('{tabs}Executing <{name}>\n'.format(tabs=tabs, name=name))
        # Function must return something to be deemed as completed.
        res = f(*args, **kwargs)
        # Open the time logging results file as append mode and write time taken with the appropriate tab nesting.
        with open(f"{os.getcwd()}/time_logging.txt", "a+") as logs:
            logs.write('{tabs}Function <{name}> execution time: {time:.3f} seconds\n'.format(
                tabs=tabs, name=name, time=perf_counter() - start_time))
        # Deduct from counter the number of active time_it() functions.
        time_it.actively_running -= 1

        return res

    return time_exact


def track_time(f):
    """
    track_time() decorator courtesy of Loong
    Outputs function runtimes to a csv file for easier parsing and obtaining global statistics.
    :param f:
    :return:
    """
    def t(*args, **kwargs):
        start_time = perf_counter()
        r = f(*args, **kwargs)
        end_time = perf_counter()
        with open(f"{os.getcwd()}/track_time.csv", "a+") as logs:
            logs.write(f"{f.__name__}, {end_time-start_time}\n")
        return r
    return t


def get_function_statistics(function_name: str, result_csv_file: str, main_function_name="main") -> float:
    data = pd.read_csv(result_csv_file, header=None)
    # Get the rows whereby the function being executed matches the function of interest in statistics.
    function_calls = data.loc[data.iloc[:, 0] == function_name]
    # Sum the rows containing the time taken for the function call of interest to give the total time.
    time_for_function = function_calls.iloc[:, 1].sum()
    # Get the total time for the overall program execution.
    main_call = data.loc[data.iloc[:, 0] == main_function_name]
    # Get the total time taken from the column of interest.
    total_time = main_call.iloc[:, 1].sum()
    # Calculate the percentage of time taken for the function of interest.
    percentage_time_function = round((100*time_for_function/total_time), 2)

    return percentage_time_function, time_for_function, total_time
