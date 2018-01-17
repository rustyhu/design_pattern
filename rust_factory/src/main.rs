use std::io::stdin;
use std::convert::From;

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

    let orderMenu: Vec<&str> = vec![
        "1. chicken Hb\n",
        "2. fish Hb\n",
        "3. sweet Hb\n",
        "0. I need no more!\n",
    ];

    let mut bill_sum = 0;
    let mut prod_no = 0;
    fn CheckBill<T: Hamburger>(ham: Box<T>,
                               ref_no: &mut u32,
                               ref_bill: &mut u32) {
        *ref_no += 1;
        *ref_bill+= ham.getPrice();
        println!("Product Number: {}, Price: {}.", 
                 *ref_no,
                 ham.getPrice());
    };

    let mut asking = String::new();
    println!("Welcome! Begin to accept order!");
    loop {
        for i in orderMenu.iter() {
            print!("{}", i);
        }

        println!("Please make your choice: ");
        // stdin().read_line() would execute before print!(),
        // but not with println!(). Seems a bug.
        asking = String::new();
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
            HB_TYPE::CHICKEN => CheckBill(FactoryBase::<ChickenHb>::Create(), &mut prod_no, &mut bill_sum),
            HB_TYPE::FISH => CheckBill(FactoryBase::<FishHb>::Create(), &mut prod_no, &mut bill_sum),
            HB_TYPE::SWEET => CheckBill(FactoryBase::<SweetHb>::Create(), &mut prod_no, &mut bill_sum),
            _ => println!("Sorry! No this type of hamburger provided now!"),
        }
    }

    println!("Please check the bill: {}", bill_sum);
    stdin().read_line(&mut asking);
    println!("Thank you!");
}
