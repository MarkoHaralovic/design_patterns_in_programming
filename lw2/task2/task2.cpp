#include <iostream>
#include <string>
#include <vector>
#include <set>

int gt_int(const int& a, const int& b){
    if(a > b) return 1;
    return 0;
}

int gt_char(const char& a, const char& b){
   if (a > b) return 1;
   return 0;
}

int gt_str(std::string str1, std::string str2){
   if (str1>str2) return 1;
   return 0;
}

template <typename Iterator, typename Predicate>
Iterator mymax(
  Iterator first, Iterator last, Predicate pred){

   if(first == last) return last;

   Iterator max = first;
   ++first;

   while(first!=last){
      if(pred(*first, *max)>0){
         max = first;
      }
      ++first;
   }
   return max;
}

int main(){
   int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
   std::string arr_str[] = {
      "Gle", "malu", "vocku", "poslije", "kise",
      "Puna", "je", "kapi", "pa", "ih", "njise"
   };
  std::vector<int> vect_int { 1,2,3,4,5 }; 
  std::set<int> set_int({1,2,3,4,5}); 


  const int* maxint = mymax(&arr_int[0], &arr_int[sizeof(arr_int)/sizeof(*arr_int)], gt_int);
  std::cout <<"Maxint : " <<*maxint <<"\n";

  //used chatgpt to solve this as I defined std::string and I couldn't see the issue I had
  auto maxstr = mymax(&arr_str[0], &arr_str[sizeof(arr_str)/sizeof(*arr_str)], gt_str);
  std::cout <<"Maxstr : " <<*maxstr <<"\n";

  const int* maxint_v = mymax(&vect_int.at(0), &vect_int[vect_int.size()], gt_int);
  std::cout <<"Maxint_v : " <<*maxint_v <<"\n";

  auto maxint_s = mymax(set_int.begin(), set_int.end(), gt_int);
  std::cout <<"Maxint : " <<*maxint_s <<"\n";

}