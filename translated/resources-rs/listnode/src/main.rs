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

        pub fn from_list(values: &[i32]) -> Option<Box<Self>> {
            if values.is_empty() {
                return None;
            }
            let mut head = Box::new(Self::new(values[0]));
            let mut last_node = &mut *head;
            for &val in &values[1..] {
                let new_node = Box::new(Self::new(val));
                last_node.next = Some(new_node);
                last_node = last_node.next.as_mut().unwrap();
            }
            Some(head)
        }

        pub fn from_list_unsafe(values: &[i32]) -> Option<Box<Self>> {
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
            Some(Box::new(result))
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


fn test_to_list_from_list()
{
    use listnode::*;

    let values = vec![ vec![1,2,3,4,5], vec![7,9,4,3], vec![], vec![1], ];
    let checks = values.clone();
    assert_eq!(values, checks);

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
    }
    println!();
}


fn traversal_non_mutating()
{
    use listnode::*;

    let vals = vec![1,2,3,4,5];
    let check = vals.clone();
    let head = ListNode::from_list(&vals);

    //  Using `while let Some()`
    let mut result = vec![];
    let mut node = &head;
    while let Some(curr) = node {
        result.push(curr.val);
        node = &curr.next;
    }
    assert_eq!(vals, result);

    //  Using `match`
    let mut result = vec![];
    let mut node = &head;
    while node.is_some() {
        match node {
            Some(n) => {
                result.push(n.val);
                node = &n.next;
            },
            None => {}
        }
    }
    assert_eq!(vals, result);

    //  Using `if let Some()`
    let mut result = vec![];
    let mut node = &head;
    loop {
        if let Some(n) = node {
            result.push(n.val);
            node = &n.next;
        } else {
            break;
        }
    }

}


fn traversal_mutate_values() 
{
    use listnode::*;

    let vals = vec![1,2,3,4,5];
    let mut head = ListNode::from_list(&vals);

    let mut node = &mut head;
    while let Some(curr) = node {
        curr.val = 0;
        node = &mut curr.next;
    }
    assert_eq!(head.unwrap().to_list(), vec![0,0,0,0,0]);
}


fn traversal_consume_list()
{
    use listnode::*;

    let vals = vec![1,2,3,4,5];
    let mut head = ListNode::from_list(&vals);

    let mut result = vec![];
    while let Some(mut node) = head {
        head = node.next.take();
        node.next = None;
        result.push(*node);
    }
    //println!("{:?}", result);
    
}


fn traversal_pointers()
{
    use listnode::*;

    let vals = vec![1,2,3,4,5];
    let mut head = ListNode::from_list(&vals);

    let mut result: Vec<*mut Option<Box<ListNode>>> = vec![];
    unsafe {
        let mut raw_node = &mut head as *mut Option<Box<ListNode>>;
        while let Some(node) = raw_node.as_mut().unwrap().as_mut() {
            result.push(raw_node);
            raw_node = &mut node.next as *mut _;
        }
    }

}


fn main() 
{
    test_to_list_from_list();
    traversal_non_mutating();
    traversal_mutate_values();
    traversal_consume_list();
    traversal_pointers();
}

