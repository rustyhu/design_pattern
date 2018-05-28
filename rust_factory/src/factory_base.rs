pub struct FactoryBase();

use hamburger::New;
use hamburger::Hamburger;

impl FactoryBase {
    /*
    pub fn new(t: T) -> FactoryBase<T> {
        FactoryBase {
            unused_var: t
        }
    }
    */

    pub fn create<T>() -> Box<T>
    where T: New + Hamburger {
        println!("OK! Please wait...");
        let prod = Box::new(T::new());
        println!("A {} hamburger was made!", prod.get_type());
        prod
    }
}
