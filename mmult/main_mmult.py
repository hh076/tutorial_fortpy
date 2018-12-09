import ctypes
from ctypes import *
from sys    import *
import numpy as np

##########################################
T_PTR_VOID   = ctypes.c_void_p
T_INT        = ctypes.c_int32
T_DOUBLE     = ctypes.c_double
T_PTR_INT    = ctypes.POINTER( ctypes.c_int32 )
T_PTR_DOUBLE = ctypes.POINTER( ctypes.c_double )

libmat2 = CDLL( "./libmmult.so" )
libmat2.mmult_.restype  = T_PTR_VOID
libmat2.mmult_.argtypes = [ T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE,
                            T_PTR_INT, T_PTR_INT, T_PTR_INT,
                            T_PTR_INT, T_PTR_INT, T_PTR_INT ]

##########################################
ka     = 15
kb     = 12
kc     = 14
l      = 3
m      = 5
n      = 4
A      = np.empty( [ ka, m ], dtype = np.float64, order = 'F' )
B      = np.empty( [ kb, n ], dtype = np.float64, order = 'F' )
C      = np.empty( [ kc, n ], dtype = np.float64, order = 'F' )
ptr_A  = A.ctypes.data_as( T_PTR_DOUBLE )
ptr_B  = B.ctypes.data_as( T_PTR_DOUBLE )
ptr_C  = C.ctypes.data_as( T_PTR_DOUBLE )

ptr_ka = byref( c_int32( ka ) )
ptr_kb = byref( c_int32( kb ) )
ptr_kc = byref( c_int32( kc ) )
ptr_l  = byref( c_int32( l  ) )
ptr_m  = byref( c_int32( m  ) )
ptr_n  = byref( c_int32( n  ) )

##########################################
for i in range( l ):
    for j in range( m ):
        A[ i, j ] = ( (i+1) * 4.3893e0    + (j+1) * 3.930933e0     ) * 0.1e0
for i in range( m ):
    for j in range( n ):
        B[ i, j ] = ( (i+1) * 3.3393839e0 + (j+1) * 1.8393930933e0 ) * 0.05e0

stdout.write( "py: A:\n" )
for i in range( l ):
    stdout.write( "%s%4d" % ( 'py:', i ) )
    for j in range( m ):
        stdout.write( "%20.5e" % ( A[ i, j ] ) )
    stdout.write( "\n" )
stdout.write( "py: B:\n" )
for i in range( m ):
    stdout.write( "%s%4d" % ( 'py:', i ) )
    for j in range( n ):
        stdout.write( "%20.5e" % ( B[ i, j ] ) )
    stdout.write( "\n" )

##########################################
libmat2.mmult_( ptr_A, ptr_B, ptr_C, ptr_ka, ptr_kb, ptr_kc, ptr_l, ptr_m, ptr_n )

##########################################
stdout.write( "py: C:\n" )
for i in range( l ):
    stdout.write( "%s%4d" % ( 'py:', i ) )
    for j in range( n ):
        stdout.write( "%20.5e" % ( C[ i, j ] ) )
    stdout.write( "\n" )
