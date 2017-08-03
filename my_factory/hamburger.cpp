#include <iostream>
#include <string>
#include <vector>

#include "hamburger.h"

// Chicken
ChickenHb::ChickenHb()
{
    std::cout << "Making a ChickenHb!\n";
}

ChickenHbFactory::ChickenHbFactory()
{
    ;
}

std::shared_ptr<ProductBase> ChickenHbFactory::create()
{
    return std::make_shared<ChickenHb>();
}

// Fish
FishHb::FishHb()
{
    std::cout << "Making a FishHb!\n";
}

FishHbFactory::FishHbFactory()
{
    ;
}

std::shared_ptr<ProductBase> FishHbFactory::create()
{
    return std::make_shared<FishHb>();
}

// Sweet
SweetHb::SweetHb()
{
    std::cout << "Making a SweetHb!\n";
}

SweetHbFactory::SweetHbFactory()
{
    ;
}

std::shared_ptr<ProductBase> SweetHbFactory::create()
{
    return std::make_shared<SweetHb>();
}

