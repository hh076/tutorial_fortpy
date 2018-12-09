      program main
      implicit none
      integer          KA, KB, KC, L, M, N
      parameter( KA = 10, KB = 12, KC = 14, L = 3, M = 5, N = 4 )
      double precision A(KA,M), B(KB,N), C(KC,N)
      integer          i, j
      !
      do i = 1, L
         do j = 1, M
            A( i, j ) = ( i * 4.3893d0    + j * 3.930933d0     )
     &                  * 0.1d0
         enddo
      enddo
      do i = 1, M
         do j = 1, N
            B( i, j ) = ( i * 3.3393839d0 + j * 1.8393930933d0 )
     &                  * 0.05d0
         enddo
      enddo
      write(*,'(a)') 'f:  A:'
      do i = 1, L 
         write(*,'(a,i4,10d20.5)') 'f: ', i, (A(i,j),j=1,M)
      enddo
      write(*,'(a)') 'f:  B:'
      do i = 1, M 
         write(*,'(a,i4,10d20.5)') 'f: ', i, (B(i,j),j=1,N)
      enddo
      !
      call mmult( A, B, C, KA, KB, KC, L, M, N )
      !
      write(*,'(a)') 'f:  C:'
      do i = 1, L
         write(*,'(a,i4,10d20.5)') 'f: ', i, (C(i,j),j=1,N)
      enddo
      !
      end
