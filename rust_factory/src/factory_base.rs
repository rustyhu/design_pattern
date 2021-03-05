use hamburger::*;

#[derive(Clone, Copy)]
pub enum MenuList {
    CHICKEN = 1,
    FISH = 2,
    SWEET = 3,
    // OTHER = 9999,
    NOMORE = 0,
}
/* implement std::convert::From to deal with convertion
impl From<&str> for MenuList {
    fn from(item: &str) -> Self {
        match item {
            "0" => MenuList::NOMORE,
            "1" => MenuList::CHICKEN,
            "2" => MenuList::FISH,
            3 => MenuList::SWEET,
            _ => MenuList::NOMORE,
        }
    }
}
*/

pub static MENU_DESCRIPTIONS: &[(MenuList, &str)] = &[
    (MenuList::CHICKEN, "chicken hamburger"),
    (MenuList::FISH, "fish hamburger"),
    (MenuList::SWEET, "sweet hamburger"),
    (MenuList::NOMORE, "I need no more and check out"),
];

pub struct FactoryBase {}
impl FactoryBase {
    pub fn create<T: New + Hamburger>() -> Box<T> {
        println!("OK! Please wait...");
        let prod = Box::new(T::new());
        println!("A {} hamburger was made!", prod.get_type());
        prod
    }
}
