

#include <stdio.h>

int main (int argc, const char* argv[]){
    void printspaces(int size){
        int i;
        char * spaces = "";
        for(i=0; i<size; i++){
            spaces[i] = spaces " ";
        }
        printf("%s",*spaces);
    }

    //trunk is 6 times lesser than size
    void maketrunk (int size){
        int level;
        int trunkfactor = 6;
        for(level=0; level<=size/trunkfactor; level++){
            int i;
            int spaces = size * 2/3;
            printspaces(spaces -1);
            printf("{");
            printspaces(spaces);
            printf("}\n");
            
        }
    }

    void makebody (int size){
        int level;
        int position = size;
        int i;
        for(level=0; level<size; level++){
            position--;
            printspaces(position);
            printf("/");
            printspaces(level * 2 +1 );
            printf("\\\n");
        }
    }

    void makehead(int size){
        int spaces = size;
        int i;
        printspaces(spaces);
        printf("+\n");
    }

    int size=30;
    if (argv[1] != NULL){
        makehead(size);
        makebody(size);
        maketrunk(size);
        printf("size = %d",size);
    } else {
        perror("please enter size !");
    }
}

