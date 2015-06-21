# -*- coding: utf-8 -*-

from __future__ import division

__author__ = 'christoph.statz <at> tu-dresden.de'

from maui.mesh import CartesianMesh
from maui.field import ScalarField
from mauivs import VSOutput


# Create a 3d cartesian mesh
mesh_bounds = ((-50., -50., -50.), (50., 50., 50.))
discretization = 0.5
mesh = CartesianMesh(mesh_bounds, discretization)

fields = list()
for i in range(10):
    field = ScalarField(mesh, "f%d" % i, "nounit")
    field[10:-10, 20:-50, :] = i/10.
    field.sync()

# Create the output
io = VSOutput(fields, "test_io_3d_2")

# Write the output
for i in range(100):
    io.write(cycle=i, time=i*0.1)
