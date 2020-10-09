//pub struct FactoryBase();
pub struct FactoryBase {}
/* When use {}, ";" must be elimanated otherwise compile failed, while it's OK for struct (). This seems a strange compilation scenario. */

use hamburger::Hamburger;
use hamburger::New;

impl FactoryBase {
    pub fn create<T>() -> Box<T>
    where
        T: New + Hamburger,
    {
        println!("OK! Please wait...");
        let prod = Box::new(T::new());
        println!("A {} hamburger was made!", prod.get_type());
        prod
    }
}
