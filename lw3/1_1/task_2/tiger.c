#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

struct Tiger {
   PTRFUN* fn_ptr_table;
   char const* name;
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

void construct(void * memory, const char* name){
   struct Tiger* tiger = (struct Tiger*)memory;
   tiger->name = name;
   tiger->fn_ptr_table = tiger_fn_ptr_table;
   return;
}

void* create(void * memory,char const* name){
   construct(memory, name);
   return memory;
};

size_t size_of(){
   return sizeof(struct Tiger);
}