#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef double* (*PTRFUN)(double);

double value_at(double x);
double negative_value_at(double x){
   return -value_at(x);
}
PTRFUN unary_virtual_table[2] = {NULL, negative_value_at};

typedef struct {
   int lower_bound;
   int upper_bound;
   PTRFUN **virtualTable;
} Unary_Function; 

Unary_Function* ConstructUnaryFunction(Unary_Function* unary_function, int lower_bound, int upper_bound) {
    unary_function->lower_bound = lower_bound;
    unary_function->upper_bound = upper_bound;
    unary_function->virtualTable = unary_virtual_table;
    return unary_function;
}

void tabulate(Unary_Function* unary_function){
   for(int x = unary_function->lower_bound; x < unary_function->upper_bound;x++){
      printf("f(%d)=%lf\n", x, unary_function->virtualTable[0][x]);
   }
};
static bool same_functions_for_ints(Unary_Function* f1, Unary_Function *f2, double tolerance){
    if(f1->lower_bound != f2->lower_bound) return false;
    if(f1->upper_bound != f2->upper_bound) return false;
    for(int x = f1->lower_bound; x <= f1->upper_bound; x++) {
        double delta = f1->virtualTable[0] - f2->virtualTable[0];
        if(delta < 0) delta = -delta;
        if(delta > tolerance) return false;
    }
    return true;
}
double square_value_at(double x){
   return x*x;
};

PTRFUN square_virtual_table[2] = {square_value_at, negative_value_at};

typedef struct {
   Unary_Function unary_function;
   void **vTable;
} Square;


Square* ConstructSquare(Square* square, int lower_bound, int upper_bound) {
   ConstructUnaryFunction(&(square->unary_function),lower_bound,upper_bound);
   square->vTable = square_virtual_table;
   return square;
}

typedef struct{
   Unary_Function unary_function;
   int a;
   int b;
   void **vTable;
} Linear;

double linear_value_at(Linear* linear,  double x){
   return (linear->a)*x + linear->b;
};

PTRFUN linear_virtual_table[2] = {linear_value_at, negative_value_at};

Linear* ConstructSquare(Linear* linear, int lower_bound, int upper_bound, double a, double b) {
   ConstructUnaryFunction(&(linear->unary_function),lower_bound,upper_bound);
   linear->a = a; 
   linear->b = b;
   linear->vTable = linear_virtual_table;
   return linear;
}

int main(){
   
}