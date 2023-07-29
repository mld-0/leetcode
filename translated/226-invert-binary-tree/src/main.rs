//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
pub mod bstreenode;
use crate::bstreenode::TreeNode;

use std::time::Instant;
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

struct Solution {}

impl Solution {

    //  runtime: beats 100%
    pub fn invert_tree_recursive(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() {
            return None
        }
        if let Some(node) = root.clone() {
            let l = node.borrow_mut().left.take();
            let r = node.borrow_mut().right.take();
            node.borrow_mut().left = r;
            node.borrow_mut().right = l;
            Self::invert_tree_recursive(node.borrow_mut().left.clone());
            Self::invert_tree_recursive(node.borrow_mut().right.clone());
        }
        root
    }

    //  runtime: beats 100%
    pub fn invert_tree_iterative(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() {
            return None;
        }
        let mut queue = VecDeque::new();
        queue.push_back(root.clone());
        while !queue.is_empty() {
            let current = queue.pop_front().unwrap();
            if let Some(node) = current.clone() {
                let l = node.borrow_mut().left.take();
                let r = node.borrow_mut().right.take();
                node.borrow_mut().left = r;
                node.borrow_mut().right = l;
                if node.borrow().left.is_some() {
                    queue.push_back(node.borrow().left.clone());
                }
                if node.borrow().right.is_some() {
                    queue.push_back(node.borrow().right.clone());
                }
            }
        }
        root
    }
}

fn main() 
{
    let test_functions: Vec<fn(Option<Rc<RefCell<TreeNode>>>)->Option<Rc<RefCell<TreeNode>>>> = 
        vec![ Solution::invert_tree_recursive, Solution::invert_tree_iterative, ];
    let test_functions_names = vec![ "invert_tree_recursive", "invert_tree_iterative", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![ vec![4,2,7,1,3,6,9], vec![2,1,3], vec![], ];
    let checks = vec![ vec![4,7,2,9,6,3,1], vec![2,3,1], vec![], ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for (vals, check) in inputs.iter().zip(checks.iter()) {
            let vals = vals.into_iter().map(|x| Some(x.clone())).collect::<Vec<Option<i32>>>();
            let check = check.into_iter().map(|x| Some(x.clone())).collect::<Vec<Option<i32>>>();
            let root = TreeNode::from_list(&TreeNode::fill_list_infer_missing(&vals));
            if root.is_some() {
                println!("root:\n{}", root.as_ref().unwrap().borrow().to_string());
            } else {
                println!("root:\nNone");
            }
            let result = f(root);
            if result.is_some() {
                println!("result:\n{}", result.as_ref().unwrap().borrow().to_string());
                let result_vals = result.as_ref().map_or(vec![], |x| x.borrow().to_list());
                assert_eq!(result_vals, *check, "Check comparison failed");
            } else {
                println!("result:\nNone");
                assert_eq!(check.len(), 0)
            }
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

