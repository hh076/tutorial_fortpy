#! env python

from ctypes import *
import numpy as np
import sys, struct

#################################
#################################
#################################
natom     = np.empty( [ 1        ], dtype = np.int32 )
zz        = np.empty( [ 100      ], dtype = np.float64 )
xyz       = np.empty( [ 3,   100 ], dtype = np.float64, order = 'F' )
amat      = np.empty( [ 200, 100 ], dtype = np.float64, order = 'F' )

natom[ 0 ] = 3
na         = 50
nb         = 20

zz[ 0 ] = 8.0e0
zz[ 1 ] = 1.0e0
zz[ 2 ] = 3.0e0

xyz[ 0, 0 ] =  1.84626229e0
xyz[ 1, 0 ] = -0.72376505e0
xyz[ 2, 0 ] =  2.58892457e0
xyz[ 0, 1 ] =  0.95053217e0
xyz[ 1, 1 ] = -1.04501847e0
xyz[ 2, 1 ] =  1.05068765e0
xyz[ 0, 2 ] =  3.56969239e0
xyz[ 1, 2 ] = -0.51589519e0
xyz[ 2, 2 ] =  2.07491913e0

for i in range( na ):
    for j in range( nb ):
        amat[ j, i ] = 5.39e0 + 0.7983e0 * ( (i+1) * (j+1) + 1 )

#################################
#################################
#################################
def write_record( ofs, data, nbyte ):
    ofs.write( struct.pack( 'i', nbyte) )
    ofs.write( data )
    ofs.write( struct.pack( 'i', nbyte) )

#################################
#################################
#################################
fname = "fort.88"

ofs = open( fname, "wb" )

write_record( ofs, natom.tobytes(), 4 )

for i in range( natom[ 0 ] ):
    bytebuf = bytes()
    bytebuf += struct.pack( 'i', i )
    data = struct.pack( 'dddd', zz[ i ], xyz[ 0, i ] , xyz[ 1, i ], xyz[ 2, i ] )
    bytebuf += data
    write_record( ofs, bytebuf, 4+8*4 )

bytebuf = bytes()
bytebuf += struct.pack( 'ii', na, nb)
bytebuf += (amat.transpose()).tobytes()
write_record( ofs, bytebuf, 4*2+200*100*8 )

ofs.close()
#################################
#################################
#################################
for i in range( na ):
    for j in range( nb ):
        amat[ j, i ] = 5.39e0 + 0.7983e0 * ( (i+1) * (j+1) + 1 )

iptr = 0
for i in range( na ):
    for j in range( nb ):
        print( "%10d%10d%10d%20.5e" % ( j, i, iptr, amat[ j, i ] ) )
        iptr = iptr + 1
