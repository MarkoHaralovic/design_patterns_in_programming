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

// OUTPUT:  size of  CoolClass class : 8 B, size of PlainOldClass class: 4 B

// Objašnjenje: PlainOldClass sadrži privatni razredni član x_, za koji je tip potrebno alocirati 4B podataka. Kod CoolClass klase,
// ispis je da je veličina 8B, iz razloga što je dodatnih 4B zauzeto pokazivačem klase na tablicu virtualnih funkcija, u kojoj su 
// popisane metode klase (virtualne metode set i get), a taj  pokazivač je dodan svakom objektu te klase


// Explanation: The PlainOldClass contains a private class member x_, for which 4B of data needs to be allocated.
// In the case of the CoolClass,the output shows that the size is 8B. The reason for this is that an additional 4B is occupied
// by the class pointer to the virtual function table, where the class methods (virtual methods set and get) are listed.
// This pointer is added to every object of that class.