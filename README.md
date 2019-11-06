# Traveling Salesman

This coursework considers a simplified version of the travelling salesman problem.

## Purposes of this assignment

- To get skills for solving more complex problems with programs.
- To make you consider different search algorithms and data structures.
- To give you more practice with writing tests.
- To gain experience with *Test-Driven-Development* (TDD).

## General idea of the assignment

Suppose there are a number of "cities", as in shown in Figure 1:

![Figure 1, Cities](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure1.png)



The distance between any two cities with the coordinates (x1, y1) and (x2,y2) is
 the standard Euclidean distance, that is, 

sqrt((x1-x2)^2 + (y1-y2)^2)

Thus, we assume that the Earth is "flat" for the purposes of this assignment.
A traveling salesman wishes to visit every city exactly once, 
then return to their starting point. (It doesn't matter what city is 
the starting point.) Such a path is called a *circuit*, 
as in Figure 2:

![Figure 2. A circuit](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure2.png)

However, the salesman also wishes to minimise the total distance that 
must be traveled.

This is a classic computer science problem, known as the 
**Traveling Salesman problem**. You can find algorithms for 
finding reasonably good solutions on the web, and you are welcome to look 
at those algorithms. However, we want you use a *hill climbing& approach, 
where you start with "any" solution, and try to progressively improve 
it until you can't improve it any more.

## Specific requirements

### Data representation

We are providing a file, `city-data.txt`, containing the 
latitudes and longitudes of the fifty state capitals of the U.S.A. 
Each line contains:
- the name of the state, 
- the name of the city, 
- the latitude, and 
- the longitude. 

These four items are separated by **tabs** (\t symbol). 
Read this file in as a list of four-tuples.
The list tuples will be referred to as a *"road map"*. 
It represents the path the salesman follows, starting with the 
first city in the list and ending back at the first city in the list.
You can assume that the format of the input file as above. 

Note however that the file name as well as its contents can be arbitrary (e.g., 
it can be a file `Brazil.txt` with the info on Brazilian states/cities).

While we will require these particular data representations as 
function parameters and function results, this does not imply that 
you have to work with these representations as you solve the problems.
What you do inside the functions is up to you, as long as they work as expected.
(Python makes it easy to convert from one kind of sequence to another.)

### Required functions (file `cities.py`)

`def read_cities(file_name)`
>  Read in the cities from the given `file_name`, and return 
>  them as a list of four-tuples: 
  ```
  [(state, city, latitude, longitude), ...] 
  ```

Note that the list above will be used as your initial 
`road_map`, that is, 
```
Alabama -> Alaska -> Arizona -> ... -> Wyoming.
```
as in the example of the file `city-data.txt`
  
`def print_cities(road_map)`
> Prints a list of cities, along with their locations. 
> Print up to two digits after the decimal point.

`def compute_total_distance(road_map)`
> Returns, as a floating point number, the sum of the distances of all 
> the connections in the `road_map`. Remember that it's a cycle, so that 
> for example in the initial `road_map` above, Wyoming connects to Alabama...


`def swap_cities(road_map, index1, index2)`
> Take the city at location `index` in the `road_map`, and the 
> city at location `index2`, swap their positions in the `road_map`, 
> compute the new total distance, and return the tuple 
```
(new_road_map, new_total_distance)
``` 
Allow for the possibility that `index1=index2`, 
and handle this case correctly.

`def shift_cities(road_map):`
> For every index i in the `road_map`, the city at the position i moves
> to the position i+1. The city at the last position moves to the position
> 0. Return the the new road map.
    
`def find_best_cycle(road_map)`
> Using a combination of `swap_cities` and `shift_cities`, 
> try `10000` swaps/shifts, and each time keep the best cycle found so far. 
> After `10000` swaps/shifts, return the best cycle found so far.
> Use randomly generated indices for swapping.

`def print_map(road_map)`
> Prints, in an easily understandable textual format, the cities and 
> their connections, along with the cost for each connection 
> and the total cost.

`def main()`
> Requests to specify the file to load (make sure the file exists and valid), 
> reads in and prints out the city data,
> creates the *"best"* cycle, 
> prints it out.

### Required tests (file `test_cities.py`)

Programs should be tested as thoroughly as possible using 
the `pytest` unit testing framework. Functions that do input or output 
are difficult to test. Therefore, those functions, should do as little 
computation as possible, and functions that do computation, should do no 
input or output.

In this assignment `main`, `read_cities`, `print_cities`, and 
`print_map` result in input or output, so you do not need to 
write unit tests for these. Also, you do not need to test `find_best_cycle` 
because of random results.
Provide unit tests for all the  other functions, as well as any additional 
computational functions you might write.

## Programming hints

- You don't need any global variables.
- Import `random` at the top of your program; then 
  ```
  number = N * random.random() 
  ```
  will give you a floating-point number in the 
  range `0.0 <= number < N`.
- If you want to treat a list `lst` as circular (the first item 
  follows the last item), the item after `lst[i]` is not just `lst(i + 1)`,
  but is `lst[(i + 1) % len(lst)]`.
  
## Marking

The assignment as stated above will be graded on the basis of 70% total:

- **Correctness and adherence to specification** (weight 30%). We will have our own unit tests, 
  which your functions must pass. This means that the above functions must take parameters and produce results 
  exactly as specified, or our test will fail and cost you points.
- **Completeness of code, tests, and commit history** (weight 30%). You must implement all the required functions
  and the implementation must handle all the permitted inputs correctly. You must provide good code
  coverage to catch any errors before we do. We expect to see at least 5 tests for each function that 
  needs to be tested (see above). We will assess the regularity of your commit history on
  GitHub and would like to see multiple commits (at least 20) spread over a
  reasonable period of time (at least 1 month). The solutions that appear
  fully in one commit (out-of-nowhere) a day before the deadline will loose many points. 
  You will also loose some points if you do not do Initial Work (see below) on time by 
  the deadline of Session 7.
- **Style** (weight 10%).
  - Use proper indentation and spacing. 
  - Don't repeat code if you can put it in a function and just call 
    the function.  
  - Try to avoid redundancy (such as the beginner's `if better == True`).

## Extension 

To obtain additional 30% points, you will need to extend your implementation
with functionality to *visualize* road maps. There are two ways to do that:

A) Use textual printing to visualise the map. For example, you can print
the symbols | and - to "draw" the grid and spread the numbers 1,2,3... on 
that grid in such a way that they immitate with a correct scale georgarpical 
position of the cities. In that case, you would place 1 in the position that 
corresponds to the first city visited, 2 of the second, etc. (You are not 
expected to print the names of the cities, as it would need too much space.) 
For example, the road map

```
[("Kentucky", "Frankfort", 38.197274, -84.86311), 
 ("Delaware", "Dover", 39.161921	-75.526755),
 ("Minnesota", "Saint Paul", 44.95	-93.094)] 
```

can be "drawn" as follows:

![Figure 3, Visualisation by text](https://www.dcs.bbk.ac.uk/~vlad/pub/pop1/proj/Figure3.png)

Note that your implementation should correctly handle all the possible road maps
with coordinates ranging between 90 and -90 for latitude and -180 to 180 for 
longitude.

B) Implement a proper GUI window using Tkinter module. In that case, you can
do the visualisation using a similar approach to that described above. But you
shoud propertly draw the coordinate lines, mark cities by circles, and possibly label
them not only with numbers but also with city/state names. A quick tutorial on Tkinter
can be found, e.g., in https://www.datacamp.com/community/tutorials/gui-tkinter-python.
A proper documentation is at https://docs.python.org/3/library/tkinter.html#module-tkinter

Should you pursue option B), be aware that you will be studying Tkinter on your own.
None of the lectures or TAs have expertise in this module to answer technical questions.

Presumably, in B) you will spend much time learning a new tool but less time working
on the implementation because of the available drawing functions of Tkinter. 

Independently of whether you choose A) or B), you will need to provide an additional 
function 

`def visualise(road_map)`

that would either graphically print the given road_map or will open a GUI window with
the drawing of the road_map. Also, extend the functionality of your `main` function so
that it provides visualisation of the best route when found. You do not need to test
the `visualise` function.

With either A) or B) are will able to obtain up to 30%. Marking will be based on 
style of your code (see above) as well as on the usability of your solution from an 
end-user perspective. We will try your `visualise` implementation on various road maps 
and the correctness and meaningfulness of your implementation will determine your mark.

## Initial Work

In an attempt to convince you to work in TDD (Test-Driven Development)-style, 
we require that you do the following by deadline of Session 7:

- Write at least one meaningful test for each testable function in `test_cities.py`
- Write a stab (a stub is a function that does nothing or, if it must return a value, 
  returns a value that is unlikely to be correct) for each testable function in `cities.py`
- Properly set up a GitHub repo (see separate guides) and commit the files above

If you run pytest, your tests will (most certainly) fail but this will not be considered
in marking.
