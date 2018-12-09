#! env python

from ctypes import *
import numpy as np
import sys, struct

##########################################
T_PTR_VOID   = c_void_p
T_CHAR       = c_char
T_INT        = c_int32
T_INT8       = c_int64
T_DOUBLE     = c_double
T_PTR_CHAR   = POINTER( c_char  )
T_PTR_INT    = POINTER( c_int32 )
T_PTR_INT8   = POINTER( c_int64 )
T_PTR_DOUBLE = POINTER( c_double )

#################################
#################################
#################################
def readrecord( ifs ):
    lenrec_s_bin  = ifs.read( 4 )
    lenrec_s      = (struct.unpack( 'i', lenrec_s_bin ))[0]
    print( "read: s: %10d" % ( lenrec_s ) )
    data = ifs.read( lenrec_s )
    lenrec_e_bin  = ifs.read( 4 )
    lenrec_e      = (struct.unpack( 'i', lenrec_e_bin ))[0]
    print( "read: e: %10d" % ( lenrec_e ) )
    return data

#################################
#################################
#################################
filename = "fort.38"
irecord = 1

ifs   = open( filename, 'rb' )
nso = np.empty( [ 20 ], dtype = np.int32 )
nmo = np.empty( [ 20 ], dtype = np.int32 )

###
### Skip Unnecessary Records
###
print( "here 0" )
for irec in range( 1, irecord ):
    data  = readrecord( ifs )
    name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
    nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
    nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
    nso  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4 )
    nmo  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4+4*20 )
    for i in range( nsym ):
        if ( nso[ i ]*nmo[ i ] == 0 ):
            continue
        data  = readrecord( ifs )
    nsym = 0

###
### Read Required Records
###
### Basic Data
data  = readrecord( ifs )
name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
nso  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4 )
nmo  = np.frombuffer( data, dtype = 'int32', count = 20, offset = 80+4+4+4*20 )
print( name_rec )
print( nn )
print( nsym )
print( nso )
print( nmo )

### MO Data: list[ 2D-Numpy Array ] format
amo = []
print( "here 2" )
for isym in range( nsym ):
    if ( nso[ isym ]*nmo[ isym ] == 0 ):
        continue
    amo_sym = np.empty( [ nso[ isym ], nmo[ isym ] ], dtype = 'float64', order = 'F' )
    data  = readrecord( ifs )
    iptr = 4
    buff = np.frombuffer( data, dtype = 'float64', count = nso[ isym ] * nmo[ isym ], offset = iptr )
    buff_2d = np.reshape( buff, [ nso[ isym ], nmo[ isym ] ], order = 'F' )
    b2t = buff_2d.transpose()
    amo.append( b2t )
    #for imo in range( nmo[ isym ] ):
    #    amo_sym[ imo ] = np.frombuffer( data, dtype = 'float64', count = nso[ isym ], offset = iptr + 8 * nso[ isym ] * imo )
    #amo.append( amo_sym )

print( "%s, %4d%4d" % ( name_rec, nn, nsym ) )
print( "%s" % ( nso ) )
print( "%s" % ( nmo ) )
for isym in range( nsym ):
    for imo in range( nmo[ isym ] ):
        for iso in range( nso[ isym ] ):
            print( "%4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo, iso ] ) )
