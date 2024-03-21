#include <iostream>

class B{
public:
  virtual int __cdecl prva()=0;
  virtual int __cdecl druga(int)=0;
};

class D: public B{
public:
  virtual int __cdecl prva(){return 42;}
  virtual int __cdecl druga(int x){return prva()+x;}
};

void print_values(B* pb, int x) {
    void** vtable = *(void***)pb;   
    int(*pfun_prva)();
    pfun_prva= (int(*)()) vtable[0];

    std::cout << "prva: " << pfun_prva() << std::endl;

    int(*pfun_druga)(B*,int);
    pfun_druga= (int(*)(B*,int)) vtable[1];

    std::cout << "druga: " << pfun_druga(pb,x) << std::endl;
}


int main() {
    D obj;
    print_values(&obj, 10);

    return 0;
}