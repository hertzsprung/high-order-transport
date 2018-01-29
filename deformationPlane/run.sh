#!/bin/bash
set -e

blockMesh
createGhostMesh 3
stitchMesh -perfect -overwrite -region ghostMesh inlet outlet2
stitchMesh -perfect -overwrite -region ghostMesh outlet inlet1
setGaussians setGaussiansDict
scalarDeformationWithGhosts explicit
