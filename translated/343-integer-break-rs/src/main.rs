use std::time::Instant;
use std::collections::HashMap;
use std::collections::HashSet;

struct Solution;

impl Solution {

    //  runtime: TLE
    pub fn integer_break_naive(n: i32) -> i32 {    
        let mut memoize = HashMap::<i32,Vec<Vec<i32>>>::new();

        fn sum_options(n: i32, memoize: &mut HashMap<i32,Vec<Vec<i32>>>) -> Vec<Vec<i32>> {
            if n == 0 { return vec![vec![]]; }
            if n == 1 { return vec![vec![1]]; }
            if memoize.contains_key(&n) {
                return memoize.get(&n).unwrap().clone();
            }
            let mut result = HashSet::<Vec<i32>>::new();
            for k in 1..=n {
                let remaining_options = sum_options(n-k, memoize);
                for mut option in remaining_options {
                    option.push(k);
                    option.sort();
                    result.insert(option);
                }
            }
            let mut result = result.into_iter().collect::<Vec<Vec<i32>>>();
            result.sort();
            memoize.insert(n, result.clone());
            result
        }

        let mut result = 0;
        let mut _result_option = vec![];
        let options = sum_options(n, &mut memoize);
        for option in options {
            if option.len() < 2 {
                continue;
            }
            let trial = option.iter().fold(1, |acc, &x| acc * x);
            if trial > result {
                result = trial;
                _result_option = option;
            }
        }
        result
    }


    //  runtime: beats 12%
    pub fn integer_break_naive_improved(n: i32) -> i32 {    
        let mut memoize = HashMap::<(i32,i32),Vec<Vec<i32>>>::new();

        fn sum_options(n: i32, last: i32, memoize: &mut HashMap<(i32, i32), Vec<Vec<i32>>>) -> Vec<Vec<i32>> {
            if n == 0 { return vec![vec![]]; }
            if n == 1 { return vec![vec![1]]; }
            if let Some(existing) = memoize.get(&(n, last)) {
                return existing.clone();
            }
            let mut result = Vec::new();
            for k in 1..=std::cmp::min(n, last) {
                let remaining_options = sum_options(n - k, k, memoize);
                for mut option in remaining_options {
                    option.push(k);
                    result.push(option);
                }
            }
            memoize.insert((n, last), result.clone());
            result
        }

        let mut result = 0;
        let mut _result_option = vec![];
        let options = sum_options(n, n, &mut memoize);
        for option in options {
            if option.len() < 2 {
                continue;
            }
            let trial = option.iter().fold(1, |acc, &x| acc * x);
            if trial > result {
                result = trial;
                _result_option = option;
            }
        }
        result
    }

    //  runtime: beats 100%
    pub fn integer_break_mathematical(n: i32) -> i32 {    
        let mut n = n;
        if n == 2 {
            return 1;
        }
        let mut option = Vec::<i32>::new();
        while n > 0 {
            if n == 6 {
                n -= 6;
                option.push(3);
                option.push(3);
            } else if n >= 5 {
                n -= 3;
                option.push(3);
            } else if n >= 2 {
                n -= 2;
                option.push(2);
            } else {
                n -= 1;
                option.push(1);
            }
        }
        return option.iter().fold(1, |acc, &x| acc * x);
    }

}


fn main() 
{
    let test_functions: Vec<fn(i32)->i32> = vec![ Solution::integer_break_naive, Solution::integer_break_naive_improved, Solution::integer_break_mathematical,  ];
    let test_functions_names = vec![ "integer_break_naive", "integer_break_naive_improved", "integer_break_mathematical", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![ 10, 2, 6, 12, 14, 15, 16, ];
    let checks = vec![ 36, 1, 9, 81, 162, 243, 324, ];
    assert_eq!(inputs.len(), checks.len());
    assert!(inputs.len() > 0);

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for (n, check) in inputs.iter().zip(checks.iter()) {
            println!("n=({:?})", n);
            let result = f(*n);
            println!("result=({:?})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

