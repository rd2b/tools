



#include <stdio.h>

int main(int argc, const char* argv[]){
    void printfile( const char* filename){
        FILE * pFile;
        int buffersize = 100;
        char buffer [buffersize];

        printf("Filename = %s", filename);
        pFile = fopen(filename,"r");

        if (pFile == NULL) perror("Error openning file.");
        else {
            while ( ! feof(pFile)){
                fgets(buffer, buffersize, pFile);
		printf(buffer);
            }
            fclose (pFile);
	}
    }
    int i;
    for ( i = 1; i < argc; i++){
        printfile(argv[i]);
    }
}
