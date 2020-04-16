#include "hamburger.h"

// static
int ProductBase::product_no_ = 0;
std::vector<std::string> ProductBase::product_types_;

ProductBase::~ProductBase() {}

// Chicken
ChickenHb::ChickenHb(): ProductBase("chicken", 8) {
    /* could not directly init these member vars derived from base class. */
    std::cout << "Making a ChickenHb!\n";
}

// Fish
FishHb::FishHb(): ProductBase("fish", 12) {
    std::cout << "Making a FishHb!\n";
}

// Sweet
SweetHb::SweetHb(): ProductBase("sweet", 6) {
    std::cout << "Making a SweetHb!\n";
}
