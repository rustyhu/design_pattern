#include <iostream>
#include <string>
#include <vector>

#include "hamburger.h"

enum HB_TYPE
{
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

int main()
{
    /* single thread process ordering task */
    // build factory!
    ChickenHbFactory chickenFac;
    FishHbFactory fishFac;
    SweetHbFactory sweetFac;

    // main produce pipeline
    FactoryBase* mainLine = nullptr;

    int iBillSum = 0;

    std::cout << "Begin to accept order!\n";

    int iAsking = 0;
    while (1)
    {
        for (const std::string &strChoice : orderMenu)
        {
            std::cout << strChoice;
        }
        std::cout << "Please make your choice: ";
        std::cin >> iAsking;
        if (iAsking == static_cast<int>(NOMORE))
            break;

        std::cout << "OK! Please wait for a moment...\n";
        switch (iAsking)
        {
            case CHICKEN:
                mainLine = &chickenFac; 
                break;
            case FISH:
                mainLine = &fishFac; 
                break;
            case SWEET:
                mainLine = &sweetFac; 
                break;
            default:
                mainLine = nullptr;
                std::cout << "Sorry! No this type of hamburger provided now!\n";
        }

        // cooking!
        if (mainLine)
        {
            mainLine->create();
        }
    }

    std::cout << "Please check the bill: " << iBillSum << std::endl;
    std::getchar();
    std::cout << "Thank you!" << std::endl;

    //return 0;
}
