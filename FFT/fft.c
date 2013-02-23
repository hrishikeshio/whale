
/*
 * requires
 *    libsndfile
 *    libfftw3
 *
 *     sudo apt-get install libfftw3-doc 
 *                  libfftw3-3 libfftw3-bin
 *                  libfftw3-dev
 */

#include <stdlib.h>
#include <stdio.h>
#include <fftw3.h>
#include <sndfile.h>


double frand ( void )
{
    return ( ( double ) rand ( ) / ( RAND_MAX ) );
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


void test_read( void )
{
    SF_INFO a_sf_info;
    SNDFILE* sf = NULL;
    double *in;
    int n = 2000;

    sf_count_t n_to_read = n;
    sf_count_t n_read = 0;

    in = fftw_malloc ( sizeof ( double ) * n );
    sf = sf_open( "train19050.aiff", SFM_READ, &a_sf_info );

    n_read = sf_read_double( sf, in, n_to_read );

    for ( int i = 0; i < n; ++i ) {
        printf( "%d %f\n", i, in[i] );
    }
    printf( "Read %d samples\n", n_read );
}


int main( int argc, char** argv )
{
    test_read();
    transform();
    return EXIT_SUCCESS;
}

