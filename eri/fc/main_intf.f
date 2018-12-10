      block data
      implicit none
      integer NSH, NPR, NAT, ML
      parameter(NSH=13, NPR=28, NAT=3, ML=1)
      integer numb_shell, numb_prim, numb_atom, maxl
      integer shel_lqn(NSH), shel_atm(NSH), shel_tem(NSH)
      integer shel_add(NSH), shel_ini(NSH)
      real*8  atom_zz(NAT),  atom_xyz(NAT*3),
     &        prim_exp(NPR), prim_coe(NPR)
      common /iinputs/numb_shell, numb_prim, numb_atom, maxl,
     &               shel_lqn, shel_atm, shel_tem,
     &               shel_add, shel_ini
      common /dinputs/atom_zz, atom_xyz, prim_exp, prim_coe
      data numb_shell, numb_prim, numb_atom, maxl/
     &     NSH, NPR, NAT, ML/
      data shel_lqn/0, 0, 0, 0, 1, 1, 1, 0, 0, 1,  0, 0, 1/
      data shel_atm/0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  2, 2, 2/
      data shel_tem/5, 2, 1, 1, 1, 3, 1, 3, 1, 3,  3, 1, 3/
      data shel_add/0, 5, 7, 8, 9,10,13,14,17,18, 21,24,25/
      data shel_ini/0, 1, 2, 3, 4, 7,10,13,14,15, 18,19,20/
      data atom_zz/8.0D0, 1.0D0, 1.0D0/
      data atom_xyz/
     &     1.84626229D0, -0.72376505D0,  2.58892457D0,
     &     0.95053217D0, -1.04501847D0,  1.05068765D0,
     &     3.56969239D0, -0.51589519D0,  2.07491913D0/
      data prim_exp/
     &     5.0657590099999998D+03, 7.6080541299999993D+02,
     &     1.7306691900000001D+02, 4.8688319000000007D+01,
     &     1.5572176000000001D+01, 1.0158026999999999D+01,
     &     9.3726299999999996D-01, 5.2547980000000001D+00,
     &     2.8650600000000004D-01, 2.2210805000000004D+01,
     &     1.7691086000000002D+01, 3.8521809999999999D+00,
     &     1.0449199999999998D+00, 2.7504099999999998D-01,
     &     1.3010700269999999D+01, 1.9622570800000001D+00,
     &     4.4453797000000000D-01, 1.2194961999999999D-01,
     &     2.8606729999999998D+00, 8.8819000000000004D-01,
     &     3.0377599999999999D-01, 1.3010700269999999D+01,
     &     1.9622570800000001D+00, 4.4453797000000000D-01,
     &     1.2194961999999999D-01, 2.8606729999999998D+00,
     &     8.8819000000000004D-01, 3.0377599999999999D-01/
      data prim_coe/
     &     1.1520426087473887D+00, 2.1219762063841294D+00,
     &     3.4146270844410713D+00, 4.4040672419995586D+00,
     &     3.6112031237508075D+00,-6.2708283493057582D-01,
     &     7.1569294634675040D-01, 2.4735865551015990D+00,
     &     2.7910035138546846D-01, 6.8729860422543865D+01,
     &     3.2410517821686669D+00, 2.5663992531302311D+00,
     &     1.1162275504579231D+00, 2.8391405061454988D-01,
     &     1.6349038957298870D-01, 2.7735153639996912D-01,
     &     3.1575014844115706D-01, 1.4707722621719763D-01,
     &     6.8332898898525340D-01, 7.6170728997588932D-01,
     &     1.1994223393465964D-01, 1.6349038957298870D-01,
     &     2.7735153639996912D-01, 3.1575014844115706D-01,
     &     1.4707722621719763D-01, 6.8332898898525340D-01,
     &     7.6170728997588932D-01, 1.1994223393465964D-01/
      end

      program main
      implicit none
      integer NSH, NPR, NAT, ML
      parameter(NSH=13, NPR=28, NAT=3, ML=1)
      integer numb_shell, numb_prim, numb_atom, maxl
      integer shel_lqn(NSH), shel_atm(NSH), shel_tem(NSH)
      integer shel_add(NSH), shel_ini(NSH)
      real*8  atom_zz(NAT),  atom_xyz(NAT*3),
     &        prim_exp(NPR), prim_coe(NPR)
      common /iinputs/numb_shell, numb_prim, numb_atom, maxl,
     &                 shel_lqn, shel_atm, shel_tem,
     &                 shel_add, shel_ini
      common /dinputs/atom_zz, atom_xyz, prim_exp, prim_coe
      integer is, js, inttype, nsize_int, level_print
      real*8 tol, DINT_cont(81)

      level_print = 4
      tol = 1.0d10

      call int1_s_init_f ( numb_atom, numb_shell, numb_prim,
     &                  shel_lqn,  shel_tem,   shel_atm,   shel_add,
     &                  atom_zz,   atom_xyz,
     &                  prim_exp,  prim_coe,
     &                  tol,       level_print )
      call int1_t_init_f ( numb_atom, numb_shell, numb_prim,
     &                  shel_lqn,  shel_tem,   shel_atm,   shel_add,
     &                  atom_zz,   atom_xyz,
     &                  prim_exp,  prim_coe,
     &                  tol,       level_print )
      call int1_v_init_f ( numb_atom, numb_shell, numb_prim,
     &                  shel_lqn,  shel_tem,   shel_atm,   shel_add,
     &                  atom_zz,   atom_xyz,
     &                  prim_exp,  prim_coe,
     &                  tol,       level_print )
!
      write(*,*) 's:'
      do is = 0, numb_shell-1
         do js = 0, is
            call int1_s_calc_f ( is, js, inttype, nsize_int, DINT_cont )
            call int1_s_print_f( is, js, inttype, nsize_int, DINT_cont )
         end do
      end do
      write(*,*) 't:'
      do is = 0, numb_shell-1
         do js = 0, is
            call int1_t_calc_f ( is, js, inttype, nsize_int, DINT_cont )
            call int1_t_print_f( is, js, inttype, nsize_int, DINT_cont )
         end do
      end do
      write(*,*) 'v:'
      do is = 0, numb_shell-1
         do js = 0, is
            call int1_v_calc_f ( is, js, inttype, nsize_int, DINT_cont )
            call int1_v_print_f( is, js, inttype, nsize_int, DINT_cont )
         end do
      end do
      end
