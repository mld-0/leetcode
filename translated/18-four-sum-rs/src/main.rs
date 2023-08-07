//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(non_snake_case)]

use std::time::Instant;
use std::collections::HashMap;

//  Continue: 2022-12-27T18:22:55AEST 'fourSum_kSumMap_Unsorted' solution

//  macro: vec_of_strings
//  {{{
macro_rules! vec_of_strings {
    ($($x:expr),*) => ( vec![$($x.to_string()),*] );
    ($($x:expr),+,) => ( vec_of_strings![ $($x),* ] );
}
//  }}}

struct Solution {}

impl Solution {

    //  runtime: beats 99%
    pub fn fourSum_kSumTwoPointers(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {

        fn kSum(nums: &[i32], target: i64, k: i64) -> Vec<Vec<i32>> {
            let mut result: Vec<Vec<i32>> = vec![];
            if nums.len() == 0 {
                return result;
            }
            let avg = (target / k) as i32;
            if nums[0] > avg || nums[nums.len()-1] < avg {
                return result;
            }
            if k == 2 {
                return twoSum_TwoPointers(nums, target as i32);
            }
            for i in 0..nums.len() {
                if i > 0 && nums[i] == nums[i-1] {
                    continue;
                }
                let partialSolutions = kSum(&nums[i+1..], (target as i64) - (nums[i] as i64), k-1);
                for subset in partialSolutions.into_iter() {
                    let mut temp_values: Vec<i32> = vec![ nums[i] ];
                    temp_values.extend(subset);
                    result.push( temp_values );
                }
            }
            result
        }

        fn twoSum_TwoPointers(nums: &[i32], target: i32) -> Vec<Vec<i32>> {
            let mut result: Vec<Vec<i32>> = vec![];
            let mut l = 0;
            let mut r = nums.len() - 1;
            while l < r {
                let trial = nums[l] + nums[r];
                if trial < target || (l > 0 && nums[l] == nums[l-1]) {
                    l += 1;
                } else if trial > target || (r < nums.len()-1 && nums[r] == nums[r+1]) {
                    r -= 1;
                } else {
                    result.push( vec![ nums[l], nums[r] ] );
                    l += 1;
                    r -= 1;
                }
            }
            result
        }

        nums.sort();
        kSum(&nums, target as i64, 4)
    }


    //  runtime: beats 80%
    pub fn fourSum_kSumMap(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {

        fn kSum(nums: &[i32], target: i64, k: i64) -> Vec<Vec<i32>> {
            let mut result: Vec<Vec<i32>> = vec![];
            if nums.len() == 0 {
                return result;
            }
            let avg = (target / k) as i32;
            if nums[0] > avg || nums[nums.len()-1] < avg {
                return result;
            }
            if k == 2 {
                return twoSum_Map(nums, target as i32);
            }
            for i in 0..nums.len() {
                if i > 0 && nums[i] == nums[i-1] {
                    continue;
                }
                let partialSolutions = kSum(&nums[i+1..], (target as i64) - (nums[i] as i64), k-1);
                for subset in partialSolutions.into_iter() {
                    let mut temp_values: Vec<i32> = vec![ nums[i] ];
                    temp_values.extend(subset);
                    result.push( temp_values );
                }
            }
            result
        }

        fn twoSum_Map(nums: &[i32], target: i32) -> Vec<Vec<i32>> {
            let mut result: Vec<Vec<i32>> = vec![];
            //  num_to_index[nums[index]] = index
            let mut num_to_index: HashMap<i32,usize> = HashMap::new();
            for (i, x) in nums.iter().enumerate() {
                if result.len() > 0 && result[result.len()-1][1] == *x {
                    continue;
                }
                let delta = target - x;
                if num_to_index.contains_key(&delta) {
                    result.push( vec![ delta, *x ] );
                }
                num_to_index.insert(*x, i);
            }
            result
        }

        nums.sort();
        kSum(&nums, target as i64, 4)
    }


    pub fn fourSum_kSumMap_Unsorted(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        unimplemented!();
    }

}


fn main() 
{
    let test_functions: Vec<fn(Vec<i32>,i32)->Vec<Vec<i32>>> = vec![ Solution::fourSum_kSumTwoPointers, Solution::fourSum_kSumMap, ];
    let test_functions_names = vec_of_strings![ "fourSum_kSumTwoPointers", "fourSum_kSumMap", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs: Vec<(Vec<i32>, i32)> = vec![ (vec![1,0,-1,0,-2,2], 0), (vec![2,2,2,2,2], 8), (vec![1,0,-1,0,-2,2], 0), (vec![-1000000000,-1000000000,1000000000,-1000000000,-1000000000],
    294967296), ];
    let checks: Vec<Vec<Vec<i32>>> = vec![ vec![vec![-2,-1,1,2],vec![-2,0,0,2],vec![-1,0,0,1]], vec![vec![2,2,2,2]], vec![vec![-2,-1,1,2],vec![-2,0,0,2],vec![-1,0,0,1]], vec![], ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for ((nums, target), check) in inputs.iter().zip(checks.iter()) {
            println!("nums=({:?}), target=({})", nums, target);
            let result = f(nums.clone(), *target);
            println!("result=({:?})", result);
            assert!(result.iter().all(|x| check.contains(&x)));
            assert!(check.iter().all(|x| result.contains(&x)));
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }

}

