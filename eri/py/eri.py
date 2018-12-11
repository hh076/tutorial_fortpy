import ctypes
from ctypes import *
import numpy as np
import sys, os

##########################################
from rhf_input import *
from wrapper   import *

#print numb_atom
#print numb_shell
#print numb_prim
#print maxl
#print
#print shel_lqn
#print shel_atm
#print shel_tem
#print shel_add
#print shel_ini
#print atom_zz
#print atom_xyz
#print prim_exp
#print prim_coe
#tol_eri = 1.0e+10
#lvl_dbg = 4

##########################################
lib = setlib( "../molint/libmolint.so" )
setfuncs( lib )

#np_numb_atom  = np.array( [ numb_atom  ], dtype = np.int32 )
#np_numb_shell = np.array( [ numb_shell ], dtype = np.int32 )
#np_numb_prim  = np.array( [ numb_prim  ], dtype = np.int32 )
#ptr_numb_atom  = np_numb_atom.ctypes.data_as( T_PTR_INT )
#ptr_numb_shell = np_numb_shell.ctypes.data_as( T_PTR_INT )
#ptr_numb_prim  = np_numb_prim.ctypes.data_as( T_PTR_INT )
#print np_numb_atom
#print np_numb_shell
#print np_numb_prim
ptr_numb_atom  = byref( c_int32( numb_atom  ) )
ptr_numb_shell = byref( c_int32( numb_shell ) )
ptr_numb_prim  = byref( c_int32( numb_prim  ) )

ptr_shel_lqn   = (shel_lqn).ctypes.data_as( T_PTR_INT )
ptr_shel_tem   = (shel_tem).ctypes.data_as( T_PTR_INT )
ptr_shel_atm   = (shel_atm).ctypes.data_as( T_PTR_INT )
ptr_shel_add   = (shel_add).ctypes.data_as( T_PTR_INT )
ptr_shel_ini   = (shel_ini).ctypes.data_as( T_PTR_INT )

ptr_atom_zz    = atom_zz.ctypes.data_as ( T_PTR_DOUBLE )
ptr_atom_xyz   = atom_xyz.ctypes.data_as( T_PTR_DOUBLE )
ptr_prim_exp   = prim_exp.ctypes.data_as( T_PTR_DOUBLE )
ptr_prim_coe   = prim_coe.ctypes.data_as( T_PTR_DOUBLE )

#ptr_tol        = np.array( [ tol_eri ], dtype = np.float64 ).ctypes.data_as( T_PTR_DOUBLE )
#ptr_lvl_dbg    = np.array( [ lvl_dbg ], dtype = np.int32   ).ctypes.data_as( T_PTR_INT )
ptr_tol        = byref( c_double( tol_eri ) )
ptr_lvl_dbg    = byref( c_int32(  lvl_dbg ) )

retval = lib.int1_s_init_f_(
        ptr_numb_atom,  ptr_numb_shell, ptr_numb_prim,
        ptr_shel_lqn,   ptr_shel_tem,   ptr_shel_atm,  ptr_shel_add,
        ptr_atom_zz,    ptr_atom_xyz,   ptr_prim_exp,  ptr_prim_coe,
        ptr_tol,        ptr_lvl_dbg )
retval = lib.int1_t_init_f_(
        ptr_numb_atom,  ptr_numb_shell, ptr_numb_prim,
        ptr_shel_lqn,   ptr_shel_tem,   ptr_shel_atm,  ptr_shel_add,
        ptr_atom_zz,    ptr_atom_xyz,   ptr_prim_exp,  ptr_prim_coe,
        ptr_tol,        ptr_lvl_dbg )
retval = lib.int1_v_init_f_(
        ptr_numb_atom,  ptr_numb_shell, ptr_numb_prim,
        ptr_shel_lqn,   ptr_shel_tem,   ptr_shel_atm,  ptr_shel_add,
        ptr_atom_zz,    ptr_atom_xyz,   ptr_prim_exp,  ptr_prim_coe,
        ptr_tol,        ptr_lvl_dbg )

#sys.exit()

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
sys.stdout.write( "s:\n" )
for ish in range( numb_shell ):
    for jsh in range( ish+1 ):
        ptr_ish   = byref( c_int32( ish   ) )
        ptr_jsh   = byref( c_int32( jsh   ) )
        lib.int1_s_calc_f_(  ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )
        lib.int1_s_print_f_( ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )

sys.stdout.write( "t:\n" )
for ish in range( numb_shell ):
    for jsh in range( ish+1 ):
        ptr_ish   = byref( c_int32( ish   ) )
        ptr_jsh   = byref( c_int32( jsh   ) )
        lib.int1_s_calc_f_(  ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )
        lib.int1_s_print_f_( ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )

sys.stdout.write( "v:\n" )
for ish in range( numb_shell ):
    for jsh in range( ish+1 ):
        ptr_ish   = byref( c_int32( ish   ) )
        ptr_jsh   = byref( c_int32( jsh   ) )
        lib.int1_s_calc_f_(  ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )
        lib.int1_s_print_f_( ptr_ish, ptr_jsh, ptr_itype, ptr_nsize, ptr_dint )
#        li = shel_lqn[ ish ]
#        lj = shel_lqn[ jsh ]
#        print( "(%3d,%3d ) : (%2d,%2d ) : %4d%4d" % ( ish, jsh, li, lj, itype[ 0 ], nsize[ 0 ] ) )
#        ncomp_i = ( ( li + 1 ) * ( li + 2 ) ) / 2 ;
#        ncomp_j = ( ( lj + 1 ) * ( lj + 2 ) ) / 2 ;
#        offset_i = 0 ;
#        for i in range( ish ):
#            offset_i += ( ( shel_lqn[ i ] + 1 ) * ( shel_lqn[ i ] + 2 ) ) / 2 ;
#        offset_j = 0 ;
#        for j in range( jsh ):
#            offset_j += ( ( shel_lqn[ j ] + 1 ) * ( shel_lqn[ j ] + 2 ) ) / 2 ;
#
#        iint = 0 ;
#        for i in range( ncomp_i ):
#            for j in range( ncomp_j ):
#                print( "%5d%5d:%5d %24.16e" % ( offset_i + i, offset_j + j, iint, dint [ iint ] ) )
#                iint = iint + 1
