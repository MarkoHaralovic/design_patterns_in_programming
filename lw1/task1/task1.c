#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

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

void animalPrintGreeting(struct Animal* animal){
   printf("%s pozdravlja: %s\n", animal->name, animal->fn_ptr_table[0]());
   return;
}

void animalPrintMenu(struct Animal* animal){
   printf("%s voli: %s\n", animal->name, animal->fn_ptr_table[1]());
   return;
}

struct Animal* ConstructCat(struct Animal* animal, char const* name){
   animal->name = name;
   animal->fn_ptr_table = cat_fn_ptr_table;
   return animal;
}

struct Animal* ConstructDog(struct Animal* animal, char const* name){
   animal->name = name;
   animal->fn_ptr_table = dog_fn_ptr_table;
   return animal;
}

struct Animal* createDog(char const* name){
   struct Animal *animal = (struct Animal*) malloc(sizeof(struct Animal));
   return ConstructDog(animal,name);
}

struct Animal* createCat(char const* name){
   struct Animal *animal = (struct Animal*) malloc(sizeof(struct Animal));
   return ConstructCat(animal,name);
}

struct Animal** createNdogs(const char** names[], int n){
   struct Animal** dogs = (struct Animal**) malloc(n * sizeof(struct Animal*));
   for(int i = 0; i < n; i++){
      dogs[i] = createDog(names[i]);
   }
   return dogs;
};


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
  ConstructDog(&stackDog, "Laertes");
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