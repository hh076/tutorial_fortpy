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

zz        = np.empty( [ 100      ], dtype = np.float64 )
xyz       = np.empty( [ 3,   100 ], dtype = np.float64, order = 'F' )
amat      = np.empty( [ 200, 100 ], dtype = np.float64, order = 'F' )
#

def readrecord( ifs ):
    lenrec_s_bin  = ifs.read( 4 )
    lenrec_s      = (struct.unpack( 'i', lenrec_s_bin ))[0]
    data = ifs.read( lenrec_s )
    lenrec_e_bin  = ifs.read( 4 )
    lenrec_e      = (struct.unpack( 'i', lenrec_e_bin ))[0]
    #print( "read: %10d %10d" % ( lenrec_s, lenrec_e ) )
    return data

#################################
#################################
#################################
filename = "fort.99"

ifs   = open( filename, 'rb' )
data  = readrecord( ifs )
natom = struct.unpack_from( 'i', data, 0 )[ 0 ]
print( "%4d" % ( natom ) )

for i in range( natom ):
    data        = readrecord( ifs )
    iptr        = 0
    ij          = struct.unpack_from( 'i', data, iptr )[0]
    iptr        = iptr + 4
    zz[ i ]     = struct.unpack_from( 'd', data, iptr )[0]
    iptr        = iptr + 8
    xyz[ 0, i ] = struct.unpack_from( 'd', data, iptr )[0]
    iptr        = iptr + 8
    xyz[ 1, i ] = struct.unpack_from( 'd', data, iptr )[0]
    iptr        = iptr + 8
    xyz[ 2, i ] = struct.unpack_from( 'd', data, iptr )[0]
    print( "%4d: %6.2f %20.5e%20.5e%20.5e" % ( ij, zz[ i ], xyz[ 0, i ], xyz[ 1, i ], xyz[ 2, i ] ) )
    ij          = struct.unpack_from( 'i', data, 0 )[0]
    tpl         = struct.unpack_from( 'dddd', data, 4 )
    print( "%4d: %s" % ( ij, tpl ) )
    

data = readrecord( ifs )
print( data.__class__.__name__ )
itmps = struct.unpack_from( 'ii', data, 0 )
na   = itmps[ 0 ]
nb   = itmps[ 1 ]
print( "natom, na, nb: %4d%4d%4d" % ( natom, na, nb ) )

####################################
nab  = np.frombuffer( data, dtype = 'int32', count = 2, offset = 0 )
print( nab )
lmat = np.frombuffer( data, dtype = 'float64', count = 200 * 100, offset = 8 )
amat = np.reshape( lmat, [ 200, 100 ], order = 'F' )

lmat.flags.writeable = True
amat.flags.writeable = True
#lmat[ 200 * nb + na - 1 ] = 8.888888888e0
amat[ nb-1, na-1 ] = 8.888888888e0
lmat[ 0 ] = 2.0e0

lmat2 = np.frombuffer( data, dtype = 'float64', count = 200 * 100, offset = 8 )
iptr = 0
for i in range( na ):
    for j in range( nb ):
        print( "%10d%10d%10d%20.5e%20.5e%20.5e" % ( j+1, i+1, iptr, amat[ j, i ], lmat[ 200 * i + j ], lmat2[ 200 * i + j ] ) )
        iptr = iptr + 1

#for i in range( natom ):
#    print( "%4d: %6.2f %20.5e%20.5e%20.5e" % ( i, zz[ i ], xyz[ 0, i ], xyz[ 1, i ], xyz[ 2, i ] ) )
ifs.close
