#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>
#include <string.h>

#define _NROW_ 200
#define _NCOL_ 100

char* filename = "fort.99" ;

int main()
{
    int fd ;
    int na, nb, natom ;
    int i, j, rc ;
    uint32_t len ;
    double a[ _NROW_ * _NCOL_ ] ;
    char buff[ 100000 ] ;
    double zz[ 100 ] ;
    double xyz[ 100 ][ 3 ] ;
    na = 50 ;
    nb = 20 ;

    fd = open( filename, O_RDONLY ) ;
///
    rc = read( fd, &len, 4 ) ;
///    printf( "len = %u\n", len ) ;
    rc = read( fd, &natom, 4 ) ;
    rc = read( fd, &len, 4 ) ;
///    printf( "len = %u\n", len ) ;
///
    for ( i = 0 ; i < natom ; i++ ) {
        rc = read( fd, &len, 4 ) ;
///        printf( "len = %u\n", len ) ;
        rc = read( fd, buff, len ) ;
        rc = read( fd, &len, 4 ) ;
///        printf( "len = %u\n", len ) ;
        memcpy( zz + i,   buff+4,   8 ) ;
        memcpy( xyz[ i ], buff+4+8, 8*3 ) ;
    }
    
///
    rc = read( fd, &len, 4 ) ;
///    printf( "len = %u\n", len ) ;
    rc = read( fd, buff, len ) ;
    rc = read( fd, &len, 4 ) ;
///    printf( "len = %u\n", len ) ;
///
    memcpy( &na, buff + 0, 4           ) ;
    memcpy( &nb, buff + 4, 4           ) ;
    memcpy(   a, buff + 8, len - 4 * 2 ) ;

    printf( "natom,na,nb = %4d%4d%4d\n", natom, na, nb ) ;
    for ( i = 0 ; i < natom ; i++ ) {
        printf( "%5d%20.5e     %20.5e%20.5e%20.5e\n",
                i, zz[ i ], xyz[ i ][ 0 ], xyz[ i ][ 1 ], xyz[ i ][ 2 ] ) ;
    }
    for ( i = 0 ; i < na ; i++ ) {
        for ( j = 0 ; j < nb ; j++ ) {
            printf( "%5d%5d%20.5e\n", j+1, i+1, a[ _NROW_ * i + j ] ) ;
        }
    }
    
    close( fd ) ; 
    
    return 0 ;
}
//       program main
//       implicit none
//       integer nrow, ncol
//       parameter( nrow = 100, ncol = 100 )
//       integer i, j, na, nb
//       real*8 a(nrow,ncol)
//
//       na = 50
//       nb = 20
//
//       read(8) na, nb
//       read(8) a
//
//       do i = 1, na
//          do j = 1, nb
//             write(*,'(2i5,d20.5)') j, i, a(j,i)
//          enddo
//       enddo
//
//       end
