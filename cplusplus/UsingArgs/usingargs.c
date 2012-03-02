//#######################################################
//#	Name: 	usingargs.c				#
//#	Description: TODO				#
//#######################################################

#include <stdio.h>

int main( int argc, const char* argv[]){
    int i;
    for ( i = 0; i < argc; i++){
        printf("%d arg = %s\n", i, argv[i]);
    }
}

