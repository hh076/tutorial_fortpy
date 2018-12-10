import numpy as np
import sys, struct
from ctypes import *
from readwrite38 import *

###########################################
###########################################
###########################################
filename = "fort.38"
irecord = 1

ifs   = open( filename, 'rb' )
###
### Skip Records
###
for irec in range( 1, irecord ):
    data  = read_record( ifs )
    name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
    nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
    nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
    nso = []
    nmo = []
    for i in range( 20 ):
        nso.append( struct.unpack_from( 'i', data, 80+4+4     +4*i )[ 0 ] )
    for i in range( 20 ):
        nmo.append( struct.unpack_from( 'i', data, 80+4+4+4*20+4*i )[ 0 ] )
    for i in range( nsym ):
        if ( nso[ i ]*nmo[ i ] == 0 ):
            continue
        data  = read_record( ifs )
    nsym = 0

data  = read_record( ifs )
name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
nso = []
nmo = []
for i in range( 20 ):
    nso.append( struct.unpack_from( 'i', data, 80+4+4     +4*i )[ 0 ] )
for i in range( 20 ):
    nmo.append( struct.unpack_from( 'i', data, 80+4+4+4*20+4*i )[ 0 ] )
amo = []
for isym in range( nsym ):
    if ( nso[ isym ]*nmo[ isym ] == 0 ):
        continue
    data  = read_record( ifs )
    idummy = struct.unpack_from( 'i', data, 0 )[ 0 ]
    iptr = 4
    lamo_sym = []
    for imo in range( nmo[ isym ] ):
        lamo = []
        for iso in range( nso[ isym ] ):
            lamo.append( struct.unpack_from( 'd', data, iptr )[ 0 ] )
            iptr = iptr + 8
        lamo_sym.append( lamo )
    amo.append( lamo_sym )

###########################################
###########################################
###########################################
print( "%s, %4d%4d" % ( name_rec, nn, nsym ) )
print( "%s" % ( nso ) )
print( "%s" % ( nmo ) )
for isym in range( nsym ):
    for imo in range( nmo[ isym ] ):
        for iso in range( nso[ isym ] ):
            print( "%4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo ][ iso ] ) )
