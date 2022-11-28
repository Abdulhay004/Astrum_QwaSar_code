#include "Makefile"

/* checks the transmitted data for equality */
int equal_wll(char *matn1, char *matn2)
{
    int wl = 0;
    for(int i = 0; i < strlen(matn1); i++) {
        if(matn1[i] == matn2[i]) {
            wl ++;
        }
    }
    return wl;
}

/* Misplaced pieces */
int equal_ms(char *matn1, char *matn2)
{
    int ms = 0;
    for(int i = 0; matn1[i] != '\0'; i++) {
        for(int j = 0; matn2[j] != '\0'; j++) {
            if(matn1[i] != matn2[i] && matn1[i] == matn2[j]){
                ms++;
            }
        }
    }
    return ms;
}

/* checks that the reference is not duplicated */
int is_repeat(char *matn) 
{
    for(int i = 0; i < strlen(matn) - 1; i++) {
        for(int j = i; j < strlen(matn); j++) {
            if(matn[i] == matn[j+1]) {
                return 1;
            }
        }
    }
    return 0;
}

/* my strcmp */
int mystrcmp(char *a, char* b)
{
    for(int i = 0; i < strlen(a); i++){
        if(a[i] != b[i]){
            return 0;
        }
    }
    return 1;
}

/* wrong input */
int wrong_input(char *matn)
{
    if(strlen(matn) != 4) {
        return 1;
    }
    for(int i = 0; i < strlen(matn); i++){
        if(matn[i] > '7' || matn[i] < '0' || is_repeat(matn)){
            return 1;
        }
    }
    return 0;
}

/* whether the random number was repeated */
int in_code(char*matn, char r) 
{
    if(matn == 0){
        return 1;
    }
    for(int i = 0; i < strlen(matn); i++) {
        if(matn[i] == r) {
            return 0;
        }
    }
    return 1;
}

/* my strcpy */
char* my_strcpy(char* destination, char* source)
{
    for(int i = 0; i < strlen(source); i++){
        destination[i] = source[i];
    }
    return destination;
}

/* get rand code */
char* get_rand() 
{
    char *code = malloc(4);
    int i = 0;
    srand(time(0));
    while(strlen(code) < 4){
        char r = rand() % 8 + '0';
        if(in_code(code, r))
            code[i++] = r;
        
    }
    return code;
}

/* main function */
int main(int argc, char* argv[]) {
    char *ran_code = malloc(4);
    char *input_code = malloc(4);
    int rounds;
    int c = 0;
    int t = 0;
    
    for(int i = 1; i < argc; i++){
        if(mystrcmp(argv[i], "-c")){
            c = i + 1;
        }
        if(mystrcmp(argv[i], "-t")){
            t = i + 1;
            rounds = atoi(argv[t]);
        }
    }
    
    if(c == 0){
        ran_code = get_rand();
    }else{
        my_strcpy(ran_code, argv[c]);
    }
    
    printf("%s\n", ran_code);
    
    printf("Will you find the secret code?\n");
    for(int i = 0; i < rounds; i++) {
        printf("---\nround %d \n>",i);
        scanf("%s", input_code);
        
        if(wrong_input(input_code)){
            printf("Wrong input!\n");
            continue;
        }
        int wll = equal_wll(ran_code, input_code);
        int ms = equal_ms(ran_code, input_code);
     
        
        if(wll == 4){
            printf("Congratz! You did it!\n");
            break;
        }else{
            printf("Well placed pieces: %d\n", wll);
            printf("Misplaced pieces: %d\n", ms);
        }
        
    }
    
    
    return 0;
}
