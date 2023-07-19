
use std::time::Instant;
use std::collections::HashSet;

struct Solution;

impl Solution {

    //  runtime: TLE
    pub fn erase_overlap_intervals_i(mut intervals: Vec<Vec<i32>>) -> i32 {
        let initial_len = intervals.len();
        intervals.sort();
        let mut i = 1;
        while i < intervals.len() {
            let a = &intervals[i-1];
            let b = &intervals[i];
            if b[0] < a[1] {
                if b[1] < a[1] {
                    intervals.remove(i-1);
                } else {
                    intervals.remove(i);
                }
            } else {
                i += 1;
            }
        }
        (initial_len - intervals.len()) as i32
    }

    //  runtime: beats 5%
    pub fn erase_overlap_intervals_ii(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort();
        let mut removed = HashSet::new();
        let mut i = 1;
        while i < intervals.len() {
            let mut l = i-1;
            while removed.contains(&l) { 
                l -= 1;
            }
            let mut r = i;
            while removed.contains(&r) {
                r -= 1;
            }
            let a = &intervals[l];
            let b = &intervals[r];
            if b[0] < a[1] {
                if b[1] < a[1] {
                    removed.insert(l);
                } else {
                    removed.insert(r);
                }
            }
            i += 1;
        }
        removed.len() as i32
    }

    //  runtime: beats 87%
    pub fn erase_overlap_intervals_ans(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by_key(|x| x[1]);
        let mut included_intervals = HashSet::new();
        let mut most_recent_end_time = i32::MIN;
        for (i, start_and_end) in intervals.iter().enumerate() {
            let start = start_and_end[0];
            let end = start_and_end[1];
            if start >= most_recent_end_time {
                most_recent_end_time = end;
                included_intervals.insert(i);
            }
        }
        (intervals.len() - included_intervals.len()) as i32 
    }

}


fn main() 
{
    let test_functions: Vec<fn(Vec<Vec<i32>>)->i32> = vec![ Solution::erase_overlap_intervals_i, Solution::erase_overlap_intervals_ii, Solution::erase_overlap_intervals_ans, ];
    let test_functions_names = vec![ "erase_overlap_intervals_i", "erase_overlap_intervals_ii", "erase_overlap_intervals_ans", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![  vec![vec![1,2],vec![2,3],vec![3,4],vec![1,3]], 
                        vec![vec![1,2],vec![1,2],vec![1,2]], 
                        vec![vec![1,2],vec![2,3]], 
                        vec![vec![1,100],vec![11,22],vec![1,11],vec![2,12]], 
                        vec![vec![-52,31],vec![-73,-26],vec![82,97],vec![-65,-11],vec![-62,-49],vec![95,99],vec![58,95],vec![-31,49],vec![66,98],vec![-63,2],vec![30,47],vec![-40,-26]], ];
    let checks = vec![ 1, 2, 0, 2, 7, ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for (interval, check) in inputs.iter().zip(checks.iter()) {
            println!("interval=({:?})", interval);
            let result = f(interval.clone());
            println!("result=({:?})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

