#include <iostream>
#include <string>
#include <vector>

#include "factory_base.h"
#include "hamburger.h"

enum HB_TYPE {
    CHICKEN = 1, 
    FISH = 2, 
    SWEET = 3, 
    NOMORE = 99,
};

std::vector<std::string> orderMenu =
{
    "1. chicken Hb\n",
    "2. fish Hb\n",
    "3. sweet Hb\n",
    "99. I need no more!\n",
};

int main() {
    /* single thread process ordering task */

    // main produce pipeline
    //FactoryBase* mainLine = nullptr;  //(when base class used)
    FactoryBase mainFactory;

    int iBillSum = 0;
    std::cout << "Begin to accept order!\n";

    int iAsking = 0;
    while (1) {
        for (auto& strChoice : orderMenu) {
            std::cout << strChoice;
        }
        std::cout << "Please make your choice: ";
        std::cin >> iAsking;
        std::cout << std::endl;

        if (iAsking == static_cast<int>(NOMORE))
            break;

        // else
        std::cout << "OK! Please wait...\n";
        auto CheckBill = [&](std::unique_ptr<ProductBase> hamburger) {
            std::cout << "Product Number: " << hamburger->getProductNo()
                << "; Price: " << hamburger->getPrice()
                << "\n\n";
            iBillSum += hamburger->getPrice();
        };

        switch (iAsking) {
            // cooking!
            case CHICKEN:
                CheckBill(mainFactory.Create<ChickenHb>());
                break;
            case FISH:
                CheckBill(mainFactory.Create<FishHb>());
                break;
            case SWEET:
                CheckBill(mainFactory.Create<SweetHb>());
                break;
            default:
                std::cout << "Sorry! No this type of hamburger provided now!\n\n";
        }
    }

    std::cout << "Please check the bill: " << iBillSum << std::endl;
    std::getchar();
    std::cout << "Thank you!" << std::endl;

    return 0;
}
