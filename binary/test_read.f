       program main
       implicit none
       integer nrow, ncol, iu
       parameter( nrow = 200, ncol = 100 )
       integer i, idummy, j, na, nb, natom
       real*8 zz(100), xyz(3,100), a(nrow,ncol)
!
       iu = 88
       iu = 99
       read(iu) natom
       do i = 1, natom
          read(iu) idummy, zz(i), (xyz(j,i),j=1,3)
       end do
       read(iu) na, nb, a
!
       write(*,'(3i5)') natom, na, nb
       do i = 1, natom
          write(*,'(i5,d20.5,5x,3d20.5)') i, zz(i), (xyz(j,i),j=1,3)
       enddo
       do i = 1, na
          do j = 1, nb
             write(*,'(2i5,d20.5)') j, i, a(j,i)
          enddo
       enddo

       end
