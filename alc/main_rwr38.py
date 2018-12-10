import sys, struct
import numpy as np
from ctypes import *
from readwrite38 import *

###########################################
###########################################
###########################################
finame = "fort.38"
foname = "fort.39"

name_rec, nsym, nso, nmo, amo = read38( finame )

print( "B: %s, %4d" % ( name_rec, nsym ) )
print( "B: %s" % ( nso ) )
print( "B: %s" % ( nmo ) )
for isym in range( nsym ):
    for imo in range( nmo[ isym ] ):
        for iso in range( nso[ isym ] ):
            print( "B: %4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo ][ iso ] ) )

for imo in range( nmo[ 0 ] ):
    amo[ 0 ].flags.writeable = True
    for iso in range( nso[ 0 ] ):
        if ( imo >= 5 ):
            if ( imo == iso ):
                amo[ 0 ][ imo ][ iso ] = 1
            else:
                amo[ 0 ][ imo ][ iso ] = 0

write38( foname, amo )

name_rec, nsym, nso, nmo, amo = read38( foname )
print( "A: %s, %4d" % ( name_rec, nsym ) )
print( "A: %s" % ( nso ) )
print( "A: %s" % ( nmo ) )
for isym in range( nsym ):
    for imo in range( nmo[ isym ] ):
        for iso in range( nso[ isym ] ):
            print( "A: %4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo ][ iso ] ) )
