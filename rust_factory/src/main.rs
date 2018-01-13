//mod factory_base;
//mod hamburger;

enum HB_TYPE {
    CHICKEN = 1, 
    FISH = 2, 
    SWEET = 3, 
    NOMORE = 99,
}

fn main() {
    let orderMenu: Vec<&str> = vec![
        "1. chicken Hb\n",
        "2. fish Hb\n",
        "3. sweet Hb\n",
        "99. I need no more!\n",
    ];

    let bill_sum = 0;
    println!("Begin to accept order!");

    let asking = 0;
    loop {
    }

    // Debug
    for i in orderMenu {
        print!("{}", i);
    }
}
