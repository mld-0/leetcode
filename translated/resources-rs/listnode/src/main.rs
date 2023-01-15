//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(unused)]

//  Continue: 2023-01-15T22:26:27AEDT (how to) implement 'from_list()' without using unsafe/pointers?

pub mod listnode {

    #[derive(PartialEq, Eq, Clone, Debug)]
    pub struct ListNode {
        pub val: i32,
        pub next: Option<Box<ListNode>>
    }
    
    impl ListNode {
        #[inline]
        pub fn new(val: i32) -> Self {
            ListNode { val, next: None, }
        }
        pub fn from_list(values: &[i32]) -> Option<Self> {
            if values.len() == 0 {
                return None;
            }
            let mut result = Self::new(0);
            let mut first = &mut result as *mut Self;
            let mut second = first;
            unsafe {
                for v in values {
                    (*first).val = *v;
                    (*first).next = Some(Box::new(Self::new(0)));
                    second = first;
                    first = (*first).next.as_deref_mut().unwrap() as *mut Self;
                }
                (*second).next = None;
            }
            Some(result)
        }
        pub fn to_list(&self) -> Vec<i32> {
            let mut result = vec![];
            let mut first = Some(self);
            while first.is_some() {
                result.push(first.as_ref().unwrap().val);
                first = first.unwrap().next.as_deref();
            }
            result
        }
        pub fn to_string(&self) -> String {
            format!("{:?}", self.to_list())
        }
    }

}

fn main() 
{
    use listnode::*;

    let values = vec![ vec![1,2,3,4,5], vec![7,9,4,3], vec![], vec![1], ];
    let checks = values.clone();

    for (value, check) in values.iter().zip(checks.iter()) {
        let loop_node = ListNode::from_list(value);
        print!("loop_node=({:?})\n", loop_node);
        let loop_list = if loop_node.is_some() {
            loop_node.unwrap().to_list()
        } else {
            vec![]
        };
        print!("loop_list=({:?})\n", loop_list);
        assert_eq!(loop_list, *check);
        println!();
    }
}

