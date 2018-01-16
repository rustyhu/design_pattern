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
    NOMORE = 0,
}
impl From<u32> for HB_TYPE {
    fn from(item: u32) -> Self {
        match item {
            0 => HB_TYPE::NOMORE,
            1 => HB_TYPE::CHICKEN,
            2 => HB_TYPE::FISH,
            3 => HB_TYPE::SWEET,
            _ => {
                println!("HB_TYPE match exception!");
                HB_TYPE::NOMORE
            }
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

    let bill_sum = 0;
    println!("Begin to accept order!");

    let mut asking = String::new();
    loop {
        for i in orderMenu.iter() {
            print!("{}", i);
        }

        print!("Please make your choice: ");
        stdin().read_line(&mut asking).expect("Failed to read line");
        println!();

        let type_ask: u32 = asking.parse().unwrap();
        if type_ask == (HB_TYPE::NOMORE as u32) {
            break;
        }
        //else
        println!("OK! Please wait...");

        let mut prod_no = 0;
        fn CheckBill<T: Hamburger>(ham: Box<T>, ref_no: &mut u32) {
            *ref_no += 1;
            println!("Product Number: {}, Price: {}.", 
                     *ref_no,
                     (*ham).getPrice());
        };

        match HB_TYPE::from(type_ask) {
            // start cooking!
            HB_TYPE::CHICKEN => CheckBill(FactoryBase::<ChickenHb>::Create(), &mut prod_no),
            HB_TYPE::FISH => CheckBill(FactoryBase::<FishHb>::Create(), &mut prod_no),
            HB_TYPE::SWEET => CheckBill(FactoryBase::<SweetHb>::Create(), &mut prod_no),
            _ => println!("Sorry! No this type of hamburger provided now!"),
        }
    }

    println!("Please check the bill: {}", bill_sum);
    stdin().read_line(&mut asking);
    println!("Thank you!");
}
