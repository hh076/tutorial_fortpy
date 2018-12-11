from ctypes import *
import numpy as np
import sys, struct
from readwrite38 import *

#################################
#################################
#################################
fname = "fort.38"
name_rec, nsym, nso, nmo, amo = read38( fname )

print( "%s, %4d" % ( name_rec, nsym ) )
print( "%s" % ( nso ) )
print( "%s" % ( nmo ) )
for isym in range( nsym ):
    for imo in range( nmo[ isym ] ):
        for iso in range( nso[ isym ] ):
            print( "%4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo, iso ] ) )

#fname = "fort.39"
#name_rec, nsym, nso, nmo, amo = read38( fname )
#
#print( "%s, %4d" % ( name_rec, nsym ) )
#print( "%s" % ( nso ) )
#print( "%s" % ( nmo ) )
#for isym in range( nsym ):
#    for imo in range( nmo[ isym ] ):
#        for iso in range( nso[ isym ] ):
#            print( "%4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo, iso ] ) )
