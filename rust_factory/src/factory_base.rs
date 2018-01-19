use hamburger::New;
use hamburger::Hamburger;

pub struct FactoryBase<T> {
    //name: String,
    unused_var: T,
}


impl<T> FactoryBase<T>
where T: New + Hamburger {
    pub fn new(t: T) -> FactoryBase<T> {
        FactoryBase {
            unused_var: t
        }
    }

    pub fn Create() -> Box<T> {
        let prod = Box::new(T::new());
        println!("A {} hamburger made!", prod.getType());
        prod
    }
}
