      subroutine mmult( A, B, C, KA, KB, KC, L, M, N )
      implicit none
      integer          KA, KB, KC, L, M, N
      double precision A( KA, M ), B( KB, N ), C( KC, N )
      integer          i, j, k
c
      write(*,'(a)') 'm2: A:'
      do i = 1, L
         write(*,'(a,i4,10d20.5)') 'm2:', i, ( A( i, j ), j = 1, M )
      enddo
      write(*,'(a)') 'm2: B:'
      do i = 1, M
         write(*,'(a,i4,10d20.5)') 'm2:', i, ( B( i, j ), j = 1, N )
      enddo
c
      do j = 1, N
         do k = 1, M
            C( i, j ) = 0
            do i = 1, L
               C ( i, j ) = C( i, j ) + A( i, k ) * B( k, j )
            end do
         end do
      end do
c
      write(*,'(a)') 'm2: C:'
      do i = 1, L
         write(*,'(a,i4,10d20.5)') 'm2:', i, ( C( i, j ), j = 1, N )
      enddo
c
      end
