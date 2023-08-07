//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2

// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }

#[path = "./listnode.rs" ]
mod listnode;
use listnode::listnode::*;

use std::time::Instant;

//  macro: vec_of_strings
//  {{{
macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}
//  }}}

struct Solution {}

impl Solution {

    //  runtime: beats 100%
    pub fn merge_two_lists_iterative(mut l1: Option<Box<ListNode>>, mut l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if l1.is_none() && l2.is_none() {
            return None;
        }
        let mut result = Some(Box::new(ListNode::new(0)));
        let mut node = result.as_deref_mut().unwrap() as *mut ListNode;
        let mut previous = node;
        unsafe {
            while l1.is_some() && l2.is_some() {
                if l1.as_deref().unwrap().val < l2.as_deref().unwrap().val {
                    (*node).val = l1.as_deref().unwrap().val;
                    l1 = l1.unwrap().next;
                } else {
                    (*node).val = l2.as_deref().unwrap().val;
                    l2 = l2.unwrap().next;
                }
                (*node).next = Some(Box::new(ListNode::new(0)));
                previous = node;
                node = (*node).next.as_deref_mut().unwrap() as *mut _;
            }
            while l1.is_some() {
                (*node).val = l1.as_ref().unwrap().val;
                l1 = l1.unwrap().next;
                (*node).next = Some(Box::new(ListNode::new(0)));
                previous = node;
                node = (*node).next.as_deref_mut().unwrap() as *mut _;
            }
            while l2.is_some() {
                (*node).val = l2.as_deref().unwrap().val;
                l2 = l2.unwrap().next;
                (*node).next = Some(Box::new(ListNode::new(0)));
                previous = node;
                node = (*node).next.as_deref_mut().unwrap() as *mut _;
            }
            (*previous).next = None;
        }
        result
    }


    //  runtime: beats 100%
    pub fn merge_two_lists_recursive(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if l1.is_none() {
            return l2;
        }
        if l2.is_none() {
            return l1;
        }
        if l1.as_deref().unwrap().val < l2.as_deref().unwrap().val {
            let mut l1_unwrapped = l1.unwrap();
            let l1_next = l1_unwrapped.next;
            l1_unwrapped.next = Self::merge_two_lists_recursive(l1_next, l2);
            return Some(l1_unwrapped);
        } else {
            let mut l2_unwrapped = l2.unwrap();
            let l2_next = l2_unwrapped.next;
            l2_unwrapped.next = Self::merge_two_lists_recursive(l1, l2_next);
            return Some(l2_unwrapped);
        }
    }

}


fn main() 
{
    let functions: Vec<fn(Option<Box<ListNode>>,Option<Box<ListNode>>)->Option<Box<ListNode>>> = vec![ Solution::merge_two_lists_iterative, Solution::merge_two_lists_recursive, ];
    let functions_names = vec_of_strings![ "merge_two_lists_iterative", "merge_two_lists_recursive", ];
    assert_eq!(functions.len(), functions_names.len());

    let inputs = vec![ (vec![1,2,4], vec![1,3,4]), (vec![], vec![]), (vec![], vec![0]) ];
    let checks = vec![ vec![1,1,2,3,4,4], vec![], vec![0] ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in functions.iter().zip(functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for ((l1, l2), check) in inputs.iter().zip(checks.iter()) {
            println!("l1=({:?}), l2=({:?})", l1, l2);
            let n1 = ListNode::from_list(l1);
            let n2 = ListNode::from_list(l2);
            let result = f(n1, n2);
            let result_list = if result.is_some() {
                result.unwrap().to_list()
            } else {
                vec![]
            };
            println!("result_list=({:?})", result_list);
            assert_eq!(result_list, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

