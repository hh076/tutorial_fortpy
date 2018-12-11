import ctypes
from ctypes import *
import numpy as np
import sys, os

##########################################
T_PTR_VOID   = c_void_p
T_INT        = c_int32
T_DOUBLE     = c_double
T_PTR_INT    = POINTER( c_int32 )
T_PTR_DOUBLE = POINTER( c_double )

##########################################
def setlib( sofile ):
    lib = CDLL( sofile )
    return lib

def setfuncs( lib ):
    lib.int1_s_init_f_.restype   =   T_INT
    lib.int1_s_init_f_.argtypes  = [ T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_INT,    T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE,
                                     T_PTR_DOUBLE, T_PTR_INT ]
    lib.int1_t_init_f_.restype   =   T_INT
    lib.int1_t_init_f_.argtypes  = [ T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_INT,    T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE,
                                     T_PTR_DOUBLE, T_PTR_INT ]
    lib.int1_v_init_f_.restype   =   T_INT
    lib.int1_v_init_f_.argtypes  = [ T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_INT,    T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE,
                                     T_PTR_DOUBLE, T_PTR_INT ]
    lib.eri0_init_f_.restype     =   T_INT
    lib.eri0_init_f_.argtypes    = [ T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_INT,    T_PTR_INT,    T_PTR_INT,    T_PTR_INT,
                                     T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE, T_PTR_DOUBLE,
                                     T_PTR_DOUBLE, T_PTR_INT ]

    lib.int1_s_calc_f_.restype   =   T_INT
    lib.int1_s_calc_f_.argtypes  = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]
    lib.int1_t_calc_f_.restype   =   T_INT
    lib.int1_t_calc_f_.argtypes  = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]
    lib.int1_v_calc_f_.restype   =   T_INT
    lib.int1_v_calc_f_.argtypes  = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]

    lib.eri0_calc_f_.restype     =   T_INT
    lib.eri0_calc_f_.argtypes    = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]

    lib.int1_s_print_f_.restype  =   T_INT
    lib.int1_s_print_f_.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]
    lib.int1_t_print_f_.restype  =   T_INT
    lib.int1_t_print_f_.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]
    lib.int1_v_print_f_.restype  =   T_INT
    lib.int1_v_print_f_.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]

    lib.eri0_print_f_.restype    =   T_INT
    lib.eri0_print_f_.argtypes   = [ T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]
