#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

struct Tiger {
   char const* name;
   PTRFUN* fn_ptr_table;
};

char const* greet(void){
  return "Ja sam tigretina!";
}
char const* menu(void){
  return "ljudsko meso, medium rare";
}

char const* name(void* this){
   struct Tiger* tiger = (struct Tiger*)this;
   return tiger->name;
}

PTRFUN tiger_fn_ptr_table[3] = {name,greet, menu};

void* create(char const* name){
   struct Tiger* tiger = malloc(sizeof(struct Tiger));
   tiger->name = name;
   tiger->fn_ptr_table = tiger_fn_ptr_table;
   return tiger;
};