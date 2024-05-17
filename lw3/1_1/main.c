#include "myfactory.h"

#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

// struct Animal{
//   PTRFUN* vtable;
//   // vtable entries:
//   // 0: char const* name(void* this);
//   // 1: char const* greet();
//   // 2: char const* menu();
// };
struct Animal {
   char const* name;
   PTRFUN* fn_ptr_table;
};

// parrots and tigers defined in respective dynamic libraries

// animalPrintGreeting and animalPrintMenu similar as in lab 1
void animalPrintGreeting(struct Animal* animal){
   printf("%s pozdravlja: %s\n", animal->name, animal->fn_ptr_table[1]());
   return;
}

void animalPrintMenu(struct Animal* animal){
   printf("%s voli: %s\n", animal->name, animal->fn_ptr_table[2]());
   return;
}

int main(int argc, char *argv[]){
  if (argc < 3) {
       printf("Usage: %s <library_name> <constructor_argument>\n", argv[0]);
       return 1;
   }
  for (int i=0; i<argc/2; ++i){
    struct Animal* p=(struct Animal*)myfactory(argv[1+2*i], argv[1+2*i+1]);
    if (!p){
      printf("Creation of plug-in object %s failed.\n", argv[1+2*i]);
      continue;
    }

    animalPrintGreeting(p);
    animalPrintMenu(p);
    free(p); 
  }
}

