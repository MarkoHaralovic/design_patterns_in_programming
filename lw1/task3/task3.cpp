#include <iostream>

class CoolClass{
public:
  virtual void set(int x){x_=x;};
  virtual int get(){return x_;};
private:
  int x_;
};
class PlainOldClass{
public:
  void set(int x){x_=x;};
  int get(){return x_;};
private:
  int  x_;
};

// Ispitajte memorijske zahtjeve objekata dvaju tipova (pomoć: ispiši sizeof(PlainOldClass) i sizeof(CoolClass)).
//  Objasnite dobivenu razliku. Ako dobijete rezultate koje ne možete objasniti, pročitajte kada i zašto prevoditelj
//   nadopunjava objekte (engl. padding).

int main() {

    std::cout << "size of  CoolClass class : " << sizeof(CoolClass) << " B\n";
    std::cout << "size of PlainOldClass class: " << sizeof(PlainOldClass) << " B\n";
    CoolClass cool_class;
    cool_class.set(5);

    return 0;
}
