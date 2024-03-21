#include <iostream>

class B{
public:
  virtual int prva()=0;
  virtual int druga(int)=0;
};

class D: public B{
public:
  virtual int prva(){return 42;}
  virtual int druga(int x){return prva()+x;}
};

void print_values(B* pb, int x) {
    void** vtable = *(void***)pb;   
    int(*pfun_prva)();
    pfun_prva= (int(*)()) vtable[0];

    std::cout << "prva: " << pfun_prva() << std::endl;

   //  int(*pfun_druga)(int);
   //  pfun_druga= (int(*)(int)) (vtable[0]+4);

   //  std::cout << "druga: " << pfun_druga(x) << std::endl;
}


int main() {
    D obj;
    print_values(&obj, 10);

    return 0;
}