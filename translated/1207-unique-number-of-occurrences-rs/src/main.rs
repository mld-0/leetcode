//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(unused)]
#![allow(non_snake_case)]

use std::time::Instant;
use std::collections::{HashSet,HashMap};
use counter::Counter;

//  macro: vec_of_strings
//  {{{
macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}
//  }}}

struct Solution {}

impl Solution {

    //  runtime: N/A (`Counter` not available)
    pub fn unique_occurences_Counter(arr: Vec<i32>) -> bool {
        let counts = arr.iter().collect::<Counter<_>>();
        let counts_set = counts.values().collect::<HashSet<_>>();
        if counts.values().len() == counts_set.len() {
            return true;
        }
        false
    }

    //  runtime: beats 100%
    pub fn unique_occurences(arr: Vec<i32>) -> bool {
        let mut counts: HashMap<i32,usize> = HashMap::new();
        for x in arr.iter() {
            if counts.contains_key(x) {
                *counts.get_mut(x).unwrap() += 1;
            } else {
                counts.insert(*x, 1);
            }
        }
        let counts_set = counts.values().collect::<HashSet<_>>();
        if counts.values().len() == counts_set.len() {
            return true;
        }
        false
    }

}

fn main() 
{
    let funcs: Vec<fn(Vec<i32>)->bool> = vec![ Solution::unique_occurences_Counter, Solution::unique_occurences ];
    let func_names = vec_of_strings![ "unique_occurences_Counter", "unique_occurences", ];
    assert_eq!(funcs.len(), func_names.len());

    let inputs = vec![ vec![1,2,2,1,1,3], vec![1,2], vec![-3,0,1,-3,1,1,1,-3,10,0], ];
    let checks = vec![ true, false, true, ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in funcs.iter().zip(func_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for (arr, check) in inputs.iter().zip(checks.iter()) {
            println!("arr=({:?})", arr);
            let result = f(arr.clone());
            println!("result=({})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

