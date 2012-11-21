## __Workviz__

Workviz is a prototype tool for viewing live server metadata in a compact way. The original intention was not to create an admin tool but rather a way for human’s to use their natural pattern recognition to identify properties in a server cluster.

Written in python, using NumPy and VPython, Workviz displays a 3d representation of user-selected metrics about any number of physical machines. It also supports simulations by creating alternate “Workload Generators” and inserting them on the fly. Currently there are two workload generators built-in:
 *   one that consumes data from a script (Used for real-time server data). 
 *   one that uses a Normal Distribution to generate fake data.

[Demo Videos](http://www.youtube.com/watch?v=2_nB1rQ3p-M)
