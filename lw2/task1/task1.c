#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gt_int(const void* a, const void* b){
   int *a_int = (int*)a;
   int *b_int = (int*)b;
   if(*a_int > *b_int) return 1;
   return 0;
}

int gt_char(const void* a, const void* b){
   char *a_char = (char*)a;
   char *b_char = (char*)b;
   if (*a_char > *b_char) return 1;
   return 0;
}

int gt_str(const void* str1, const void* str2){
   const char **str1_char = (const char**)str1;
   const char **str2_char = (const char**)str2;
   int comparison = strcmp(*str1_char,*str2_char);
   if (comparison > 0){
      return 1;
   }else return 0;
}

const void* mymax(const void *base, size_t nmemb, size_t size,int (*compar)(const void *, const void *)){
   const void* max = NULL;  
   for(size_t i=0;i<nmemb;i++){
      void* currentElement = (char*)base + i * size;
      if (max == NULL){
         max = currentElement;
      }
      if (compar(currentElement,max)==1){
         max = currentElement;
      }
   }

   return max;
}

int main() {
   int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
   char arr_char[] = "Suncana strana ulice";
   const char* arr_str[] = {
      "Gle", "malu", "vocku", "poslije", "kise",
      "Puna", "je", "kapi", "pa", "ih", "njise"
   };

   int *max_int = (int *) mymax(arr_int, 9, sizeof(int), gt_int);
   printf("Max in arr_int: %d\n", *max_int);
   char* max_char = (char *) mymax(arr_char, 21, sizeof(char), gt_char);
   printf("Max in arr_char: %c\n", *max_char);
   const char *max_str = *(const char **) mymax(arr_str, 11, sizeof(char*), gt_str);
   printf("Max in arr_str: %s\n", max_str);
}