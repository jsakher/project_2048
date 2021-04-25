# Benchmarks
## About the machine
The execution times and memory usage of the functions benchmarked have been determined with a machine equipped with the following hardware:
* CPU : Intel(R) Core(TM) i5-7600K CPU @ 3.80GHz
* Memory (RAM): 16,0 Go
* system : 64-bit operating system (Windows 10)
* GPU : NVIDIA GeForce GTX 970

## Execution time
The following results are execution for the main functions used in the package Game2048.  

Execution time of movement functions is very fast (beyond measurable, even when setting the time measurement tool to $10^{-15}$ seconds, as shown in `time.py`). Knowing these functions use more 'primary' functions (such as `newcell`, `stop_game` ect ...) it means that the functions they used (the 'primary' ones therefore) have unmeasurably fast execution times.  


#### Whole Games
What we call 'whole games' is the set of functions that play an entire game of 2048 automatically. It is the games using strategies, such as `random_2048`, `clockwise_2048`, `opposite_2048` and `adjacent_2048` which can be found in '`Game2048/game/Main.py`'. Whole games functions have randomness properties coming from the programming of the appearances of 2 and 4 tiles during the game (every game is the different than the other), which makes their execution time vary by an significant amount of time.  
For example, we ran `random_2048` 3 times and on these 3 tries we found an execution time of (the fact that the time is decreasing upon new tries is a pure coincidence):
1. 0.00598 s.
2. 0.00401 s.
3. 0.00299 s.

Obviously, the same goes for other 'whole games' functions. Running multiple tries of all the whole games functions, we observe that execution times of the functions `random_2048` and `clockwise_2048` are likely and that execution times of the functions `opposite_2048` and `adjacent_2048` are likely, with the execution time measured for the former group higher than the latter's. This is explained by the fact that the former group's strategies make the game take a much higher number of steps to end itself. This is explained in the report.


The statsmaker functions (which allow to produce graphics of statistics from games played with different strategies) have execution times dependant on the number of games with which one wants to generate the graphics.
Furthermore, bear in mind that the execution times of the functions statsmaker1 and statsmaker2 are also dependant on their randomness properties.
 


|      | statsmaker1(100) | statsmaker1(1000) | statsmaker1(10000) |
|------|------------------|-------------------|--------------------|
| time | 1.38713 s        | 10.92425 s        | 110.53780 s        |




**Note**: The use of Numba to accelerate the compilation hasn't shown to be applicable to the function. This issue has not been fixed as of today.

## Memory usage



