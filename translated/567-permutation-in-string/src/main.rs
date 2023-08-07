//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(non_snake_case)]

use std::time::Instant;

//  macros: vec_of_strings / tuple_of_strings
//  {{{
macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}
macro_rules! tuple_of_strings {
    ($($x:expr),*) => ( ( $($x.to_string()),* ) );
    ($($x:expr),+,) => ( tuple_of_strings!( $($x),* ) );
}
//  }}}

/// Problem: Return true if s2 contains a permutation of s1
/// (s1/s2 contain only [a-z])

struct Solution {}

impl Solution {

    //  runtime: beats 5%
    pub fn check_inclusion_Sorting(s1: String, s2: String) -> bool {
        fn sort_string_bytes(s: &str) -> String {
            let mut s_bytes = s.as_bytes().iter().cloned().collect::<Vec<_>>();
            s_bytes.sort();
            String::from_utf8(s_bytes).unwrap()
        }
        if s1.len() > s2.len() {
            return false;
        }
        let s1_sorted = sort_string_bytes(&s1);
        let R = ((s2.len() as isize) - (s1.len() as isize) + 1) as usize;
        for l in 0..R {
            let r = std::cmp::min(l+s1.len(), s2.len());
            if l >= r {
                break
            }
            let trial = sort_string_bytes(&s2[l..r]);
            if trial == s1_sorted {
                return true;
            }
        }
        false
    }


    //  runtime: beats 6%
    pub fn check_inclusion_Counter(s1: String, s2: String) -> bool {
        use std::collections::HashMap;
        fn count_string_bytes(s: &str) -> HashMap<u8,usize> {
            let mut result = HashMap::new();
            for c in s.as_bytes().iter() {
                if result.contains_key(c) {
                    *result.get_mut(c).unwrap() += 1;
                } else {
                    result.insert(*c, 1);
                }
            }
            result
        }
        if s1.len() > s2.len() {
            return false;
        }
        let s1_counts = count_string_bytes(&s1);
        let R = ((s2.len() as isize) - (s1.len() as isize) + 1) as usize;
        for l in 0..R {
            let r = std::cmp::min(l+s1.len(), s2.len());
            let trial = &s2[l..r];
            let trial_counts = count_string_bytes(trial);
            if trial_counts == s1_counts {
                return true;
            }
        }
        false
    }


    //  runtime: beats 42%
    pub fn check_inclusion_RollingCounter(s1: String, s2: String) -> bool {
        use std::collections::HashMap;
        fn count_string_bytes(s: &str) -> HashMap<u8,usize> {
            let mut result = HashMap::new();
            for c in s.as_bytes().iter() {
                if result.contains_key(c) {
                    *result.get_mut(c).unwrap() += 1;
                } else {
                    result.insert(*c, 1);
                }
            }
            result
        }
        if s1.len() > s2.len() {
            return false;
        }
        let s1_counts = count_string_bytes(&s1);
        let mut s2_window_counts = count_string_bytes(&s2[..s1.len()]);
        if s1_counts == s2_window_counts {
            return true;
        }
        let R = ((s2.len() as isize) - (s1.len() as isize) + 1) as usize;
        for i in 1..R {
            let l = s2.as_bytes()[i-1];                 //  character leaving window
            let r = s2.as_bytes()[i+s1.len()-1];        //  character entering window
            //  Update counter to new window:
            if s2_window_counts.contains_key(&r) {
                *s2_window_counts.get_mut(&r).unwrap() += 1; 
            } else {
                s2_window_counts.insert(r, 1);
            }
            *s2_window_counts.get_mut(&l).unwrap() -= 1;
            if *s2_window_counts.get(&l).unwrap() == 0 {
                s2_window_counts.remove(&l);
            }
            if s1_counts == s2_window_counts {
                return true;
            }
        }
        false
    }


    //  runtime: beats 100%
    pub fn check_inclusion_RollingListCounter(s1: String, s2: String) -> bool {
        if s1.len() > s2.len() {
            return false;
        }
        let mut s1_counts =  [0; 26];
        let mut s2_window_counts = [0; 26];
        for c in s1.as_bytes() {
            s1_counts[(*c as usize) - ('a' as usize)] += 1;
        }
        for i in 0..s1.len() {
            let c = s2.as_bytes()[i];
            s2_window_counts[(c as usize) - ('a' as usize)] += 1;
        }
        if s1_counts == s2_window_counts {
            return true;
        }
        let R = ((s2.len() as isize) - (s1.len() as isize) + 1) as usize;
        for i in 1..R {
            let l = s2.as_bytes()[i-1];
            let r = s2.as_bytes()[i+s1.len()-1];
            s2_window_counts[(r as usize) - ('a' as usize)] += 1;
            s2_window_counts[(l as usize) - ('a' as usize)] -= 1;
            if s1_counts == s2_window_counts {
                return true;
            }
        }
        false
    }

}


fn main()
{
    let functions: Vec<fn(String,String)->bool> = vec![ Solution::check_inclusion_Sorting, Solution::check_inclusion_Counter, Solution::check_inclusion_RollingCounter, Solution::check_inclusion_RollingListCounter, ];
    let functions_names = vec_of_strings![ "check_inclusion_Sorting", "check_inclusion_Counter", "check_inclusion_RollingCounter", "check_inclusion_RollingListCounter", ];
    assert_eq!(functions.len(), functions_names.len());

    let inputs = vec![ tuple_of_strings!("ab", "eidbaooo"), tuple_of_strings!("ab", "eidboaoo"), tuple_of_strings!("a", "ab"), tuple_of_strings!("horse", "ros"), tuple_of_strings!("adc", "dcda"), ];
    let checks = vec![ true, false, true, false, true, ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in functions.iter().zip(functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for ((s1, s2), check) in inputs.iter().zip(checks.iter()) {
            println!("s1=({}), s2=({})", s1, s2);
            let result = f(s1.clone(), s2.clone());
            println!("result=({})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

