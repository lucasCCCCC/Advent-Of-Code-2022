#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void formatFile(FILE *fp) {
    fp = fopen("input.txt", "a");
    if (fp == NULL) exit(-1);
    putc('\n', fp);
    putc('\n', fp);
    fclose(fp);
}

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)b - *(int*)a );
}

int main() {
    int test = 0;
    FILE *fp;
    char buffer[128];

    int calories[250];
    int index = 0;

    formatFile(fp);

    fp = fopen("input.txt", "r");    
    if (fp == NULL) exit(-1);
    
    int temp = 0;

    while (fgets(buffer, 128, fp) != NULL) {
        if (strcmp(buffer, "\n") == 0) {
            calories[index] = temp;
            index++;
            temp = 0;
        } else if (strcmp(buffer, "\n") != 0) {
            temp+= atoi(buffer);
        }
    }

    fclose(fp);

    qsort(calories, 250, sizeof(int), cmpfunc);

    int top3Calories = calories[0] + calories[1] + calories[2];

    printf("Solution to part 1: %d\n", calories[0]);
    printf("Solution to part 2: %d\n", top3Calories);

    return 0;
}