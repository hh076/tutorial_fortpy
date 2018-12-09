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
class FORT8:
    def readfort( self, fname_fort8 ):
        ifs   = open( fname_fort8, 'rb' )
        ###
        ### BASIC
        ###
        data  = readrecord( ifs )
        self.title  = ''.join(struct.unpack_from( '192c', data, 0 ))
        self.maxlop = struct.unpack_from( 'i', data, 192 )[ 0 ]
        self.nxbas  = struct.unpack_from( 'i', data, 192+4 )[ 0 ]
        self.potnuc = struct.unpack_from( 'd', data, 192+4+4 )[ 0 ]
        self.idosph = struct.unpack_from( 'i', data, 192+4+4+8 )[ 0 ]
        
        print( "BASIC DATA:" )
        print( "%s"      % ( self.title ) )
        print( "%4d"     % ( self.maxlop ) )
        print( "%4d"     % ( self.nxbas ) )
        print( "%20.16e" % ( self.potnuc ) )
        print( "%4d"     % ( self.idosph ) )
        
        ###
        ### ATOMS
        ###
        data  = readrecord( ifs )
        data  = readrecord( ifs )
        self.nnuc = struct.unpack_from( 'i', data, 0 )[ 0 ]
        self.nuc_name = []
        self.nuc_tid  = []
        self.nuc_xyz  = []
        self.nuc_z    = []
        for i in range( self.nnuc ):
            if ( i >= self.nnuc ):
                break
            data  = readrecord( ifs )
            self.nuc_name.append( ''.join(struct.unpack_from( '4c', data, 0 )) )
            self.nuc_tid.append( struct.unpack_from( 'i', data, 4 )[ 0 ] )
            xyz = []
            xyz.append(   struct.unpack_from( 'd', data, 8+0   )[ 0 ] )
            xyz.append(   struct.unpack_from( 'd', data, 8+8*1 )[ 0 ] )
            xyz.append(   struct.unpack_from( 'd', data, 8+8*2 )[ 0 ] )
            self.nuc_xyz.append( xyz )
            self.nuc_z.append( struct.unpack_from( 'd', data, 8+8*3 )[ 0 ] )
        
        print( "ATOMS:" )
        print( "%4d" % ( self.nnuc ) )
        for i in range( self.nnuc ):
            print( "%s: %4d: %20.8e: %20.8e%20.8e%20.8e" % (
                self.nuc_name[ i ], self.nuc_tid[ i ], self.nuc_z[ i ], self.nuc_xyz[ i ][ 0 ], self.nuc_xyz[ i ][ 1 ], self.nuc_xyz[ i ][ 2 ] ) )
        
        ###
        ### BASIS FUNCTIONS
        ###
        data = readrecord( ifs )
        npri_nbas = struct.unpack_from( 'ii', data, 0 )
        self.npri = npri_nbas[ 0 ]
        self.nbas = npri_nbas[ 1 ]
        print( "%4d%4d" % ( self.npri, self.nbas ) )
        
        self.icds = []
        data = readrecord( ifs )
        for i in range( self.nbas ):
            self.icds.append( struct.unpack_from( 'i', data, 4*i )[ 0 ] )
        print( "%s" % ( self.icds ) )
        
        self.bas_lam = []
        self.bas_kb = []
        self.bas_nako = []
        self.bas_exp = []
        self.bas_coe = []
        for i in range( self.npri ):
            data = readrecord( ifs )
            self.bas_lam.append(  ''.join(struct.unpack_from( '4c', data, 0         )) )
            self.bas_kb.append(           struct.unpack_from( 'i',  data, 0+4       )[ 0 ] )
            self.bas_nako.append( ''.join(struct.unpack_from( '4c', data, 0+4+4     )) )
            self.bas_exp.append(          struct.unpack_from( 'd',  data, 0+4+4+4   )[ 0 ] )
            self.bas_coe.append(          struct.unpack_from( 'd',  data, 0+4+4+4+8 )[ 0 ] )
            
        print( "BASIS FUNCTIONS:" )
        print( "%4d%4d" % ( self.npri, self.nbas ) )
        print( "%s" % ( self.icds ) )
        for i in range( self.npri ):
            print( "%s, %4d, %s, %20.8e%20.8e" % ( self.bas_lam[ i ], self.bas_kb[ i ], self.bas_nako[ i ], self.bas_exp[ i ], self.bas_coe[ i ] ) )
        
        
        ###
        ### SYMINP: NOT USED
        ###
        data = readrecord( ifs )
        self.syminp = []
        self.syminp.append( ''.join( struct.unpack_from( '8c', data,  0 ) ) )
        self.syminp.append( ''.join( struct.unpack_from( '8c', data,  8 ) ) )
        self.syminp.append( ''.join( struct.unpack_from( '8c', data, 16 ) ) )
        self.syminp.append( ''.join( struct.unpack_from( '8c', data, 24 ) ) )
        
        ###
        ### SO COEFFICIENTS
        ###
        data = readrecord( ifs )
        self.nso = struct.unpack_from( 'i', data, 0 )[ 0 ]
        print( "%4d" % ( self.nso ) )
        
        self.so_itran = []
        self.so_jtran = []
        self.so_ctran = []
        for i in range( self.nso ):
            data = readrecord( ifs )
            nao  = struct.unpack_from( 'i', data, 0 )[ 0 ]
            print( "%4d%4d" % ( self.nso, nao ) )
            l_itran = []
            l_ctran = []
            for j in range( nao ):
                l_itran.append( struct.unpack_from( 'i', data, 4  +8*j )[ 0 ] )
                l_ctran.append( struct.unpack_from( 'd', data, 4+4+8*j )[ 0 ] )
            self.so_itran.append( l_itran )
            self.so_ctran.append( l_ctran )
            self.so_jtran.append( nao )
        
        print( "SYMMETRY ORBITALS:" )
        print( "%4d" % ( self.nso ) )
        print( "%s, %s, %s, %s" % ( self.syminp[ 0 ], self.syminp[ 1 ], self.syminp[ 2 ], self.syminp[ 3 ] ) )
        for i in range( self.nso ):
            print( "%4d%4d" % ( i, self.so_jtran[ i ] ) )
            for j in range( self.so_jtran[ i ] ):
                print( "%4d%4d:%4d%20.8e" % ( i+1, j+1, self.so_itran[ i ][ j ], self.so_ctran[ i ][ j ] ) )

        ###
        ### Overlap Matrix
        ###
        ifs.close

#################################
#################################
#################################
read8 = FORT8()
read8.readfort( 'fort.8' )
