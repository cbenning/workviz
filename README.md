## Workviz

Workviz is a prototype tool for viewing live server metadata in a compact way. The original intention was not to create an admin tool but rather a way for human’s to use their natural pattern recognition to identify properties in a server cluster.

Written in python, using NumPy and VPython, Workviz displays a 3d representation of user-selected metrics about any number of physical machines. It also supports simulations by creating alternate “Workload Generators” and inserting them on the fly. Currently there are two workload generators built-in:

one which consumes data from a script (Used for real-time server data) and another which uses a Normal Distribution to generate fake data.

<embed src="http://www.youtube.com/watch?v=2_nB1rQ3p-M" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385"></embed></object>
http://www.youtube.com/watch?v=2_nB1rQ3p-M