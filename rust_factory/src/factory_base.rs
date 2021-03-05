pub enum MenuList {
    CHICKEN = 1,
    FISH = 2,
    SWEET = 3,
    NOMORE = 0,
}
/* implement std::convert::From to deal with convertion
impl From<u32> for HbType {
    fn from(item: u32) -> Self {
        match item {
            0 => HbType::NOMORE,
            1 => HbType::CHICKEN,
            2 => HbType::FISH,
            3 => HbType::SWEET,
            _ => HbType::NOMORE,
        }
    }
}
*/

use hamburger::New;
use hamburger::Hamburger;

//pub struct FactoryBase();
pub struct FactoryBase {}
/* When use {}, ";" must be elimanated otherwise compile failed,
while it's must for struct(). This seems a strange compilation scenario. */

impl FactoryBase {
    pub fn create<T: New + Hamburger>() -> Box<T>
    {
        println!("OK! Please wait...");
        let prod = Box::new(T::new());
        println!("A {} hamburger was made!", prod.get_type());
        prod
    }
}
