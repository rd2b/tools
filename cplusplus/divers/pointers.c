

#include <stdio.h>

int main( int argc, const char* argv[]){

    //Fonction utilisant le byref :
    int add (int* a, int* b){
        printf("adress un %p\n",&a);
        return *a + *b;
    } 
    ////////////////////////////////////
    int i = 0;
    int * b;
    b = &i;
    printf("%s\n", argv[0]);
    printf("i = %d\n", i);
    printf("b = %p\n", b);
    * b = 12;
    printf("i = %d\n", i);
    printf("b = %p\n", b);
    ////////////////////////////////////
    
    int un = 1;
    int deux = 2;
    int result ;
    printf("adress un %p\n", &un);
    result = add(&un, &deux);
    printf("adress un %p\n", &un);
    printf(" %d + %d = %d\n", un, deux, result);
    return 0;
}
