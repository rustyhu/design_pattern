use std::io::stdin;

mod factory_base;
mod hamburger;

use factory_base::{FactoryBase, MenuList};
use hamburger::{
    ChickenHb, FishHb, SweetHb, Hamburger,
};

fn main() {
    let mut bill_sum = 0;
    let mut prod_no = 0;

    println!("Welcome! Begin to accept order!");

    let order_menu: Vec<&str> = vec![
        "1. chicken Hb",
        "2. fish Hb",
        "3. sweet Hb",
        "0. I need no more!",
    ];

    let mut check_bill = |ham: Box<dyn Hamburger>| {
        prod_no += 1;
        let price = ham.get_price();
        println!("Product Number: {}, Price: {}.", prod_no, price);
        bill_sum += price;
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
        match asking.trim().parse::<u32>() {
            // start cooking!
            Ok(i_ask) if i_ask == MenuList::CHICKEN as u32 => {
                check_bill(FactoryBase::create::<ChickenHb>());
            }
            Ok(i_ask) if i_ask == MenuList::FISH as u32 => {
                check_bill(FactoryBase::create::<FishHb>());
            }
            Ok(i_ask) if i_ask == MenuList::SWEET as u32 => {
                check_bill(FactoryBase::create::<SweetHb>())
            }
            Ok(i_ask) if i_ask == MenuList::NOMORE as u32 => break,
            Ok(_) => println!("Sorry! This type of product not provided!"),
            Err(e) => {
                println!("Invalid input: {}", e);
                continue;
            }
        }
    }

    println!("Please check the bill: {}, enter to ensure:", bill_sum);
    // read in any input to finish
    stdin()
        .read_line(&mut String::new())
        .expect("Failed to read line");

    println!("Thank you!");
}
