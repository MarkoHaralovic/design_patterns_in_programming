#include <stdio.h>
#include <stdlib.h>

char const* dogGreet(void){
  return "vau!";
}
char const* dogMenu(void){
  return "kuhanu govedinu";
}
char const* catGreet(void){
  return "mijau!";
}
char const* catMenu(void){
  return "konzerviranu tunjevinu";
}

typedef char const* (*PTRFUN)();

PTRFUN cat_fn_ptr_table[2] = {catGreet, catMenu};
PTRFUN dog_fn_ptr_table[2] = {dogGreet, dogMenu};

struct Animal {
   char const* name;
   PTRFUN* fn_ptr_table;
};
struct Dog {
   char const* name;
   PTRFUN* fn_ptr_table;
};
struct Cat {
   char const* name;
   PTRFUN* fn_ptr_table;
};

void animalPrintGreeting(struct Animal* animal){
   printf("%s pozdravlja: %s\n", animal->name, animal->fn_ptr_table[0]());
   return;
}

void animalPrintMenu(struct Animal* animal){
   printf("%s voli: %s\n", animal->name, animal->fn_ptr_table[1]());
   return;
}

struct Animal* constructAnimal(struct Animal *animal, char const *name){
  animal->name = name;
  return animal;
}

struct Cat* constructCat(struct Cat* cat, char const* name){
   constructAnimal((struct Animal*) cat, name);
   cat->fn_ptr_table = cat_fn_ptr_table;
   return cat;
}

struct Dog* constructDog(struct Dog* dog, char const* name){
   constructAnimal((struct Animal*) dog, name);
   dog->fn_ptr_table = dog_fn_ptr_table;
   return dog;
}

struct Animal* createDog(char const*name){
  struct Dog *dog = (struct Dog*) malloc(sizeof(struct Dog));
  constructDog(dog, name);
  return (struct Animal*) dog;
}

struct Animal* createCat(char const* name){
   struct Cat *cat = (struct Cat*) malloc(sizeof(struct Cat));
   constructCat(cat,name);
   return (struct Animal*)  cat;
}

struct Animal** createNdogs(const char** names, int n){
    struct Animal** dogs = (struct Animal**) malloc(n * sizeof(struct Dog*));
    for(int i = 0; i < n; i++){
        dogs[i] = createDog(names[i]);
    }
    return dogs;
}


//   Hamlet pozdravlja: vau!
//   Ofelija pozdravlja: mijau!
//   Polonije pozdravlja: vau!
//   Hamlet voli kuhanu govedinu
//   Ofelija voli konzerviranu tunjevinu
//   Polonije voli kuhanu govedinu

void testAnimals(void){
  struct Animal* p1=createDog("Hamlet");
  struct Animal* p2=createCat("Ofelija");
  struct Animal* p3=createDog("Polonije");

  animalPrintGreeting(p1);
  animalPrintGreeting(p2);
  animalPrintGreeting(p3);

  animalPrintMenu(p1);
  animalPrintMenu(p2);
  animalPrintMenu(p3);

  free(p1); free(p2); free(p3);

  struct Animal stackDog;
  constructDog((struct Dog*) &stackDog, "Laertes");
  animalPrintGreeting(&stackDog);
  animalPrintMenu(&stackDog);

  const char* dog_names[] = {"psic1", "psic2", "psic3", "psic4", "psic5"};
  struct Animal** dogs = createNdogs(dog_names, 5);
 
  for(int i = 0; i < 5; i++) {
      free(dogs[i]);
  }
  free(dogs);

}

int main(){
   testAnimals();
}