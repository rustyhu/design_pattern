#include <string>
#include <vector>
#include <memory>


// Product waiting for inheritance
// what if it is abstract base?
class ProductBase {
public:
    // Avoid to use default constructor. This is like a debug tool.
    ProductBase(): price_(0) {
        std::cout << "Warning: initialize an empty ProductBase!\n";
    };

    ProductBase(std::string type, int price): type_(type),
                                              price_(price) {
        ++product_no_;
    };
                        
    virtual ~ProductBase() = 0;

    std::string getType() {
        return type_;
    };

    int getPrice() {
        return price_;
    };

    static int getProductNo() {
        return product_no_;
    };

    static void getProductTypes() {
        std::cout << "We provide these products:\n";
        for (auto i : product_types_) {
            std::cout << i << ";\n";
        }
    };

protected:
    std::string type_;
    int price_;

    // test: were static members of pure virtual class herited by 
    // subclass? No, all classes in heritance tree share only one
    // static instance from this base defination.
    static int product_no_;
    static std::vector<std::string> product_types_;
};

// chicken
class ChickenHb: public ProductBase {
public:
    ChickenHb();
};

// Fish
class FishHb: public ProductBase {
public:
    FishHb();
};

// Sweet
class SweetHb: public ProductBase {
public:
    SweetHb();
};

