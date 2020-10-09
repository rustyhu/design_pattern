use std::io::stdin;

mod factory_base;
mod hamburger;

use factory_base::FactoryBase;
use hamburger::ChickenHb;
use hamburger::FishHb;
use hamburger::Hamburger;
use hamburger::SweetHb;

enum HbType {
    CHICKEN = 1,
    FISH = 2,
    SWEET = 3,
    OTHER = 99,
    NOMORE = 0,
}
impl From<u32> for HbType {
    fn from(item: u32) -> Self {
        match item {
            0 => HbType::NOMORE,
            1 => HbType::CHICKEN,
            2 => HbType::FISH,
            3 => HbType::SWEET,
            _ => HbType::OTHER,
        }
    }
}

fn main() {
    let mut bill_sum = 0;
    let mut prod_no = 0;

    println!("Welcome! Begin to accept order!");

    let order_menu: Vec<&str> = vec![
        "\n1. chicken Hb",
        "2. fish Hb",
        "3. sweet Hb",
        "0. I need no more!",
    ];

    let mut check_bill = |ham: Box<dyn Hamburger>| {
        prod_no += 1;
        bill_sum += ham.get_price();
        println!("Product Number: {}, Price: {}.", prod_no, ham.get_price());
    };

    loop {
        for i in order_menu.iter() {
            println!("{}", i);
        }

        println!("Please make your choice: ");
        // stdin().read_line() would execute before print!(),
        // but not with println!(). Refer to character device line buffering.
        let mut asking = String::new();
        stdin().read_line(&mut asking).expect("Failed to read line");

        let i_ask = asking.trim().parse::<u32>();
        if let Err(e) = i_ask {
            println!("Invalid input: {}", e);
            continue;
        };

        match HbType::from(i_ask.unwrap()) {
            // start cooking!
            HbType::CHICKEN => check_bill(FactoryBase::create::<ChickenHb>()),
            HbType::FISH => check_bill(FactoryBase::create::<FishHb>()),
            HbType::SWEET => check_bill(FactoryBase::create::<SweetHb>()),
            HbType::NOMORE => break,
            _ => println!("Sorry! No this type of hamburger provided now!"),
        }
    }
    // The following is a legacy problem of the rustc compiler:
    // Limit the lifetime of the mut borrow of bill_sum and such long-live vars, to eliminate the conflicts by borrow rule.

    println!("Please check the bill: {}, enter to ensure:", bill_sum);
    stdin()
        .read_line(&mut String::new())
        .expect("Failed to read line");

    println!("Thank you!");
}
