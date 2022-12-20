//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(non_snake_case)]

macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}

//  Indexing a Rust string is slow (solutions using 's.chars().nth(i).unwap()' timeout)
//  (hence use of 'p = s.as_bytes()')

struct Solution;

impl Solution {

    //  runtime: TLE
    pub fn longestPalindrome_BruteForce(s: String) -> String {
        fn is_palindrome(s: &String) -> bool {
            s.eq(&s.chars().rev().collect::<String>())
        }
        let mut result = String::new();
        for i in 0 .. s.len() {
            for j in i+1 .. s.len()+1 {
                let loop_str = s.get(i..j).unwrap().to_string();
                if loop_str.len() > result.len() && is_palindrome(&loop_str) {
                    result = loop_str;
                }
            }
        }
        result
    }

    //  Runtime: beats 55%
    pub fn longestPalindrome_DP_BottomUp(s: String) -> String {
        let mut start: usize = 0;
        let mut end: usize = 0;
        let p = s.as_bytes();
        //  is_palindrome[i][j]: True if s[i:j+1] is a palindrome
        let mut is_palindrome = Vec::<Vec<bool>>::new();
        for _ in 0..s.len() { is_palindrome.push(vec![false; s.len()]); }
        //  All substrings of length 1 are palindromes
        for i in 0..s.len() {
            is_palindrome[i][i] = true;
        }
        //  Substrings of length 2 are palindromes if start/end letters match
        for i in 0..s.len()-1 {
            if p[i] == p[i+1] {
                is_palindrome[i][i+1] = true;
                start = i;
                end = i + 1;
            }
        }
        //  s[l:r+1] is a palindrome if s[l] == s[r] and is_palindrome[l+1][r-1] == True
        for r in 1..s.len() {
            for l in (0..r-1).rev() {
                if p[l] == p[r] && is_palindrome[l+1][r-1] {
                    is_palindrome[l][r] = true;
                    if r-l > end-start {
                        end = r;
                        start = l;
                    }
                }
            }
        }
        String::from(s.get(start..=end).unwrap())
    }

    //  runtime: beats 95%
    pub fn longestPalindrome_TwoPointers(s: String) -> String {
        let mut result_start = 0;
        let mut result_len = 1;
        let p = s.as_bytes();
        for i in 0..s.len() {
            let mut r = i;
            while r < s.len() && p[i] == p[r] {
                r += 1;
            }
            let mut l = (i as isize) - 1;
            while l >= 0 && r < s.len() && p[l as usize] == p[r] {
                l -= 1;
                r += 1;
            }
            let trial_len = (r as isize - l - 1) as usize;
            if trial_len > result_len {
                result_len = trial_len;
                result_start = (l + 1) as usize;
            }
        }
        String::from(s.get(result_start..result_start+result_len).unwrap())
    }

}


fn main() 
{
    let test_functions: Vec<fn(String)->String> = vec![ Solution::longestPalindrome_BruteForce, Solution::longestPalindrome_DP_BottomUp, Solution::longestPalindrome_TwoPointers, ];
    let test_functions_names = vec![ "longestPalindrome_BruteForce", "longestPalindrome_DP_BottomUp", "longestPalindrome_TwoPointers", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec_of_strings![ "debabec", "ceebababefd", "a", "ac", "bb", ];
    let checks = [ vec_of_strings!["ebabe"], vec_of_strings!["ebababe"], vec_of_strings!["a"], vec_of_strings![ "a", "c" ], vec_of_strings!["bb"], ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        for (text, check_list) in inputs.iter().zip(checks.iter()) {
            println!("text=({})", text);
            let result = f(text.clone());
            println!("result=({})", result);

            //  Ongoing: 2022-12-11T23:54:14AEDT A more elegant (Rust-ian) approach?
            let mut flag_check = false;
            for check in check_list {
                if result == check.clone() {
                    flag_check = true;
                }
            }
            assert!(flag_check);

        }
        println!();
    }
}

