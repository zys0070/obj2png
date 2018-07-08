
import sys
# assumed being called from obj2png/
sys.path.append('./src')

import numpy as np
import ObjFile

def test_open_obj():
   obj_file = './obj/bun_zipper_res2.obj'
   out_file = './obj/bun_zipper_res2.png'
   obj = ObjFile.ObjFile(obj_file)
   assert(len(obj.nodes)==8147)
   assert(len(obj.faces)==16301)
   nmin,nmax=obj.MinMaxNodes()
   assert(np.allclose(nmin, np.array([-0.094572,  0.      , -0.061874]) ) )
   assert(np.allclose(nmax, np.array([0.060935, 0.186643, 0.05869 ])) )
   obj.Plot(out_file)

"""
    >>> obj_file = '../obj/bun_zipper_res2.obj'
    >>> out_file = '../obj/bun_zipper_res2.png'
    >>> obj = ObjFile(obj_file)
    >>> len(obj.nodes)==8147
    True
    >>> len(obj.faces)==16301
    True
    >>> nmin,nmax=obj.MinMaxNodes()
    >>> np.allclose(nmin, np.array([-0.094572,  0.      , -0.061874]) )
    True
    >>> np.allclose(nmax, np.array([0.060935, 0.186643, 0.05869 ]))
    True
    >>> obj.Plot(out_file)
    """
 

