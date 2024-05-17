#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include "myfactory.h"

void* myfactory(char const* libname, char const* ctorarg){

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
   FARPROC create_function = (FARPROC)GetProcAddress(library, "create");

   if (create_function == NULL)
   {
      return NULL;
   }
   void * create_function_arg = ((void* (*)(const char*))create_function)(ctorarg);
   return create_function_arg;
}