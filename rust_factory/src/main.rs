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
    //let chicken_fac = FactoryBase::new(ChickenHb::new());
    //let fish_fac = FactoryBase::new(FishHb::new());
    //let sweet_fac = FactoryBase::new(SweetHb::new());

    let mut bill_sum = 0;
    let mut prod_no = 0;

    println!("Welcome! Begin to accept order!");

    {
        let orderMenu: Vec<&str> = vec![
            "1. chicken Hb\n",
            "2. fish Hb\n",
            "3. sweet Hb\n",
            "0. I need no more!\n",
        ];

        let mut CheckBill = | ham: Box<Hamburger> | {
            prod_no += 1;
            bill_sum += ham.getPrice();
            println!("Product Number: {}, Price: {}.", 
                     prod_no,
                     ham.getPrice());
        };

        loop {
            for i in orderMenu.iter() {
                print!("{}", i);
            }

            println!("Please make your choice: ");
            // stdin().read_line() would execute before print!(),
            // but not with println!(). Seems a bug.
            let mut asking = String::new();
            stdin().read_line(&mut asking).expect("Failed to read line");

            //println!("DEBUGGING: {:?}", asking);
            let i_ask = asking.trim()
                              .parse::<u32>()
                              .expect("Parse to u32 failed!");
            if i_ask == (HB_TYPE::NOMORE as u32) {
                break;
            }
            //else
            println!("OK! Please wait...");

            match HB_TYPE::from(i_ask) {
                // start cooking!
                HB_TYPE::CHICKEN => CheckBill(FactoryBase::<ChickenHb>::Create()),
                HB_TYPE::FISH => CheckBill(FactoryBase::<FishHb>::Create()),
                HB_TYPE::SWEET => CheckBill(FactoryBase::<SweetHb>::Create()),
                _ => println!("Sorry! No this type of hamburger provided now!"),
            }
        }
    } // Limit the lifetime of the mut borrow of bill_sum and such long-live vars, to eliminate the conflicts by borrow rule.

    println!("Please check the bill: {}", bill_sum);
    stdin().read_line(&mut String::new()).expect("Failed to read line");
    println!("Thank you!");
}
