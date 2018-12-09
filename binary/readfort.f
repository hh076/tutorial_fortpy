       subroutine read_fort( iu, natom, zz, xyz, na, nb, amat )
       implicit none
       integer nrow, ncol, nat
       parameter( nrow = 200, ncol = 100, nat = 100 )
       integer iu, i, idummy, j, na, nb, natom
       real*8 zz(nat), xyz(3,nat), amat(nrow,ncol)
!
       read(iu) natom
       do i = 1, natom
          read(iu) idummy, zz(i), (xyz(j,i),j=1,3)
       end do
       read(iu) na, nb, amat
       end
