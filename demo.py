import RNA
from timefunction.timer import time_it
import time


with open("timefunction/covid_rna_small.txt") as data:
    sequence = data.read()


@time_it
def mfe_scorer(rna_seq):
    fc = RNA.fold_compound(rna_seq)
    _, mfe_score = fc.mfe()
    return mfe_score


@time_it
def slow_function():
    for i in range(3):
        nested_sleep()


@time_it
def nested_sleep():
    time.sleep(2)


results_list = []


@time_it
def main():
    for i in range(3):
        slow_function()
        mfe = mfe_scorer(sequence)
        results_list.append(mfe)

    print(results_list)


if __name__ == "__main__":
    main()
