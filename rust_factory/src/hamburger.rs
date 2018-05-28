pub trait New {
    fn new() -> Self;
}

pub trait Hamburger {
    fn get_type(&self) -> &str; 
    fn get_price(&self) -> u32;
}


pub struct ChickenHb {
    type_: String,
    price_: u32,
}


impl New for ChickenHb {
    fn new() -> Self {
        println!("Making a ChickenHb!");
        ChickenHb {
            type_ : String::from("chicken"),
            price_: 8
        }
    }
}
impl Hamburger for ChickenHb {
    fn get_type(&self) -> &str {
        &(self.type_)
    }

    fn get_price(&self) -> u32 {
        self.price_
    }
}

pub struct FishHb {
    type_: String,
    price_: u32,
}

impl New for FishHb {
    fn new() -> Self {
        println!("Making a FishHb!");
        FishHb {
            type_ : String::from("fish"),
            price_: 12
        }
    }
}
impl Hamburger for FishHb {
    fn get_type(&self) -> &str {
        &(self.type_)
    }

    fn get_price(&self) -> u32 {
        self.price_
    }
}


pub struct SweetHb {
    type_: String,
    price_: u32,
}

impl New for SweetHb {
    fn new() -> Self {
        println!("Making a FishHb!");
        SweetHb {
            type_ : String::from("sweet"),
            price_: 6
        }
    }
}
impl Hamburger for SweetHb {
    fn get_type(&self) -> &str {
        &(self.type_)
    }

    fn get_price(&self) -> u32 {
        self.price_
    }
}
