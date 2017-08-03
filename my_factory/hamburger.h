#include <string>
#include <vector>
#include <memory>

#include "factory_base.h"

// productA
class ChickenHb: public ProductBase
{
public:
    ChickenHb();
    //virtual ~ChickenHb();
        
};

// factoryA
class ChickenHbFactory: public FactoryBase
{
public:
    ChickenHbFactory();
    //virtual ~ChickenHbFactory();

    std::shared_ptr<ProductBase> create();
};

// Fish
class FishHb: public ProductBase
{
public:
    FishHb();
    //virtual ~FishHb();
        
};

class FishHbFactory: public FactoryBase
{
public:
    FishHbFactory();
    //virtual ~FishHbFactory();

    std::shared_ptr<ProductBase> create();
};

class SweetHb: public ProductBase
{
public:
    SweetHb();
    //virtual ~SweetHb();
        
};

class SweetHbFactory: public FactoryBase
{
public:
    SweetHbFactory();
    //virtual ~SweetHbFactory();

    std::shared_ptr<ProductBase> create();
};
