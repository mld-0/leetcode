//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
#![allow(unused)]
#![allow(non_snake_case)]
//  Ongoings:
//  {{{
//  Ongoing: 2023-01-19T22:13:52AEDT 'fill_list_infer_missing()' -> vector 'result' is not prefilled, we do not use 'result[loop_level] = loop_nodes' -> are we assigning to correct level (every time) by using 'Vec::push()' each time(?)
//  Ongoing: 2023-01-20T19:00:51AEDT '_buildTreeFromNestedValuesList()' without unsafe/raw-pointers(?)
//  Ongoing: 2023-01-20T19:55:32AEDT '_tree_toNestedNodesList()' without using unsafe/raw-pointers (how to get a reference from a RefCell that lasts longer than the scope of the the 'Ref' returned by 'RefCell::borrow()'?)
//  Ongoing: 2023-01-20T21:52:17AEDT further debugging needed? (passes tests from python version - already had to debug pointer usage (to the point where one is unwilling to bet this all 'just works'))
//  }}}

//  LINK: https://rust-unofficial.github.io/too-many-lists/index.html

//  Continue: 2023-01-19T22:13:16AEDT macro, 'debug!()'
//  Continue: 2023-01-20T21:51:54AEDT implementation without unsafe/raw-pointers
//  Continue: 2023-01-20T21:53:22AEDT implement 'to_string()' / 'to_string_helper()' 
//  Continue: 2023-01-20T21:54:37AEDT review (after) 'Learn Rust With Entirely Too Many Linked Lists'

//  macro: get_func_name!()
//  {{{
macro_rules! get_func_name {
    () => {{
        fn f() {}
        fn type_name_of<T>(_: T) -> &'static str {
            std::any::type_name::<T>()
        }
        let name = type_name_of(f);
        // Find and cut the rest of the path
        match &name[..name.len() - 3].rfind(':') {
            Some(pos) => &name[pos + 1..name.len() - 3],
            None => &name[..name.len() - 3],
        }
    }};
}
//  }}}
use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode { val, left: None, right: None }
    }

//   Create Binary tree from list containing nodes values in breadth-first order. None represents an empty node. Lists that have non-None children of empty nodes are invalid.
    pub fn from_list(values: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>>
    {
        if values.len() == 0 {
            return None;
        }
        let tree_nestedValues = Self::_splitListToNestedValuesList(values);
        let head = Self::_buildTreeFromNestedValuesList(tree_nestedValues);
        head
    }

    pub fn to_list_nested(&self) -> Vec<Vec<Option<i32>>> 
    {
        let tree_nestedNodes = self._tree_toNestedNodesList();
        let mut tree_nestedValues = vec![];
        for x in tree_nestedNodes {
            let mut temp = vec![];
            for y in x {
                if y.is_none() {
                    temp.push(None)
                } else {
                    let val = y.unwrap().val;
                    temp.push(Some(val));
                }
            }
            tree_nestedValues.push(temp);
        }
        tree_nestedValues
    }

    pub fn to_list(&self) -> Vec<Option<i32>> 
    {
        let tree_nestedValues = self.to_list_nested();
        let mut result = vec![];
        for x in tree_nestedValues {
            for y in x {
                result.push(y);
            }
        }
        result
    }

//  Convert tree-as-list as given for leetcode input to format acceptable for 'from_list()' (by filling in missing None children of None parents)
    pub fn fill_list_infer_missing(vals: &[Option<i32>]) -> Vec<Option<i32>> 
    {
        let mut values: Vec<Option<i32>> = vals.iter().cloned().collect();
        if values.len() == 0 {
            return vec![]
        }
        let tree_levels_count = Self::_listLevelsCountWhenNested(&values);
        println!("tree_levels_count=({:?})", tree_levels_count);
        for i in values.len()..(2_usize.pow(tree_levels_count as u32)) {
            values.push(None);
        }
        let mut result = Vec::<Vec<Option<i32>>>::new();
        //  {{{
        //for _ in 0..tree_levels_count {
        //    result.push( vec![] );
        //}
        //result[0].push( values[0] );
        //  }}}
        result.push( vec![ values[0] ] );
        let mut z = 1;
        for loop_level in 1..(tree_levels_count as usize) {
            let mut loop_nodes = Vec::<Option<i32>>::new();
            let parent_level = &result[loop_level-1];
            for x in parent_level {
                if x.is_some() {
                    loop_nodes.push(values[z]);
                    z += 1;
                    loop_nodes.push(values[z]);
                    z += 1;
                } else {
                    loop_nodes.push(None);
                    loop_nodes.push(None);
                }
            }
            result.push(loop_nodes);
        }
        println!("result=({:?})", result);
        let mut result_flat = Vec::<Option<i32>>::new();
        for level in result {
            for val in level {
                result_flat.push(val);
            }
        }
        println!("result_flat=({:?})", result_flat);
        result_flat
    }

    pub fn max_depth(&self) -> usize {
        let L = &self.left;
        let R = &self.right;
        let l = Self::_max_depth(L);
        let r = Self::_max_depth(R);
        std::cmp::max(l,r) + 1
    }

    fn _max_depth(root: &Option<Rc<RefCell<TreeNode>>>) -> usize
    {
        if root.is_none() {
            return 0;
        }
        let L = &root.as_ref().unwrap().as_ref().borrow().left;
        let R = &root.as_ref().unwrap().as_ref().borrow().right;
        let l = Self::_max_depth(L);
        let r = Self::_max_depth(R);
        std::cmp::max(l, r) + 1
    }

//  Split 'values' into a list of lists, each inner list corresponding to a level in the tree, eg: [1,3,2,5] becomes [ [1], [3,2], [5,None,None,None] ]
    pub fn _splitListToNestedValuesList(values: &[Option<i32>]) -> Vec<Vec<Option<i32>>>
    {
        let tree_levels_count = Self::_listLevelsCountWhenNested(values);
        let mut z: usize = 0;
        let mut tree_nestedValues = Vec::<Vec<Option<i32>>>::new();
        for loop_level in 0..(tree_levels_count as usize) {
            let mut loop_vals = Vec::<Option<i32>>::new();;
            for j in 0..2_usize.pow(loop_level as u32) {
                let val = if values.len() > z {
                    z += 1;
                    values[z-1]
                } else {
                    None
                };
                loop_vals.push(val);
            }
            tree_nestedValues.push(loop_vals);
        }
        assert_eq!(tree_nestedValues.len(), tree_levels_count);
        tree_nestedValues
    }

//  Given flat list, how many levels of nested list / tree are necessary to represent it
    pub fn _listLevelsCountWhenNested(values: &[Option<i32>]) -> usize 
    {
        let mut tree_levels_count: usize = 0;
        while 2_usize.pow(tree_levels_count as u32) <= values.len() {
            tree_levels_count += 1;
        }
        tree_levels_count
    }

//  Create tree from given nested list of values, returning nested list of the nodes of that tree"""
    pub fn _buildTreeFromNestedValuesList(tree_nestedValues: Vec<Vec<Option<i32>>>) -> Option<Rc<RefCell<TreeNode>>>
    {
        if tree_nestedValues.len() < 1 || tree_nestedValues[0].len() < 1 {
            panic!("Must pass at nested Vec of at least 1 element");
        }
        if tree_nestedValues[0][0].is_none() {
            panic!("First element cannot be 'None'");
        }
        let node = Self { val: tree_nestedValues[0][0].unwrap(), left: None, right: None, };
        let mut head = Some(Rc::new(RefCell::new(node)));
        let mut tree_nestedNodes: Vec<Vec<*mut Option<Rc<RefCell<TreeNode>>>>> = vec![ vec![ &mut head as *mut Option<Rc<RefCell<TreeNode>>> ] ];
        let mut _none: Option<Rc<RefCell<TreeNode>>> = None;
        for loop_level in 1..tree_nestedValues.len() {
            let mut loop_nodes: Vec<*mut Option<Rc<RefCell<TreeNode>>>> = vec![];
            for (j, val) in tree_nestedValues[loop_level].iter().enumerate() {
                let parent_node = tree_nestedNodes[loop_level-1][j/2];
                let parent_val = tree_nestedValues[loop_level-1][j/2];
                //  None indicates missing node
                if val.is_none() {
                    loop_nodes.push(&mut _none as *mut Option<Rc<RefCell<TreeNode>>>);
                    continue;
                }
                if unsafe { parent_node.as_ref().is_none() } {
                    panic!("Invalid list: Unable to create non-null child for null parent\nloop_level=({:?}), j=({:?}), tree_nestedValues=({:?})", loop_level, j, tree_nestedValues);
                }
                let mut new_node = if val.is_none() {
                    None
                } else {
                    Some(Rc::new(RefCell::new( Self { val: val.as_ref().unwrap().clone(), left: None, right: None } )))
                };
                if j % 2 == 0 {
                    println!("({:?}).L=({:?})", parent_val, val);
                    unsafe { (*(*parent_node).as_ref().unwrap().as_ptr()).left = new_node; }
                    unsafe { loop_nodes.push( &mut (*(*parent_node).as_ref().unwrap().as_ptr()).left as *mut Option<Rc<RefCell<TreeNode>>>); };
                } else {
                    println!("({:?}).R=({:?})", parent_val, val);
                    unsafe { (*(*parent_node).as_ref().unwrap().as_ptr()).right = new_node; }
                    unsafe { loop_nodes.push( &mut (*(*parent_node).as_ref().unwrap().as_ptr()).right as *mut Option<Rc<RefCell<TreeNode>>>); };
                }
            }
            tree_nestedNodes.push(loop_nodes);
        }
        head
    }

//        #   {{{
//    def _tree_toNestedNodesList(self) -> List[List[Optional[TreeNode]]]:
//        depth = TreeNode.max_depth(self)
//        #   nested list of nodes, each inner list corresponding to a level of the tree
//        tree_nestedNodes = [ [ None for x in range(2**i) ] for i in range(depth) ]
//        tree_nestedNodes[0][0] = self
//        for loop_level in range(1, len(tree_nestedNodes)):
//            for j in range(len(tree_nestedNodes[loop_level])):
//                parent_node = tree_nestedNodes[loop_level-1][j//2]
//                if parent_node is None:
//                    tree_nestedNodes[loop_level][j] = None
//                    continue
//                if j % 2 == 0:
//                    tree_nestedNodes[loop_level][j] = parent_node.left
//                else:
//                    tree_nestedNodes[loop_level][j] = parent_node.right
//        return tree_nestedNodes
//        #   }}}
//  Get the nodes of the tree as a nested list
    pub fn _tree_toNestedNodesList(&self) -> Vec<Vec<Option<&TreeNode>>>
    {
        let depth = self.max_depth();
        let mut tree_nestedNodes = vec![];
        tree_nestedNodes.push( vec![ Some(self) ] );
        for i in 1..depth {
            let mut loop_list = vec![];
            for _ in 0..2_usize.pow(i as u32) {
                loop_list.push(None);
            }
            tree_nestedNodes.push(loop_list);
        }
        for loop_level in 1..tree_nestedNodes.len() {
            for j in 0..tree_nestedNodes[loop_level].len() {
                let parent_node = tree_nestedNodes[loop_level-1][j/2];
                if parent_node.is_none() {
                    tree_nestedNodes[loop_level][j] = None;
                    continue;
                }
                if j % 2 == 0 {
                    let l = &parent_node.unwrap().left;
                    tree_nestedNodes[loop_level][j] = if l.is_none() {
                        None
                    } else {
                        let temp = unsafe { &*l.as_ref().unwrap().as_ref().as_ptr() };
                        Some(temp)
                    }
                } else {
                    let r = &parent_node.unwrap().right;
                    tree_nestedNodes[loop_level][j] = if r.is_none() {
                        None
                    } else {
                        let temp = unsafe { &*r.as_ref().unwrap().as_ref().as_ptr() };
                        Some(temp)
                    }
                }
            }
        }
        tree_nestedNodes
    }

//        #   {{{
//    def __repr__(self):
//        result = ""
//        lines, *_ = self._repr_helper()
//        for line in lines:
//            result += line + "\n"
//        return result[:-1]
//        #   }}}
//  Text representation of tree as multi-line string
    pub fn to_string(&self) -> String
    {
        "".to_string()
    }

//        #   {{{
//    def _repr_helper(self):
//        #   LINK: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
//        # No child.
//        if self.right is None and self.left is None:
//            line = '%s' % self.val
//            width = len(line)
//            height = 1
//            middle = width // 2
//            return [line], width, height, middle
//        # Only left child.
//        if self.right is None:
//            lines, n, p, x = self.left._repr_helper()
//            s = '%s' % self.val
//            u = len(s)
//            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
//            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
//            shifted_lines = [line + u * ' ' for line in lines]
//            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
//        # Only right child.
//        if self.left is None:
//            lines, n, p, x = self.right._repr_helper()
//            s = '%s' % self.val
//            u = len(s)
//            first_line = s + x * '_' + (n - x) * ' '
//            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
//            shifted_lines = [u * ' ' + line for line in lines]
//            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
//        # Two children.
//        left, n, p, x = self.left._repr_helper()
//        right, m, q, y = self.right._repr_helper()
//        s = '%s' % self.val
//        u = len(s)
//        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
//        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
//        if p < q:
//            left += [n * ' '] * (q - p)
//        elif q < p:
//            right += [m * ' '] * (p - q)
//        zipped_lines = zip(left, right)
//        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
//        return lines, n + m + u, max(p, q) + 2, n + u // 2
//        #   }}}
//  Returns list of strings, width, height, and horizontal coordinate of the root.
    pub fn _to_string_helper(&self)
    {
    }

}


fn test_fromList_toList()
{
    println!("{}", get_func_name!());
    let input_values: Vec<Vec<Option<i32>>> = vec![ vec![Some(1),Some(3),Some(2),Some(5)], vec![Some(2),Some(1),Some(3),None,Some(4),None,Some(7)], vec![Some(1)], vec![Some(1),Some(2)], vec![], (1..16).map(|x| Some(x)).collect::<Vec::<Option<i32>>>(), vec![Some(1),Some(2),Some(3),Some(4),None,None,Some(7),Some(8),Some(9),None,None,None,None,Some(14),Some(15)], ];
    for values in input_values {
        println!("values=({:?})", values);
        let loop_tree = TreeNode::from_list(&values);
        println!("loop_tree=({:?})", loop_tree);
        if loop_tree.is_some() {
            let loop_list = loop_tree.as_ref().unwrap().as_ref().borrow().to_list();
            println!("loop_list=({:?})", loop_list);
            assert!( (0..values.len()).map(|i| values[i] == loop_list[i]).all(|x| x == true) );
        } else {
            assert_eq!(values.len(), 0);
        }
    }
    println!();
}

fn test_fillListInferMissing() 
{
    println!("{}", get_func_name!());
    println!("warning, test values insufficent - need more complex example of btree-as-list to call this tested");
    let input_values: Vec<Vec<Option<i32>>> = vec![ vec![Some(1)], vec![], vec![Some(1),Some(2)], vec![Some(1),None,Some(2),Some(3)], vec![Some(1),None,Some(2)], vec![Some(1),Some(2),Some(2),None,Some(3),None,Some(3)], vec![Some(5),Some(4),Some(1),None,Some(1),None,Some(4),Some(2),None,Some(2),None], ];
    let result_validate: Vec<Vec<Option<i32>>> = vec![ vec![Some(1)], vec![], vec![Some(1),Some(2),None], vec![Some(1),None,Some(2),None,None,Some(3),None], vec![Some(1),None,Some(2)], vec![Some(1),Some(2),Some(2),None,Some(3),None,Some(3)], vec![Some(5),Some(4),Some(1),None,Some(1),None,Some(4),None,None,Some(2),None,None,None,Some(2),None], ];
    assert_eq!(input_values.len(), result_validate.len());
    for (values, check) in input_values.iter().zip(result_validate.iter()) {
        println!("values=({:?})", values);
        let result = TreeNode::fill_list_infer_missing(&values);
        println!("result=({:?})", result);
        assert_eq!(result, *check, "Check comparison failed");
        if values == check {
            println!("note: values == check (no modification was required)");
        }
        println!("{:?}", TreeNode::from_list(&result));
    }
    println!();
}


fn main() 
{
    test_fromList_toList();
    test_fillListInferMissing();
}

