#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>


int manhatten_distance(int a, int b, int w);

int manhatten_distance(int a, int b, int w){
    int a_x,a_y,b_x,b_y;
    int dis;
    a =  a - 1;
    b = b - 1;
    a_x = a/w;
    a_y = a%w;
    b_x = b/w;
    b_y = b%w;
    dis = abs(a_x - b_x) + abs(a_y - b_y);
    return dis;
}

double fsigmoid(float x){
    double result;
    result = 1 / (1 + exp(x));
    return result;
}

bool inArray(int value, int len , int sp[len]){
    int i;
    for (i=0; i<len; i++){
        if (sp[i] == value) {
            return true;
        }
    }
    return false;
}

int **penalty(int len, int len2, int sp[len2], int w){

    int i,j;
//    int df[len][len];
    int **df =(int **)malloc(len * sizeof(int *));
    for (i = 0; i<len; i++){
        df[i] = (int *)malloc(len * sizeof(int));
     }
    for (i = 0; i < len; i++){
        for (j = 0; j < len; j++){
            df[i][j] = 0;
        }
    }
    for (i = 1; i < len - 1; i++){
        for (j=i+1; j < len - 1; j++)
        if ( i != j) {
            if ( inArray(i,len2,sp)){

            df[i][j] = (int)(fsigmoid((manhatten_distance(i,j,w) / 0.90)) * 6.5);
            }
            else {
            df[i][j] = (int)(fsigmoid((manhatten_distance(i, j, w) / 0.995)) * 14);
            }
        }

    }
    return df;
}

//int main(){
//    int len = 12;
//    int len2 = 3;
//    int sp[3] = {2, 5, 6};
//    int w = 2;
//    int **result = penalty(len,len2,sp, w);
//    int i,j;
//    for (i=0;i<len;i++){
//        for (j=0;j<len;j++){
//            printf("%d,",result[i][j]);
//        }
//        printf("\n");
//    }
//}