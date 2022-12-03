#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *trimString(char *str){
    char *end;

    while(isspace((unsigned char)*str)) str++;

    if(*str == 0) return str;

    end = str + strlen(str) - 1;
    while(end > str && isspace((unsigned char)*end)) end--;

    end[1] = '\0';

    return str;
}

int main() {

    FILE *fp;
    char buffer[128];

    int scorePartA = 0;
    int scorePartB = 0;

    fp = fopen("input.txt", "r");

    if (fp == NULL) {
        printf("error");
        exit(-1);
    }


    while (fgets(buffer, 128, fp) != NULL) {
        char *plays[2];
        int index = 0;
        char *line = strtok(buffer, " ");

        while (line != NULL) {
            plays[index++] = line;
            line = strtok(NULL, " ");
        }
        
        plays[0] = trimString(plays[0]);
        plays[1] = trimString(plays[1]);

        if (strcmp(plays[0], "A") == 0 && strcmp(plays[1], "X") == 0) {
            scorePartA += 4;
            scorePartB += 3;
        } else if (strcmp(plays[0], "B") == 0 && strcmp(plays[1], "Y") == 0) {
            scorePartA += 5;
            scorePartB += 5;
        } else if (strcmp(plays[0], "C") == 0 && strcmp(plays[1], "Z") == 0) {
            scorePartA += 6;
            scorePartB += 7;
        } else if (strcmp(plays[0], "B") == 0 && strcmp(plays[1], "X") == 0) {
            scorePartA += 1;
            scorePartB += 1;
        } else if (strcmp(plays[0], "C") == 0 && strcmp(plays[1], "X") == 0) {
            scorePartA += 7;
            scorePartB += 2;
        } else if (strcmp(plays[0], "A") == 0 && strcmp(plays[1], "Y") == 0) {
            scorePartA += 8;
            scorePartB += 4;
        } else if (strcmp(plays[0], "C") == 0 && strcmp(plays[1], "Y") == 0) {
            scorePartA += 2;
            scorePartB += 6;
        } else if (strcmp(plays[0], "A") == 0 && strcmp(plays[1], "Z") == 0) {
            scorePartA += 3;
            scorePartB += 8;
        } else if (strcmp(plays[0], "B") == 0 && strcmp(plays[1], "Z") == 0) {
            scorePartA += 9;
            scorePartB += 9;
        }
    }

    fclose(fp);

    printf("\nSolution to part 1: %d\n", scorePartA);
    printf("Solution to part 2: %d\n", scorePartB);

    return 0;
}