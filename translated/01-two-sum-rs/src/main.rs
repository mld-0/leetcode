use std::collections::HashMap;

struct Solution {}

impl Solution {

    //  runtime: beats 100%
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

        //  num_to_index[nums[index]] = index
        let mut num_to_index = HashMap::<i32,usize>::new();

        for index in 0..nums.len() {
            let delta = target - nums[index];

            if num_to_index.contains_key(&delta) {
                return vec![ num_to_index.remove(&delta).unwrap() as i32, index as i32 ];
            }

            num_to_index.insert(nums[index], index);
        }

        vec![]
    }

}


fn main() 
{
    let test_functions = vec![ Solution::two_sum, ];
    let test_functions_names = vec![ "two_sum", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![ (vec![2,7,11,15], 9), (vec![3,2,4], 6), (vec![3,3], 6) ];
    let checks = vec![ [0,1], [1,2], [0,1] ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        for ((nums, target), check) in inputs.iter().zip(checks.iter()) {
            println!("nums=({:?}), target=({})", nums, target);
            let result = f(nums.clone(), target.clone());
            println!("result=({:?})", result);
            assert_eq!(result, Vec::from(*check), "Check comparison failed");
        }
    }
    println!();
}

