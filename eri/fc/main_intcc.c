#include<stdio.h>
#include<stdlib.h>

#define _NSH 13
#define _NPR 28
#define _NAT  3
#define _ML   1

int    numb_shell = _NSH ;
int    numb_prim  = _NPR ;
int    numb_atom  = _NAT ;
int    maxl       = _ML  ;

int    shel_lqn[] = { 0, 0, 0, 0, 1, 1, 1, 0, 0, 1,  0, 0, 1 } ;
int    shel_atm[] = { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,  2, 2, 2 } ;
int    shel_tem[] = { 5, 2, 1, 1, 1, 3, 1, 3, 1, 3,  3, 1, 3 } ;
int    shel_add[] = { 0, 5, 7, 8, 9,10,13,14,17,18, 21,24,25 } ;
int    shel_ini[] = { 0, 1, 2, 3, 4, 7,10,13,14,15, 18,19,20 } ;

double atom_zz [] = { 8.0e0, 1.0e0, 1.0e0 } ;
double atom_xyz[] = { 1.84626229e0, -0.72376505e0,  2.58892457e0,
                      0.95053217e0, -1.04501847e0,  1.05068765e0,
                      3.56969239e0, -0.51589519e0,  2.07491913e0 } ;
double prim_exp[] = { 5.0657590099999998e+03, 7.6080541299999993e+02,
                      1.7306691900000001e+02, 4.8688319000000007e+01,
                      1.5572176000000001e+01, 1.0158026999999999e+01,
                      9.3726299999999996e-01, 5.2547980000000001e+00,
                      2.8650600000000004e-01, 2.2210805000000004e+01,
                      1.7691086000000002e+01, 3.8521809999999999e+00,
                      1.0449199999999998e+00, 2.7504099999999998e-01,
                      1.3010700269999999e+01, 1.9622570800000001e+00,
                      4.4453797000000000e-01, 1.2194961999999999e-01,
                      2.8606729999999998e+00, 8.8819000000000004e-01,
                      3.0377599999999999e-01, 1.3010700269999999e+01,
                      1.9622570800000001e+00, 4.4453797000000000e-01,
                      1.2194961999999999e-01, 2.8606729999999998e+00,
                      8.8819000000000004e-01, 3.0377599999999999e-01 } ;
double prim_coe[] = { 1.1520426087473887e+00, 2.1219762063841294e+00,
                      3.4146270844410713e+00, 4.4040672419995586e+00,
                      3.6112031237508075e+00,-6.2708283493057582e-01,
                      7.1569294634675040e-01, 2.4735865551015990e+00,
                      2.7910035138546846e-01, 6.8729860422543865e+01,
                      3.2410517821686669e+00, 2.5663992531302311e+00,
                      1.1162275504579231e+00, 2.8391405061454988e-01,
                      1.6349038957298870e-01, 2.7735153639996912e-01,
                      3.1575014844115706e-01, 1.4707722621719763e-01,
                      6.8332898898525340e-01, 7.6170728997588932e-01,
                      1.1994223393465964e-01, 1.6349038957298870e-01,
                      2.7735153639996912e-01, 3.1575014844115706e-01,
                      1.4707722621719763e-01, 6.8332898898525340e-01,
                      7.6170728997588932e-01, 1.1994223393465964e-01 } ;
///
int main()
{
    int i, is, js, level_print ;
    int inttype, nsize_int ;
    double tol, DINT_cont[81] ;

    level_print = 4 ;
    tol = 1.0e10 ;

	fprintf( stdout, "sizeof(          short     ) = %4lu\n", sizeof(          short     ) ) ;
	fprintf( stdout, "sizeof(          long      ) = %4lu\n", sizeof(          long      ) ) ;
	fprintf( stdout, "sizeof(          int       ) = %4lu\n", sizeof(          int       ) ) ;
	fprintf( stdout, "sizeof(          long int  ) = %4lu\n", sizeof(          long int  ) ) ;
	fprintf( stdout, "sizeof(          long long ) = %4lu\n", sizeof(          long long ) ) ;
	fprintf( stdout, "sizeof( unsigned short     ) = %4lu\n", sizeof( unsigned short     ) ) ;
	fprintf( stdout, "sizeof( unsigned long      ) = %4lu\n", sizeof( unsigned long      ) ) ;
	fprintf( stdout, "sizeof( unsigned int       ) = %4lu\n", sizeof( unsigned int       ) ) ;
	fprintf( stdout, "sizeof( unsigned long int  ) = %4lu\n", sizeof( unsigned long int  ) ) ;
	fprintf( stdout, "sizeof( unsigned long long ) = %4lu\n", sizeof( unsigned long long ) ) ;

    int1_s_init_( &numb_atom, &numb_shell, &numb_prim,
                  shel_lqn, shel_tem, shel_atm, shel_add,
                  atom_zz,  atom_xyz, prim_exp, prim_coe,
                  &tol,     &level_print ) ;
    int1_t_init_( &numb_atom, &numb_shell, &numb_prim,
                  shel_lqn, shel_tem, shel_atm, shel_add,
                  atom_zz,  atom_xyz, prim_exp, prim_coe,
                  &tol,     &level_print ) ;
    int1_v_init_( &numb_atom, &numb_shell, &numb_prim,
                  shel_lqn, shel_tem, shel_atm, shel_add,
                  atom_zz,  atom_xyz, prim_exp, prim_coe,
                  &tol,     &level_print ) ;

    fprintf( stdout, "\n" ) ;
    for( is = 0 ; is < numb_shell ; is++ ) {
        for( js = 0 ; js <= is ; js++ ) {
		    for ( i = 0 ; i < 81 ; i++ ) { DINT_cont[ i ] = 0 ; }
            int1_s_calc_ ( &is, &js, &inttype, &nsize_int, DINT_cont ) ;
            int1_s_print_( &is, &js, &inttype, &nsize_int, DINT_cont ) ;
	    }
	}
    fprintf( stdout, "\n" ) ;
    for( is = 0 ; is < numb_shell ; is++ ) {
        for( js = 0 ; js <= is ; js++ ) {
		    for ( i = 0 ; i < 81 ; i++ ) { DINT_cont[ i ] = 0 ; }
            int1_t_calc_ ( &is, &js, &inttype, &nsize_int, DINT_cont ) ;
            int1_t_print_( &is, &js, &inttype, &nsize_int, DINT_cont ) ;
	    }
	}
    fprintf( stdout, "\n" ) ;
    for( is = 0 ; is < numb_shell ; is++ ) {
        for( js = 0 ; js <= is ; js++ ) {
		    for ( i = 0 ; i < 81 ; i++ ) { DINT_cont[ i ] = 0 ; }
            int1_v_calc_ ( &is, &js, &inttype, &nsize_int, DINT_cont ) ;
            int1_v_print_( &is, &js, &inttype, &nsize_int, DINT_cont ) ;
	    }
	}
	return 0 ;
}
