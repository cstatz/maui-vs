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

# Create a vector field g from the mesh
sm = ScalarField(mesh, "g", "nounit")
sm[50:60, 20:, :] = 3.
sm.sync()

# Create the output
io = VSOutput([sm], "test_io_3d_2")

# Write the output
io.write()
io.write(cycle=10, time=0.66)
