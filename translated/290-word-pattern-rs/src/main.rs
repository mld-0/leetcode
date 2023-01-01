//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(unused)]
#![allow(non_snake_case)]

use std::collections::{HashSet,HashMap};

//  macro: vec_of_strings
//  {{{
macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}
//  }}}

struct Solution {}

impl Solution {

    //  runtime: beats 87%
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let letters = pattern.as_bytes();
        let words = s.split_whitespace().map(str::to_string).collect::<Vec<String>>();
        if letters.len() != words.len() {
            return false;
        }
        let mut letters_to_words = HashMap::<u8,String>::new();
        for (letter, word) in letters.iter().zip(words.iter()) {
            if letters_to_words.contains_key(letter) {
                if *letters_to_words.get(letter).unwrap() != *word {
                    return false;
                }
            } else {
                if letters_to_words.values().any(|x| *x == *word) {
                    return false;
                }
                letters_to_words.insert(*letter, word.clone());
            }
        }
        true
    }

}

fn main() 
{
    let funcs: Vec<fn(String,String)->bool> = vec![ Solution::word_pattern, ];
    let func_names = vec_of_strings![ "word_pattern", ];
    assert_eq!(funcs.len(), func_names.len());

    let inputs = vec![ ("abba", "dog cat cat dog"), ("abba", "dog cat cat fish"), ("aaaa", "dog cat cat dog"), ("abba", "dog dog dog dog"), ("aaa", "aa aa aa aa"), ];
    let checks = vec![ true, false, false, false, false, ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in funcs.iter().zip(func_names.iter()) {
        println!("{}", f_name);
        for ((pattern, s), check) in inputs.iter().zip(checks.iter()) {
            println!("pattern=({}), s=({})", pattern, s);
            let result = f(pattern.clone().to_string(), s.clone().to_string());
            println!("result=({})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!();
    }
}

