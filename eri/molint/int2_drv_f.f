      subroutine eri0_init_f (
     &                     numb_atom, numb_shell, numb_prim,
     &                     shel_lqn, shel_tem, shel_atm, shel_add,
     &                     atom_zz,  atom_xyz, prim_exp, prim_coe,
     &                     tol, level_dbg_print )
      implicit none
      integer numb_atom, numb_shell, numb_prim
      integer shel_lqn(*), shel_tem(*), shel_atm(*), shel_add(*)
      real*8  atom_zz(*),  atom_xyz(*)
      real*8  prim_exp(*), prim_coe(*)
      real*8  tol, level_dbg_print
      call eri0_init( numb_atom, numb_shell, numb_prim,
     &                 shel_lqn,  shel_tem,   shel_atm,  shel_add,
     &                 atom_zz,   atom_xyz,   prim_exp,  prim_coe,
     &                 tol,       level_dbg_print )
      end

      subroutine eri0_calc_f (
     &           Ish, Jsh, Ksh, Lsh, inttype, nsize_eris, eris )
      implicit none
      integer Ish, Jsh, Ksh, Lsh, inttype, nsize_eris
      real*8 eris(*)
      call eri0_calc ( Ish, Jsh, Ksh, Lsh, inttype, nsize_eris, eris )
      end

      subroutine eri0_print_f (
     &           Ish, Jsh, Ksh, Lsh, inttype, nsize_eris, eris )
      integer Ish, Jsh, Ksh, Lsh, inttype, nsize_eris
      real*8 eris(*)
      call eri0_print (
     &           Ish, Jsh, Ksh, Lsh, inttype, nsize_eris, eris )
      end
