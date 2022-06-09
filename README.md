# Python function time profiler

## About:
Pure python function time profiler to time slow functions within code and output them as tab delimited results according 
to function nesting.

* Currently, just a single script which you can copy and paste into your project's directory (not a module yet).
* Only pandas as a dependency for getting function run time statistics.
* Just import `timefunction.timer.time_it` or `timefunction.timer.track_time`, and add them as decorators to the functions 
you would like to time.
* Example usage can be seen in the demo.py file.

## Usage:
```python3 demo.py``` will output a tab delimited text file with the number of tabs corresponding to function nesting 
as an example.
* To use, add the `@time_it` decorator to your `main` function and other functions you wish to track the time of.
* Running your `main.py` script will result in a tab delimited text file generated something like the example below:
* From this example, we can see that in each iteration of the for loop in the `main.py`, the `slow_function` took up 
majority of the time of 6 seconds which was double the time taken of the `mfe_scorer`.

```
Executing <main>
	Executing <slow_function>
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.001 seconds
	Function <slow_function> execution time: 6.006 seconds
	Executing <mfe_scorer>
	Function <mfe_scorer> execution time: 3.031 seconds
	Executing <slow_function>
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
	Function <slow_function> execution time: 6.007 seconds
	Executing <mfe_scorer>
	Function <mfe_scorer> execution time: 2.992 seconds
	Executing <slow_function>
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.001 seconds
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
		Executing <nested_sleep>
		Function <nested_sleep> execution time: 2.002 seconds
	Function <slow_function> execution time: 6.006 seconds
	Executing <mfe_scorer>
	Function <mfe_scorer> execution time: 2.955 seconds
Function <main> execution time: 26.999 seconds
```