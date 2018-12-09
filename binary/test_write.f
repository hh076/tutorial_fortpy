       program main
       implicit none
       integer nrow, ncol, iu
       parameter( nrow = 200, ncol = 100 )
       integer i, j, na, nb, natom
       real*8 zz(100), xyz(3,100), a(nrow,ncol)

       iu = 99

       natom = 3
       na = 50
       nb = 20

       zz( 1 ) = 8.0d0
       zz( 2 ) = 1.0d0
       zz( 3 ) = 3.0d0

       xyz( 1, 1 ) =  1.84626229d0
       xyz( 2, 1 ) = -0.72376505d0
       xyz( 3, 1 ) =  2.58892457d0
       xyz( 1, 2 ) =  0.95053217d0
       xyz( 2, 2 ) = -1.04501847d0
       xyz( 3, 2 ) =  1.05068765d0
       xyz( 1, 3 ) =  3.56969239d0
       xyz( 2, 3 ) = -0.51589519d0
       xyz( 3, 3 ) =  2.07491913d0

       do i = 1, na
          do j = 1, nb
             a(j,i) = 5.39d0 + 0.7983d0 * ( i * j + 1 )
          enddo
       enddo

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       write(*,'(i5)') natom
       do i = 1, natom
          write(*,'(i5,d20.5,5x,3d20.5)') i, zz(i), (xyz(j,i),j=1,3)
       enddo
       do i = 1, na
          do j = 1, nb
             write(*,'(2i5,d20.5)') j, i, a(j,i)
          enddo
       enddo

       write(iu) natom
       do i = 1, natom
          write(iu) i, zz(i), (xyz(j,i),j=1,3)
       end do

       write(iu) na, nb, a
       end
