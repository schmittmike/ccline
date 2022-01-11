#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <unistd.h>

int intpow(int x, int y);
void termsFromArg(char *arg, int *terms);
int commaCount(char *string);

int commaCount(char *string) {
    int i=0, result=0;
    while (string[i] != '\0') {
        if (string[i] == ',')
            result += 1;
        i++;
    }
    return result;
}

int intpow(int x, int y) {
    int result=x;
    if (y == 0) return 1;
    
    for (int i=1; i<y; i++)
        result *= x;

    return result;
}

void termsFromArg(char *arg, int *terms) {
    int i=0, j=0, k=0, w=0;
    char *buf = malloc(16 * sizeof(char));
    
    while (arg[i] != '\0') {
        if (arg[i] == ',') {
            for (j-=1;j>=0;j--)
                terms[k] += (buf[j]-'0')*intpow(10, w++);
            w=0, j=0, i++, k++;     //reset for next number
            
        } else if (arg[i] == ' ') {
            i++;
        } else if (isdigit(arg[i])) {
            buf[j++] = arg[i++];
        } else {
            printf("unreachable\n");
        }
    }
    for (j-=1;j>=0;j--)
        terms[k] += (buf[j]-'0')*intpow(10, w++); //take care of final number (no comma)

    free(buf);
}

int main(int argc, char **argv) {
    int opt, literals, termcount=0;
    int *terms = calloc(commaCount(argv[1]) + 1, sizeof(int));
    while ((opt = getopt(argc, argv, "n:t:")) != -1) {
        switch (opt) {
        case 't':
            termsFromArg(optarg, terms);
            termcount = commaCount(optarg)+1;
            break;
        case 'n':
            literals = atoi(optarg);
            break;
        default: // "?"
            fprintf(stderr, "Usage: %s [-t terms] [-n literals per term]\n", argv[0]);
            return 1;
        }
    }

    printf("terms:\n");
    for (int i=0; i<termcount; i++)
        printf("%d ", terms[i]);
    printf("\nliterals: %d\n", literals);

    //char inArray[] = {"15, 12, 3, 0\0"};

    free(terms);
}
