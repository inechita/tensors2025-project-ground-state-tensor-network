# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:25:30 2025

@author: Soham
"""

import torch 
import tensorkrowch as tk

node = tk.Node(shape=(2,5,2))

tensor= torch.randn(2,5,2)
node1 = tk.Node(tensor=tensor)

#Shape
print(node.shape)
print(node1.shape)

#Shows the tensor with which the node is associated
print(node.tensor)
print(node1.tensor)

#Naming the legs of the node 
node2 = tk.randn(shape=(2,5,2,15),
                axes_names=('left', 'input', 'right','other'))

node2.get_axis('left').name = 'other_left'  # Changes the axis' name
idx = node2.get_axis_num('other')      # Returns index of 'other_left'
                                           # in the axes list

print(idx)                                           