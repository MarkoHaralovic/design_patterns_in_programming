#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

struct Parrot {
   PTRFUN* fn_ptr_table;
   char const* name;
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

void construct(void * memory, const char* name){
   struct Parrot* parrot = (struct Parrot*)memory;
   parrot->name = name;
   parrot->fn_ptr_table = parrot_fn_ptr_table;
   return;
}

void* create(void * memory,char const* name){
   construct(memory, name);
   return memory;
};

size_t size_of(){
   return sizeof(struct Parrot);
}