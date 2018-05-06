#include <iostream>
#include <string>
#include <vector>
#include <memory>

// I need only this Factory, that' all 
class FactoryBase {
public:
    //FactoryBase() {};
    //~FactoryBase() {};

    template<typename T>
    std::unique_ptr<T> Create() {
        auto prod = std::unique_ptr<T>(new T);
        std::cout << "A " << prod->getType() << "Hamburger made!\n";
        return prod;
    };

};
