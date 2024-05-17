#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

struct Parrot {
   char const* name;
   PTRFUN* fn_ptr_table;
};

char const* greet(void){
  return "Ja sam papiga!";
}
char const* menu(void){
  return "sitnu hranu";
}

char const* name(void* this){
   struct Parrot* parrot = (struct Parrot*)this;
   return parrot->name;
}

PTRFUN parrot_fn_ptr_table[3] = {name,greet, menu};

void* create(char const* name){
   struct Parrot* parrot = malloc(sizeof(struct Parrot));
   parrot->name = name;
   parrot->fn_ptr_table = parrot_fn_ptr_table;
   return parrot;
};