#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef double (*PTRFUN)();

typedef struct {
   int lower_bound;
   int upper_bound;
   PTRFUN  *virtualTable;
} Unary_Function; 

typedef struct {
   Unary_Function unary_function;
   PTRFUN *vTable;
} Square;

typedef struct{
   Unary_Function unary_function;
   double a;
   double b;
   PTRFUN *vTable;
} Linear;


double value_at(Unary_Function* unary_function, double x){
   return unary_function->virtualTable[0](x);
}

double square_value_at(Square square, double x){
   return x*x;
}

double negative_value_at(Unary_Function* unary_function, double x){
    return -(unary_function->virtualTable[0])(x);
}


double linear_value_at(Linear* linear,  double x){
   return linear->a*x + linear->b;
}



PTRFUN unary_virtual_table[2] = {NULL, negative_value_at};
PTRFUN linear_virtual_table[2] = {linear_value_at, negative_value_at};
PTRFUN square_virtual_table[2] = {square_value_at, negative_value_at};



Unary_Function* ConstructUnaryFunction(Unary_Function* unary_function, int lower_bound, int upper_bound) {
    unary_function->lower_bound = lower_bound;
    unary_function->upper_bound = upper_bound;
    unary_function->virtualTable = unary_virtual_table;
    return unary_function;
}

void tabulate(Unary_Function* unary_function){
   for(int x = unary_function->lower_bound; x < unary_function->upper_bound;x++){
      printf("f(%d)=%lf\n", x, unary_function->virtualTable[0](x));

   }
}
bool same_functions_for_ints(Unary_Function* f1, Unary_Function *f2, double tolerance){
    if(f1->lower_bound != f2->lower_bound) return false;
    if(f1->upper_bound != f2->upper_bound) return false;
    for(int x = f1->lower_bound; x <= f1->upper_bound; x++) {
        double delta = f1->virtualTable[0](x) - f2->virtualTable[0](x);
        if(delta < 0) delta = -delta;
        if(delta > tolerance) return false;
    }
    return true;
}

Square* ConstructSquare(Square* square, int lower_bound, int upper_bound) {
   ConstructUnaryFunction(&(square->unary_function),lower_bound,upper_bound);
   square->vTable = square_virtual_table;
   return square;
}

Linear* ConstructLinear(Linear* linear, int lower_bound, int upper_bound, double a, double b) {
   ConstructUnaryFunction(&(linear->unary_function),lower_bound,upper_bound);
   linear->a = a; 
   linear->b = b;
   linear->vTable = linear_virtual_table;
   return linear;
}

struct Unary_Function* createUnaryFunction(int lower_bound, int upper_bound){
   Unary_Function *unary_function = malloc(sizeof(Unary_Function));
   return ConstructUnaryFunction(unary_function,lower_bound,upper_bound);
}

Square* createSquare(int lower_bound, int upper_bound){
   Square *s = malloc(sizeof(Square));
   return ConstructSquare(s, lower_bound, upper_bound);
}

Linear* createLinear(int lower_bound, int upper_bound, double a, double b){
   Linear *l = malloc(sizeof(Linear));
   return ConstructLinear(l, lower_bound, upper_bound, a, b);
}

int main(){
   Unary_Function *f1 = createSquare(-2,2);
   tabulate(f1);
   Unary_Function *f2 = createLinear(-2,2,5,-2);
   tabulate(f2);
   printf("f1==f2: %s\n", same_functions_for_ints(f1, f2, 1E-6) ? "DA" : "NE");
   printf("neg_val f2(1) = %lf\n", f2->virtualTable[1](1.0));
   free(f1);
   free(f2);
   return 0;
}

// EXPECTED OUTPUT
// f(-2)=4.000000
// f(-1)=1.000000
// f(0)=0.000000
// f(1)=1.000000
// f(2)=4.000000
// f(-2)=-12.000000
// f(-1)=-7.000000
// f(0)=-2.000000
// f(1)=3.000000
// f(2)=8.000000
// f1==f2: NE
// neg_val f2(1) = -3.000000