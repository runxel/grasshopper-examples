# Code in your editor of choice and let Grasshopper read this file
# with the "Read File" dialog, then pipe it into the "code" input 
# of a GhPython node.
# See also https://github.com/runxel/grasshopper-examples

import Rhino.Geometry as rg

pt = rg.Point3d(x, y, z)
a = rg.Sphere(pt, 1)
