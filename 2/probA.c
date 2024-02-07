#include <stdio.h>

int main(){
    int M;
    scanf("%d", &M);
    for(int i = 1; i <= M ; i += 2){
        printf("%d ", i);
    }

    return 0;
}