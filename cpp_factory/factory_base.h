#include <iostream>
#include <string>
#include <vector>
#include <memory>

// I need only this Factory, that' all 
template<typename T>
class FactoryBase {
public:
    //FactoryBase() {};
    //~FactoryBase() {};

    std::unique_ptr<T> Create() {
        auto prod = std::unique_ptr<T>(new T);
        std::cout << "A " << prod->getType() << "Hamburger made!\n";
        return prod;
    };

};
