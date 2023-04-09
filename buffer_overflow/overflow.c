#include <stdio.h>
#include <string.h>
#include <time.h>
int exploitable( char* arg );
void abhinav();

int main( int argc, char **argv )
{
    char a[100], b[100], c[100], d[100];
    exploitable( argv[1] );
    return  0 ;
}
int exploitable(  char* arg)
{
    char buffer[10];
    strcpy( buffer, arg );
    //gets(buffer);
    printf( "The buffer says .. [%s/%p].\n", buffer, &buffer );
    return  0 ;
}
void abhinav()
{
    printf("Abhinav Dutta, CS547 \n");
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    printf("%s \n", asctime(tm));
}