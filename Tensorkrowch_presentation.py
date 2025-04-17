# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 09:36:29 2025

@author: Soham
"""

import numpy as np
import torch
import tensorkrowch as tk 
from tensorkrowch.models import MPS

n_qubits = 5

ini_GHZ = torch.tensor([[1.0/(2.0**0.5),0.0],[0.0,1.0/(2.0**0.5)]])
fin_GHZ = torch.tensor([[1.0,0.0],[0.0,1.0]])

# print(ini_GHZ.size())

ten_lst = []

mGHZ = [[[1.0,0.0],[0.0,0.0]],
        [[0.0,0.0],[0.0,1.0]]]
tGHZ = torch.tensor(mGHZ)

ten_lst.append(ini_GHZ)
for i in range(n_qubits-2):
    ten_lst.append(tGHZ)                
ten_lst.append(fin_GHZ)

# ten_lst.append(ini_GHZ)
# ten_lst.append(fin_GHZ)

sGHZ = MPS(tensors=ten_lst)
print("MPS properties:")
print(f"- Number of sites: {sGHZ.n_features}")
print(f"- Physical dims: {sGHZ.phys_dim}")
print(f"- Bond dims: {sGHZ.bond_dim}")
print(f"- Tensor shapes: {[t.shape for t in sGHZ.tensors]}")
print(sGHZ.norm())

# MPS.contract(sGHZ)

# print("MPS properties:")
# print(f"- Number of sites: {sGHZ.n_features}")
# print(f"- Physical dims: {[t.phys_dim for t in sGHZ.tensors]}")
# print(f"- Bond dims: {[t.bond_dim for t in sGHZ.tensors]}")
# print(f"- Tensor shapes: {[t.shape for t in sGHZ.tensors]}")