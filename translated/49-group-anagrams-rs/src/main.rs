//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(unused)]
#![allow(non_snake_case)]

use std::collections::HashMap;
use std::iter::FromIterator;

//  macro: vec_of_strings
//  {{{
macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}
//  }}}

struct Solution {}

impl Solution {

    //  runtime: beats 96%
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut result = HashMap::<String,Vec<String>>::new();
        for s in strs {
            let mut s_sorted = s.clone();
            unsafe {
                s_sorted.as_bytes_mut().sort();
            }
            if result.contains_key(&s_sorted) {
                result.get_mut(&s_sorted).unwrap().push(s);
            } else {
                result.insert(s_sorted, vec![s]);
            }
        }
        Vec::from_iter(result.into_iter().map(|(k,v)| v))
    }

}


fn main() 
{
    let functions = vec![ Solution::group_anagrams, ];
    let function_names = vec_of_strings![ "group_anagrams", ];
    assert_eq!(functions.len(), function_names.len());

    let inputs = vec![ vec_of_strings!["eat","tea","tan","ate","nat","bat"], vec_of_strings![""], vec_of_strings!["a"], ];
    let checks = vec![ vec![vec_of_strings!["bat"],vec_of_strings!["nat","tan"],vec_of_strings!["ate","eat","tea"]], vec![vec_of_strings![""]], vec![vec_of_strings!["a"]], ];
    assert_eq!(inputs.len(), checks.len());

    fn check_result(result: &Vec<Vec<String>>, check: &Vec<Vec<String>>) {
        let mut temp1 = result.clone().iter_mut().map(|x| x.sort()).collect::<Vec<_>>();
        let mut temp2 = check.clone().iter_mut().map(|x| x.sort()).collect::<Vec<_>>();
        temp1.sort();
        temp2.sort();
        assert_eq!(temp1, temp2, "Check comparison failed");
    }

    for (f, f_name) in functions.iter().zip(function_names.iter()) {
        println!("{}", f_name);
        for (strs, check) in inputs.iter().zip(checks.iter()) {
            println!("strs=({:?})", strs);
            let result = f(strs.clone());
            println!("result=({:?})", result);
            check_result(&result, check);
        }
        println!();
    }
}

