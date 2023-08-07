//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(non_snake_case)]

use std::time::Instant;
use std::collections::{HashSet, HashMap, VecDeque};

/// For a graph, return a (sorted) list of 'safe nodes'
/// A node is safe if all possible paths from that node lead only to terminal nodes or other safe nodes
/// A terminal node is a node with no outgoing edges

struct Solution {}

impl Solution {

    //  runtime: beats 23%
    pub fn eventual_safe_nodes_DFSCycleCheck(graph: Vec<Vec<i32>>) -> Vec<i32> {        
        let mut result = HashSet::new();
        let mut memoize = HashMap::new();

        fn contains_cycle(node: i32, graph: &Vec<Vec<i32>>, result: &mut HashSet<i32>, seen: &mut HashSet<i32>, memoize: &mut HashMap<i32,bool>) -> bool {
            if memoize.contains_key(&node) {
                return *memoize.get(&node).unwrap();
            }
            if seen.contains(&node) {
                memoize.insert(node, true);
                return true;
            }
            seen.insert(node);
            for n in &graph[node as usize] {
                if result.contains(&n) {
                    continue;
                }
                if contains_cycle(*n, graph, result, seen, memoize) {
                    memoize.insert(*n, true);
                    return true;
                }
            }
            seen.remove(&node);
            memoize.insert(node, false);
            false
        }

        for i in 0..graph.len() {
            let mut seen = HashSet::new();
            if !contains_cycle(i as i32, &graph, &mut result, &mut seen, &mut memoize) {
                result.insert(i as i32);
            }
        }
        let mut result: Vec<_> = result.into_iter().collect();
        result.sort();
        result
    }


    //  runtime: beats 98%
    pub fn eventual_safe_nodes_DFSCycleCheck_gpt4optimised(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = Vec::new();
        // 0 = not visited, 1 = visiting, 2 = visited & has cycle, 3 = visited & safe
        let mut memoize = vec![0; graph.len()]; 

        fn contains_cycle(node: usize, graph: &Vec<Vec<i32>>, memoize: &mut Vec<u8>) -> bool {
            match memoize[node] {
                1 => return true,   // We're currently visiting this node, so we found a cycle
                2 => return true,   // We've visited this node before and know it's part of a cycle
                3 => return false,  // We've visited this node before and know it's safe
                _ => {}
            }
            memoize[node] = 1; // Mark as currently visiting
            for &neighbour in &graph[node] {
                if contains_cycle(neighbour as usize, graph, memoize) {
                    memoize[node] = 2; // This node is part of a cycle
                    return true;
                }
            }
            memoize[node] = 3; // This node is safe
            false
        }

        for i in 0..graph.len() {
            if !contains_cycle(i, &graph, &mut memoize) {
                result.push(i as i32);
            }
        }
        result
    }


    //  runtime: TLE
    pub fn eventual_safe_nodes_BFSCycleCheck(graph: Vec<Vec<i32>>) -> Vec<i32> {        
        let mut result = HashSet::new();

        fn contains_cycle(node: i32, graph: &Vec<Vec<i32>>, result: &mut HashSet<i32>) -> bool {
            let mut queue = VecDeque::new();
            let seen: HashSet<i32> = HashSet::new();
            queue.push_back( (node, seen.clone()) );
            while !queue.is_empty() {
                let (current, mut seen) = queue.pop_front().unwrap();
                if seen.contains(&current) {
                    return true;
                }
                if result.contains(&current) {
                    continue;
                }
                seen.insert(current);
                for n in &graph[current as usize] {
                    if result.contains(&n) {
                        continue;
                    }
                    queue.push_back( (*n, seen.clone()) );
                }
                seen.remove(&current);
            }
            false
        }

        for i in 0..graph.len() {
            if !contains_cycle(i as i32, &graph, &mut result) {
                result.insert(i as i32);
            }
        }
        let mut result: Vec<_> = result.into_iter().collect();
        result.sort();
        result
    }


    //  runtime: beats 90%
    pub fn eventual_safe_nodes_ans_TopologicalSort_KahnsAlgorithm(graph: Vec<Vec<i32>>) -> Vec<i32> {                
        let num_nodes = graph.len();
        let mut graph_invert = vec![ vec![]; num_nodes ];
        let mut graph_in_edges = vec![ 0; num_nodes ];

        //  Invert the graph, and count the number of edges going into each node for the non-inverted graph
        for src in 0..num_nodes {
            for dest in &graph[src] {
                graph_invert[*dest as usize].push(src);
                graph_in_edges[src] += 1;
            }
        }

        let mut result = vec![];
        let mut queue = VecDeque::new();

        //  Add all terminal nodes to the queue
        for n in 0..num_nodes {
            if graph_in_edges[n] == 0 {
                queue.push_back(n);
            }
        }

        //  Iteratively remove terminal nodes (those with no remaining in_edges) from the graph
        //  The only nodes left in the origional graph (nodes not in `result`) are either in a cycle, or lead to a node in a cycle
        while !queue.is_empty() {
            let current = queue.pop_front().unwrap();
            result.push(current as i32);
            for n in &graph_invert[current as usize] {
                graph_in_edges[*n as usize] -= 1;
                if graph_in_edges[*n as usize] == 0 {
                    queue.push_back(*n);
                }
            }
        }

        result.sort();
        result
    }

}


fn main() 
{
    let test_functions: Vec<fn(Vec<Vec<i32>>)->Vec<i32>> = 
        vec![ Solution::eventual_safe_nodes_DFSCycleCheck, Solution::eventual_safe_nodes_DFSCycleCheck_gpt4optimised,  Solution::eventual_safe_nodes_BFSCycleCheck, Solution::eventual_safe_nodes_ans_TopologicalSort_KahnsAlgorithm, ];
    let test_functions_names = vec![ "eventual_safe_nodes_DFSCycleCheck", "eventual_safe_nodes_DFSCycleCheck_gpt4optimised", "eventual_safe_nodes_BFSCycleCheck", "eventual_safe_nodes_ans_TopologicalSort_KahnsAlgorithm", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![ vec![vec![1,2],vec![2,3],vec![5],vec![0],vec![5],vec![],vec![]], vec![vec![1,2,3,4],vec![1,2],vec![3,4],vec![0,4],vec![]], vec![vec![],vec![0,2,3,4],vec![3],vec![4],vec![]], ];
    let checks = vec![ vec![2,4,5,6], vec![4], vec![0,1,2,3,4], ];
    assert_eq!(inputs.len(), checks.len());

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        let now = Instant::now();
        for (graph, check) in inputs.iter().zip(checks.iter()) {
            println!("graph=({:?})", graph);
            let result = f(graph.clone());
            println!("result=({:?})", result);
            assert_eq!(result, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}


