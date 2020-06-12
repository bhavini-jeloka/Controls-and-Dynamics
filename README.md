# controls-and-dynamics
The folder consists of a code for the Euler's rigid body equations using rotation matrices (a file for that is present as well) and these equations have been tested on a cube  (using 3D animation) which was drawn using the functions available on Matplotlib.

So far only constant torques have been incorporated - time varying ones would have a unique code, not a generalised one

PLEASE NOTE: 
1. For the files that involve a graph, the empty plot opens as soon as the code runs - this must be crossed off for letting the code run further (it works properly after that).
2. The entire code seems to be running slower than the given time of simulation (for instance, if the t_initial = 0 and t_final = 5, the code does not run for five seconds, but for a different interval). This is due to the interval specified in the animation function and the sleep time given in the for loop (both refer to Animation_Cube.py). I'm yet to fix this!

