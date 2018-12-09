#!/home/dahon/local/Python/bin/python
import ctypes
from ctypes import *
import numpy as np
import sys, os

##########################################
T_PTR_VOID   = ctypes.c_void_p
T_INT        = ctypes.c_int32
T_DOUBLE     = ctypes.c_double
T_PTR_INT    = ctypes.POINTER( ctypes.c_int32 )
T_PTR_DOUBLE = ctypes.POINTER( ctypes.c_double )

##########################################
import rhf_input
#from rhf_input import *

print rhf_input.numb_atom
print rhf_input.numb_shell
print rhf_input.numb_prim
print rhf_input.maxl
print
print rhf_input.shel_lqn
print rhf_input.shel_atm
print rhf_input.shel_tem
print rhf_input.shel_add
print rhf_input.shel_ini
print rhf_input.atom_zz
print rhf_input.atom_xyz
print rhf_input.prim_exp
print rhf_input.prim_coe
tol_eri = 1.0e+10
lvl_dbg = 4

##########################################
libmolint = CDLL( "molint/libmolint.so" )
libmolint

libmolint.int1_s_init_f_.restype  = T_INT
libmolint.int1_s_init_f_.argtypes = [ T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                      T_PTR_INT,    T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                      T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE,
                                      T_PTR_DOUBLE, T_PTR_INT ]

#np_numb_atom  = np.array( [ rhf_input.numb_atom  ], dtype = np.int32 )
#np_numb_shell = np.array( [ rhf_input.numb_shell ], dtype = np.int32 )
#np_numb_prim  = np.array( [ rhf_input.numb_prim  ], dtype = np.int32 )
#ptr_numb_atom  = np_numb_atom.ctypes.data_as( T_PTR_INT )
#ptr_numb_shell = np_numb_shell.ctypes.data_as( T_PTR_INT )
#ptr_numb_prim  = np_numb_prim.ctypes.data_as( T_PTR_INT )
#print np_numb_atom
#print np_numb_shell
#print np_numb_prim
ptr_numb_atom  = byref( c_int32( rhf_input.numb_atom  ) )
ptr_numb_shell = byref( c_int32( rhf_input.numb_shell ) )
ptr_numb_prim  = byref( c_int32( rhf_input.numb_prim  ) )

ptr_shel_lqn   = (rhf_input.shel_lqn).ctypes.data_as( T_PTR_INT )
ptr_shel_tem   = (rhf_input.shel_tem).ctypes.data_as( T_PTR_INT )
ptr_shel_atm   = (rhf_input.shel_atm).ctypes.data_as( T_PTR_INT )
ptr_shel_add   = (rhf_input.shel_add).ctypes.data_as( T_PTR_INT )
ptr_shel_ini   = (rhf_input.shel_ini).ctypes.data_as( T_PTR_INT )

ptr_atom_zz    = rhf_input.atom_zz.ctypes.data_as ( T_PTR_DOUBLE )
ptr_atom_xyz   = rhf_input.atom_xyz.ctypes.data_as( T_PTR_DOUBLE )
ptr_prim_exp   = rhf_input.prim_exp.ctypes.data_as( T_PTR_DOUBLE )
ptr_prim_coe   = rhf_input.prim_coe.ctypes.data_as( T_PTR_DOUBLE )

#ptr_tol        = np.array( [ tol_eri ], dtype = np.float64 ).ctypes.data_as( T_PTR_DOUBLE )
#ptr_lvl_dbg    = np.array( [ lvl_dbg ], dtype = np.int32   ).ctypes.data_as( T_PTR_INT )
ptr_tol        = byref( c_double( tol_eri ) )
ptr_lvl_dbg    = byref( c_int32(  lvl_dbg ) )

retval = libmolint.int1_s_init_f_(
        ptr_numb_atom,  ptr_numb_shell, ptr_numb_prim,
        ptr_shel_lqn,   ptr_shel_tem,   ptr_shel_atm,  ptr_shel_add,
        ptr_atom_zz,    ptr_atom_xyz,   ptr_prim_exp,  ptr_prim_coe,
        ptr_tol,        ptr_lvl_dbg )

#itype = c_int32()
#nsize = c_int32()
#ptr_itype = byref( itype )
#ptr_nsize = byref( nsize )
itype  = np.empty( [ 1 ], dtype = np.int32 )
nsize  = np.empty( [ 1 ], dtype = np.int32 )
ptr_itype  = itype.ctypes.data_as( T_PTR_INT )
ptr_nsize  = nsize.ctypes.data_as( T_PTR_INT )
dint = np.empty( [ 81 ], dtype = np.float64 )
ptr_dint  = dint.ctypes.data_as( T_PTR_DOUBLE )
for ish in range( rhf_input.numb_shell ):
    for jsh in range( ish+1 ):
        ptr_ish   = byref( c_int32( ish   ) )
        ptr_jsh   = byref( c_int32( jsh   ) )
        libmolint.int1_s_calc_f_(  ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )
#        libmolint.int1_s_print_f_( ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )
        li = rhf_input.shel_lqn[ ish ]
        lj = rhf_input.shel_lqn[ jsh ]
        print( "(%3d,%3d ) : (%2d,%2d ) : %4d%4d" % ( ish, jsh, li, lj, itype[ 0 ], nsize[ 0 ] ) )
        ncomp_i = ( ( li + 1 ) * ( li + 2 ) ) / 2 ;
        ncomp_j = ( ( lj + 1 ) * ( lj + 2 ) ) / 2 ;
        offset_i = 0 ;
        for i in range( ish ):
            offset_i += ( ( rhf_input.shel_lqn[ i ] + 1 ) * ( rhf_input.shel_lqn[ i ] + 2 ) ) / 2 ;
        offset_j = 0 ;
        for j in range( jsh ):
            offset_j += ( ( rhf_input.shel_lqn[ j ] + 1 ) * ( rhf_input.shel_lqn[ j ] + 2 ) ) / 2 ;

        iint = 0 ;
        for i in range( ncomp_i ):
            for j in range( ncomp_j ):
                print( "%5d%5d:%5d %24.16e" % ( offset_i + i, offset_j + j, iint, dint [ iint ] ) )
                iint = iint + 1
