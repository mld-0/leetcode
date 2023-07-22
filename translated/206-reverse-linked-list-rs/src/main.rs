
use std::time::Instant;

pub mod listnode;
use crate::listnode::listnode::ListNode;


struct Solution;

impl Solution {

    //    #       runtime: beats 39%
    //    def reverseList_Iterative(self, head):
    //        if head is None:
    //            return None
    //        elements = []
    //        node = head
    //        while node is not None:
    //            elements.append(node.val)
    //            node = node.next
    //        elements = elements[::-1]
    //        result = ListNode()
    //        node = result
    //        previous = node
    //        for i in elements:
    //            node.val = i
    //            node.next = ListNode()
    //            previous = node
    //            node = node.next
    //        previous.next = None
    //        return result
    pub fn reverse_list_iterative(_head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {        
        unimplemented!();
    }


    //    let mut result: Vec<*mut Option<Box<ListNode>>> = vec![];
    //    unsafe {
    //        let mut raw_node = &mut head as *mut Option<Box<ListNode>>;
    //        while let Some(node) = raw_node.as_mut().unwrap().as_mut() {
    //            result.push(raw_node);
    //            raw_node = &mut node.next as *mut _;
    //        }
    //    }
    //if head.is_none() {
    //    return None;
    //}
    //unsafe {
    //    let mut curr: *mut ListNode = head.as_deref_mut().unwrap();
    //    let mut prev: *mut ListNode = 0 as *mut _;
    //    while !curr.is_null() {
    //        //let x = (*curr).next;
    //    }
    //}
    pub fn reverse_list_inplace_pointers(_head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {        
        unimplemented!();
    }


    //  runtime: beats 100%
    pub fn reverse_list_inplace(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {        
        let mut curr = head;
        let mut prev = None;
        while let Some(mut n) = curr {
            curr = n.next;
            n.next = prev;
            prev = Some(n);
        }
        prev
    }

 
    //  runtime: beats 100%
    pub fn reverse_list_recursive(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {        
        fn solve(head: Option<Box<ListNode>>, mut r: Option<Box<ListNode>>) 
            -> Option<Box<ListNode>> 
        {
            if head.is_none() {
                return r;
            }
            if r.is_none() {
                r = Some(Box::new(ListNode { val: head.as_ref().unwrap().val, next: None }));
                return solve(head.unwrap().next, r);
            }
            r = Some(Box::new(ListNode { val: head.as_ref().unwrap().val, next: r }));
            return solve(head.unwrap().next, r);
        }
        solve(head, None)
    }


    //  runtime: beats 100%
    pub fn reverse_list_recursive_inplace(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {        
        fn solve(mut current: Option<Box<ListNode>>, tail: Option<Box<ListNode>>) 
            -> Option<Box<ListNode>> 
        {
            match current {
                Some(mut node) => {
                    current = node.next.take();
                    node.next = tail;
                    solve(current, Some(node))
                }
                None => tail,
            }
        }
        solve(head, None)
    }

}


fn main() 
{
    let _test_functions: Vec<fn(Option<Box<ListNode>>)->Option<Box<ListNode>>> = vec![ Solution::reverse_list_iterative, Solution::reverse_list_inplace_pointers, Solution::reverse_list_inplace, Solution::reverse_list_recursive, Solution::reverse_list_recursive_inplace, ];
    let _test_functions_names = vec![ "reverse_list_iterative", "reverse_list_inplace_pointers", "reverse_list_inplace", "reverse_list_recursive", "reverse_list_recursive_inplace", ];

   let test_functions: Vec<fn(Option<Box<ListNode>>)->Option<Box<ListNode>>> = vec![ Solution::reverse_list_inplace, Solution::reverse_list_recursive, Solution::reverse_list_recursive_inplace, ];
   let test_functions_names = vec![ "reverse_list_inplace", "reverse_list_recursive", "reverse_list_recursive_inplace", ];

    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![ vec![1,2,3,4,5], vec![1,2], vec![] ];
    let checks = vec![ vec![5,4,3,2,1], vec![2,1], vec![] ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for (vals, check_vals) in inputs.iter().zip(checks.iter()) {
            println!("vals=({:?})", vals);
            let vals_head = ListNode::from_list(vals);

            let result_head = f(vals_head);
            let result_vals = result_head.as_ref().map_or(vec![], |h| h.to_list());

            println!("result_head=({:?})", result_head);
            println!("result_vals=({:?})", result_vals);

            assert_eq!(result_vals, *check_vals, "Check comparison failed");

            //  Comparing result_head vs result_vals?
            //let check_head = ListNode::from_list(check_vals);
            //assert_eq!(result_head, check_head, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

