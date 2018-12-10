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

libreadfort = CDLL( "./libreadfort.so" )
libreadfort.read_fort_.restype  = T_PTR_VOID
libreadfort.read_fort_.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE, T_PTR_DOUBLE,
                                    T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]

##########################################
iunit     = 88
iunit     = 99
iunit32   = c_int32( iunit )
natom32   = c_int32()
na32      = c_int32()
nb32      = c_int32()
zz        = np.empty( [ 100      ], dtype = np.float64 )
xyz       = np.empty( [ 3,   100 ], dtype = np.float64, order = 'F' )
amat      = np.empty( [ 200, 100 ], dtype = np.float64, order = 'F' )

ptr_iunit = byref( c_int32( iunit ) )
ptr_natom = byref( natom32 )
ptr_na    = byref( na32 )
ptr_nb    = byref( nb32 )
ptr_zz    = zz.ctypes.data_as( T_PTR_DOUBLE )
ptr_xyz   = xyz.ctypes.data_as( T_PTR_DOUBLE )
ptr_amat  = amat.ctypes.data_as( T_PTR_DOUBLE )

##########################################
libreadfort.read_fort_( ptr_iunit, ptr_natom, ptr_zz, ptr_xyz,
                        ptr_na,    ptr_nb,    ptr_amat )
natom = natom32.value
na    = na32.value
nb    = nb32.value

print( "natom, na, nb: %4d%4d%4d" % ( natom, na, nb ) )
for i in range( natom ):
    print( "%4d: %6.2f %20.5e%20.5e%20.5e" % ( i, zz[ i ], xyz[ 0, i ], xyz[ 1, i ], xyz[ 2, i ] ) )

for i in range( na ):
    for j in range( nb ):
        print( "%5d%5d%20.5e" % ( j+1, i+1, amat[ j, i ] ) )
