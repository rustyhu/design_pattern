// E-commerce Restaurant Order Management

// billing check example, to test Rust dynamical type machanism

use std::io::stdin;

mod factory_base;
mod hamburger;

use factory_base::{FactoryBase, MenuList};
use hamburger::{
    ChickenHb, FishHb, SweetHb, Hamburger,
};

struct FrontDesk {
    bill_sum: u32,
    prod_no: u32,
}
impl FrontDesk {
    fn check_bill(&mut self, ham: Box<dyn Hamburger>) {
        self.prod_no += 1;
        let price = ham.get_price();
        println!("Product Number: {}, Price: {}.", self.prod_no, price);
        self.bill_sum += price;
    }
}

fn main() {
    let mut fdesk = FrontDesk{bill_sum: 0, prod_no:0};

    println!("Welcome! What would you like to order:");
    loop {
        println!("");
        for (i, desc) in factory_base::MENU_DESCRIPTIONS {
            println!("{}. {}", *i as i32, desc);
        }

        println!("Please make your choice: ");
        // stdin().read_line() would execute before print!(),
        // but not with println!(). Refer to character device line buffering.
        let mut asking = String::new();
        stdin().read_line(&mut asking).expect("Failed to read line");
        match asking.trim().parse::<u32>() {
            // start cooking!
            Ok(i_ask) if i_ask == MenuList::CHICKEN as u32 => {
                fdesk.check_bill(FactoryBase::create::<ChickenHb>());
            }
            Ok(i_ask) if i_ask == MenuList::FISH as u32 => {
                fdesk.check_bill(FactoryBase::create::<FishHb>());
            }
            Ok(i_ask) if i_ask == MenuList::SWEET as u32 => {
                fdesk.check_bill(FactoryBase::create::<SweetHb>())
            }
            Ok(i_ask) if i_ask == MenuList::NOMORE as u32 => break,
            Ok(_) => println!("Sorry! This type of product not provided!"),
            Err(e) => {
                println!("Invalid input: {}", e);
                continue;
            }
        }
    }

    println!("Please check the bill: {}, enter to ensure:", fdesk.bill_sum);
    // read in any input to finish
    stdin()
        .read_line(&mut String::new())
        .expect("Failed to read line");

    println!("Thank you!");
}
