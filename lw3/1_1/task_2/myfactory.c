#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include "myfactory.h"

void* myfactory(char const* libname, char const* ctorarg, void* buffer){

   char* temp = malloc(strlen(libname) + 7); 
   strcpy(temp, "./"); 
   strcat(temp, libname); 
   strcat(temp, ".dll"); 
   libname = temp; 

   HINSTANCE library = (HINSTANCE)LoadLibrary(libname);
   
   free(temp);

   if (library == NULL)
   {
      return NULL;
   }

   FARPROC sizeof_func = (FARPROC)GetProcAddress(library,"size_of");
   if (sizeof_func == NULL){
      return NULL;
   }
   size_t size = ((size_t (*)())sizeof_func)();

   void* memory;
   if (buffer == NULL) {
        memory = malloc(size);
        if (!memory) {
            FreeLibrary(library);
            return NULL;
        }
    } else {
      if ((size_t)buffer < size){
         return NULL;
      }
        memory = buffer;
    }

   FARPROC create_function = (FARPROC)GetProcAddress(library, "create");

   if (create_function == NULL)
   {
      return NULL;
   }
   void* create_function_arg = ((void* (*)(void*, const char*))create_function)(memory, ctorarg);
   return create_function_arg;
}

