use std::io::stdin;

mod factory_base;
mod hamburger;

use factory_base::FactoryBase;
use hamburger::Hamburger;
use hamburger::ChickenHb;
use hamburger::FishHb;
use hamburger::SweetHb;

enum HB_TYPE {
    CHICKEN = 1, 
    FISH = 2, 
    SWEET = 3, 
    OTHER = 99,
    NOMORE = 0,
}
impl From<u32> for HB_TYPE {
    fn from(item: u32) -> Self {
        match item {
            0 => HB_TYPE::NOMORE,
            1 => HB_TYPE::CHICKEN,
            2 => HB_TYPE::FISH,
            3 => HB_TYPE::SWEET,
            _ => HB_TYPE::OTHER,
        }
    }
}

fn main() {
    let mut bill_sum = 0;
    let mut prod_no = 0;

    println!("Welcome! Begin to accept order!");

    {
        let orderMenu: Vec<&str> = vec![
            "\n1. chicken Hb",
            "2. fish Hb",
            "3. sweet Hb",
            "0. I need no more!",
        ];

        let mut CheckBill = | ham: Box<Hamburger> | {
            prod_no += 1;
            bill_sum += ham.get_price();
            println!("Product Number: {}, Price: {}.", 
                     prod_no,
                     ham.get_price());
        };

        loop {
            for i in orderMenu.iter() {
                println!("{}", i);
            }

            println!("Please make your choice: ");
            // stdin().read_line() would execute before print!(),
            // but not with println!(). Seems a bug.
            let mut asking = String::new();
            stdin().read_line(&mut asking).expect("Failed to read line");

            let i_ask = asking.trim().parse::<u32>();
            if let Err(e) = i_ask {
                println!("Invalid input: {}", e);
                continue;
            };

            match HB_TYPE::from(i_ask.unwrap()) {
                // start cooking!
                HB_TYPE::CHICKEN => CheckBill(FactoryBase::create::<ChickenHb>()),
                HB_TYPE::FISH => CheckBill(FactoryBase::create::<FishHb>()),
                HB_TYPE::SWEET => CheckBill(FactoryBase::create::<SweetHb>()),
                HB_TYPE::NOMORE => break,
                _ => println!("Sorry! No this type of hamburger provided now!"),
            }
        }
    }
    // Limit the lifetime of the mut borrow of bill_sum and such long-live vars, to eliminate the conflicts by borrow rule.

    println!("Please check the bill: {}, enter to ensure:", bill_sum);
    stdin().read_line(&mut String::new()).expect("Failed to read line");
    println!("Thank you!");
}
