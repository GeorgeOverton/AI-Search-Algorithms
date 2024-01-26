# README
## How to setup
As this is a python program you must download a python interpreter to do so you can either install it by
visiting the <a href="https://www.python.org/downloads/" target="_blank">Python</a> website and downloading the latest version or if you are using an 
IDE like VS code you can install it via the IDE

To set up my application you will need to represent the maze you want to solve in the format of '-' and '#'
where '-' represent places where one may be able to go and '#' represents places where you can not go
(hedges/walls). Then save this maze as a .txt file in the /mazes subdirectory of the application.


## How to run
To run this application on a maze you will need to open using an IDE the code which resides in the "maze-solver.py" 
file in the root directory. When you have the code open make your way down to the bottom where you should see a 
variable called FILENAME, If you change the string that is stored in this variable to the name of your file then run
the code either via the built-in run-in the IDE you are using or using the following command in command prompt/
PowerShell or any other terminal you have

```
python3 maze-solver.py
```

Once run the program will output the time taken the length of the path and the number of nodes visited into the 
terminal. It will also save the solved maze into a new text file with the path taken denoted by ‘.’. The file 
will be located in the /results folder under the same name as the maze file. Along with this, it will also add 
a file that was solved via a greedy algorithm.