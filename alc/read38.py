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

#libreadfort = CDLL( "libreadfort.so" )
#libreadfort.read_fort_.restype  = T_PTR_VOID
#libreadfort.read_fort_.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE, T_PTR_DOUBLE,
#                                    T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]
#
###########################################
#iunit     = 8
#iunit32   = c_int32( iunit )
maxlop     = c_int32()
maxlop     = c_int32()
#natom32   = c_int32()
#na32      = c_int32()
#nb32      = c_int32()
zz        = np.empty( [ 100      ], dtype = np.float64 )
xyz       = np.empty( [ 3,   100 ], dtype = np.float64, order = 'F' )
amat      = np.empty( [ 200, 100 ], dtype = np.float64, order = 'F' )
#
#ptr_iunit = byref( c_int32( iunit ) )
#ptr_natom = byref( natom32 )
#ptr_na    = byref( na32 )
#ptr_nb    = byref( nb32 )
#ptr_zz    = zz.ctypes.data_as( T_PTR_DOUBLE )
#ptr_xyz   = xyz.ctypes.data_as( T_PTR_DOUBLE )
ptr_amat  = amat.ctypes.data_as( T_PTR_DOUBLE )

#
###########################################
#libreadfort.read_fort_( ptr_iunit, ptr_natom, ptr_zz, ptr_xyz,
#                        ptr_na,    ptr_nb,    ptr_amat )
#natom = natom32.value
#na    = na32.value
#nb    = nb32.value
#
#print( "natom, na, nb: %4d%4d%4d" % ( natom, na, nb ) )
#for i in range( natom ):
#    print( "%4d: %6.2f %20.5e%20.5e%20.5e" % ( i, zz[ i ], xyz[ 0, i ], xyz[ 1, i ], xyz[ 2, i ] ) )
#
#for i in range( na ):
#    for j in range( nb ):
#        print( "%5d%5d%20.5e" % ( j+1, i+1, amat[ j, i ] ) )
#    
##########################################

def readrecord2( ifs, fmt, offset ):
    lenrec_s_bin  = ifs.read( 4 )
    lenrec_s      = (struct.unpack( 'i', lenrec_s_bin ))[0]
    data = ifs.read( lenrec_s )
    lenrec_e_bin  = ifs.read( 4 )
    lenrec_e      = (struct.unpack( 'i', lenrec_e_bin ))[0]
    print( "read: %4d%4d" % ( lenrec_s, lenrec_e ) )
    unpacked_data = struct.unpack_from( fmt, data, offset )
    print( unpacked_data )
    return unpacked_data

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
###
### Skip Records
###
print( "here 0" )
for irec in range( 1, irecord ):
    data  = readrecord( ifs )
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
        data  = readrecord( ifs )
    nsym = 0

#print( "here 0" )
data  = readrecord( ifs )
name_rec = ''.join(struct.unpack_from( '80c', data, 0 ))
nn   = struct.unpack_from( 'i', data, 80   )[ 0 ]
nsym = struct.unpack_from( 'i', data, 80+4 )[ 0 ]
nso = []
nmo = []
#print( "%s, %4d%4d" % ( name_rec, nn, nsym ) )
#print( "%s" % ( nso ) )
#print( "%s" % ( nmo ) )
#print( "here 1" )
for i in range( 20 ):
    nso.append( struct.unpack_from( 'i', data, 80+4+4     +4*i )[ 0 ] )
for i in range( 20 ):
    nmo.append( struct.unpack_from( 'i', data, 80+4+4+4*20+4*i )[ 0 ] )
amo = []
print( "here 2" )
for isym in range( nsym ):
    if ( nso[ isym ]*nmo[ isym ] == 0 ):
        continue
    data  = readrecord( ifs )
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

print( "%s, %4d%4d" % ( name_rec, nn, nsym ) )
print( "%s" % ( nso ) )
print( "%s" % ( nmo ) )
for isym in range( nsym ):
    for imo in range( nmo[ isym ] ):
        for iso in range( nso[ isym ] ):
            print( "%4d%4d%4d: %26.16e" % ( isym+1, imo+1, iso+1, amo[ isym ][ imo ][ iso ] ) )
