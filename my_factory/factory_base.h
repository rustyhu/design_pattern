#include <iostream>
#include <string>
#include <vector>
#include <memory>

// Product waiting for inheritance
class ProductBase
{
public:
    ProductBase() {;}
    //virtual ~ProductBase() {;}
        
private:
    std::string name;
    std::string id;
        
    // test: were static members of pure virtual class herited by 
    // subclass?
    static int ProductNo;
};

// Factory waiting for inheritance
class FactoryBase
{
public:
    FactoryBase() {;}
    //virtual ~FactoryBase() {;}

    virtual std::shared_ptr<ProductBase> create()=0;

private:
    std::vector<std::shared_ptr<ProductBase>> ProductList_;

};
