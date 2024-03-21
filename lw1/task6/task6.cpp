#include <stdio.h>
#include <iostream>

class Base{
public:
  Base() {
    metoda();
    std::cout << "U baznoj klasi, u konstruktoru " << std::endl;
  }

  virtual void virtualnaMetoda() {
    printf("ja sam bazna implementacija!\n");
  }

  void metoda() {
    printf("Metoda kaze: ");
    virtualnaMetoda();
  }
};

class Derived: public Base{
public:
  Derived(): Base() {
    metoda();
    std::cout << "U derived, u konstruktoru " << std::endl;
  }
  virtual void virtualnaMetoda() {
    printf("ja sam izvedena implementacija!\n");
  }
};

int main(){
  Derived* pd=new Derived();
  pd->metoda();
}
