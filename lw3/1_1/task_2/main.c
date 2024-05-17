#include "myfactory.h"
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>  

typedef char const* (*PTRFUN)();

struct Animal {
    PTRFUN* fn_ptr_table;
    char const* name;
};

void animalPrintGreeting(struct Animal* animal){
   printf("%s pozdravlja: %s\n", animal->fn_ptr_table[0](animal), animal->fn_ptr_table[1]());
   return;
}

void animalPrintMenu(struct Animal* animal){
   printf("%s voli: %s\n", animal->fn_ptr_table[0](animal), animal->fn_ptr_table[2]());
   return;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <library_name> <constructor_argument>\n", argv[0]);
        return 1;
    }

    for (int i = 0; i < (argc - 1) / 2; ++i) {
        void* stack_memory = alloca(sizeof(struct Animal));

        struct Animal* p = (struct Animal*)myfactory(argv[1 + 2 * i], argv[2 + 2 * i], stack_memory);
        if (!p) {
            printf("Creation of plug-in object %s failed.\n", argv[1 + 2 * i]);
            continue;
        }

        animalPrintGreeting(p);
        animalPrintMenu(p);
    }
    return 0;
}
