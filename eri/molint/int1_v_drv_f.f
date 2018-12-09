      subroutine int1_v_init_f (
     &                  numb_atom, numb_shell, numb_prim,
     &                  shel_lqn,  shel_tem,   shel_atm,   shel_add,
     &                  atom_zz,   atom_xyz,
     &                  prim_exp,  prim_coe,
     &                  tol,       level_dbg_print )
      implicit none
      integer  numb_atom,    numb_shell,   numb_prim
      integer  shel_lqn(*),  shel_tem(*),  shel_atm(*),  shel_add(*)
      real*8   atom_zz(*),   atom_xyz(*),  prim_exp(*),  prim_coe(*)
      real*8   tol
      integer  level_dbg_print
      call int1_v_init( numb_atom, numb_shell, numb_prim,
     &                  shel_lqn,  shel_tem,   shel_atm,  shel_add,
     &                  atom_zz,   atom_xyz,
     &                  prim_exp,  prim_coe,
     &                  tol,       level_dbg_print )
      end

      subroutine int1_v_calc_f (
     &                  Ish, Jsh, inttype, nsize_int, DINT_cont )
      implicit none
      integer Ish, Jsh, inttype, nsize_int
      real*8 DINT_cont(*)
      call int1_v_calc ( Ish, Jsh, inttype, nsize_int, DINT_cont )
      end

      subroutine int1_v_print_f (
     &                  Ash, Bsh, inttype, nsize_int, Dint_cont )
      implicit none
      integer Ash, Bsh, inttype, nsize_int
      real*8 Dint_cont(*)
      call int1_v_print ( Ash, Bsh, inttype, nsize_int, Dint_cont )
      end
