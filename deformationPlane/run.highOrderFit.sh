#!/bin/bash
set -e

rm -rf constant
rm -rf 1 2 3 4 5
rm -f 0/U 0/Uf 0/T 0/ghostMesh/TGhost

cp system/controlDict.highOrderFit system/controlDict
cp system/ghostMesh/fvSchemes.highOrderFit system/ghostMesh/fvSchemes
blockMesh
mkdir -p 0
cp init_0/phi 0/
cp init_0/ghostMesh/TGhost 0/ghostMesh/
createGhostMesh 3
stitchMesh -perfect -overwrite -region ghostMesh inlet outlet2
stitchMesh -perfect -overwrite -region ghostMesh outlet inlet1
setGaussians setGaussiansDict
scalarDeformationHighOrderFit
