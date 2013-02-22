
#include <stdlib.h>
#include <stdio.h>
#include <fftw3.h>

void transform( void );



double frand ( void )
{
    return ( ( double ) rand ( ) / ( RAND_MAX ) );
}



int main( int argc, char** argv )
{
    transform();

    return EXIT_SUCCESS;
}


void transform( void )
{
    int i;
    int n = 2000;
    int nc;
    double *in;
    fftw_complex *out;
    fftw_plan plan_forward;
    unsigned int seed = 19671111;

    in = fftw_malloc ( sizeof ( double ) * n );

    srand ( seed );
    for ( i = 0; i < n; i++ )
    {
        in[i] = frand ( );
    }

    nc = ( n / 2 ) + 1;
    out = fftw_malloc ( sizeof ( fftw_complex ) * nc );

    plan_forward = fftw_plan_dft_r2c_1d ( n, in, out, FFTW_ESTIMATE );
    fftw_execute ( plan_forward );

}


