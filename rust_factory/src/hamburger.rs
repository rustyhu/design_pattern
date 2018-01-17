pub trait Hamburger {
    fn new() -> Self;
    fn getType(&self) -> &str; 
    fn getPrice(&self) -> u32;
}


pub struct ChickenHb {
    type_: String,
    price_: u32,
}


impl Hamburger for ChickenHb {
    fn new() -> Self {
        println!("Making a ChickenHb!");
        ChickenHb {
            type_ : String::from("chicken"),
            price_: 8
        }
    }

    fn getType(&self) -> &str {
        &(self.type_)
    }

    fn getPrice(&self) -> u32 {
        self.price_
    }
}

pub struct FishHb {
    type_: String,
    price_: u32,
}

impl Hamburger for FishHb {
    fn new() -> Self {
        println!("Making a FishHb!");
        FishHb {
            type_ : String::from("fish"),
            price_: 12
        }
    }
    fn getType(&self) -> &str {
        &(self.type_)
    }

    fn getPrice(&self) -> u32 {
        self.price_
    }
}


pub struct SweetHb {
    type_: String,
    price_: u32,
}

impl Hamburger for SweetHb {
    fn new() -> Self {
        println!("Making a FishHb!");
        SweetHb {
            type_ : String::from("sweet"),
            price_: 6
        }
    }
    fn getType(&self) -> &str {
        &(self.type_)
    }

    fn getPrice(&self) -> u32 {
        self.price_
    }
}
