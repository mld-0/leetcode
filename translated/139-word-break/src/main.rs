//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(non_snake_case)]

use std::time::Instant;
use std::collections::{HashSet, HashMap, VecDeque};

struct Solution {}

/// Problem: determine whether string `s` can be constructed from words in `wordDict`
impl Solution {

    //  runtime: beats 100%
    pub fn word_break_DP_TopDown(s: String, word_dict: Vec<String>) -> bool {        
        let word_set = word_dict.into_iter().collect::<HashSet<String>>();
        let mut memoize: HashMap<usize,bool> = HashMap::new();

        fn solve(l: usize, s: &str, word_set: &HashSet<String>, memoize: &mut HashMap<usize,bool>) -> bool {
            if memoize.contains_key(&l) {
                return memoize[&l];
            }
            if l == s.len() {
                memoize.insert(l, true);
                return true;
            }
            for r in l..s.len() {
                if word_set.contains(&s[l..=r]) {
                    if solve(r+1, s, word_set, memoize) {
                        memoize.insert(l, true);
                        return true;
                    }
                }
            }
            memoize.insert(l, false);
            false
        }

        solve(0, &s, &word_set, &mut memoize)
    }


    //  runtime: beats 100%
    pub fn word_break_DP_BottomUp(s: String, word_dict: Vec<String>) -> bool {        
        let word_set = word_dict.into_iter().collect::<HashSet<String>>();

        //  table[i]: True if `s[:i+1]` can be comprised of strings from `wordDict` 
        let mut table: Vec<bool> = vec![false; s.len()+1];
        //  base case: empty string can be created from word_dict
        table[0] = true;

        for r in 0..s.len() {
            for l in 0..=r {
                if table[l] && word_set.contains(&s[l..=r]) {
                    table[r+1] = true;
                    break;
                }
            }
        }

        table[table.len()-1]
    }


    //  runtime: beats 100%
    pub fn word_break_BFS(s: String, word_dict: Vec<String>) -> bool {        
        let word_set = word_dict.into_iter().collect::<HashSet<String>>();
        let mut queue = VecDeque::new();
        let mut visited = HashSet::new();
        queue.push_back(0);

        while !queue.is_empty() {
            let l = queue.pop_front().unwrap();
            if visited.contains(&l) {
                continue;
            }
            for r in l..s.len() {
                if word_set.contains(&s[l..=r]) {
                    queue.push_back(r+1);
                    if r == s.len()-1 {
                        return true;
                    }
                }
            }
            visited.insert(l);
        }

        false
    }

}


fn main() 
{
    let test_functions: Vec<fn(String,Vec<String>)->bool> = 
        vec![ Solution::word_break_DP_TopDown, Solution::word_break_DP_BottomUp, Solution::word_break_BFS, ];
    let test_functions_names = vec![ "word_break_DP_TopDown", "word_break_DP_BottomUp", "word_break_BFS", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![ ("leetcode",vec!["leet","code"]),("applepenapple",vec!["apple","pen"]),("catsandog",vec!["cats","dog","sand","and","cat"]),("a",vec!["a"]), ("aaaaaaa",vec!["aaaa","aaa"]), ];
    let checks = vec![ true, true, false, true, true, ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for ((s, word_dict), check) in inputs.iter().zip(checks.iter()) {
            let s = s.to_string();
            let word_dict = word_dict.into_iter().map(|x| x.to_string()).collect();
            println!("s=({}), word_dict=({:?})", s, word_dict);
            let result = f(s, word_dict);
            println!("result=({})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

