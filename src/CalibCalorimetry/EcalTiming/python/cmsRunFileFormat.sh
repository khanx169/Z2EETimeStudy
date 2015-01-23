#!/bin/bash

# This Small tool almost gave me the hwole day to know how to use it.

# It actually Puts the input root files in the way accepted  by CMS Modules:

# Author TEN

 sed -e s/"\/pnfs"/"'dcache:\/pnfs"/  -e  s/"root"/"root',"/  < doubleEleRun2012C_22Jan.txt > DoubleEleRun2012C_22Jan.txt&
# sed -e s/"\/pnfs/"/"'dcache:\/pnfs/"/  -e  s/"root"/"root',"/  < singleEleR12C.txt >SingleEleRun2012C.txt&
