pub trait New {
    fn new() -> Self;
}

pub trait Hamburger {
    fn get_type(&self) -> &str; 
    fn get_price(&self) -> u32;
}

macro_rules! impl_hamburger {
    ($name: ident, $price: expr) => {
        pub struct $name {
            type_: String,
            price_: u32,
        }

        impl New for $name {
            fn new() -> Self {
                println!("Making a {}!", stringify!($name));
                $name {
                    type_ : stringify!($name).to_string(),
                    price_: $price,
                }
            }
        }
        impl Hamburger for $name {
            fn get_type(&self) -> &str {
                &(self.type_)
            }

            fn get_price(&self) -> u32 {
                self.price_
            }
        }
    };
}

impl_hamburger!(ChickenHb, 8);
impl_hamburger!(FishHb, 12);
impl_hamburger!(SweetHb, 6);
