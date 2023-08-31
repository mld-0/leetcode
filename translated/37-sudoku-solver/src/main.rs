//  {{{3
//  vim: set tabstop=4 modeline modelines=10:
//  vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//  {{{2
use std::time::Instant;
use std::collections::HashSet;

struct Solution {}
impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let mut s = Solver { board };
        s.solve();
    }
}

pub struct Solver<'a> { board: &'a mut Vec<Vec<char>> }
impl<'a> Solver<'a> {

    //  runtime: beats 47%
    fn solve(&mut self) -> bool {
        let unassigned = self.find_unassigned();
        if unassigned.is_none() {
            return true;
        }
        let (row, col) = unassigned.unwrap();
        let options = self.options(row, col);
        for i in options {
            self.board[row][col] = i;
            let result = self.solve();
            if result == true {
                return true;
            }
            self.board[row][col] = '.';
        }
        false
    }

    fn find_unassigned(&self) -> Option<(usize, usize)> {
        let mut best = None;
        let mut best_options_len = usize::MAX;
        for row in 0..9 {
            for col in 0..9 {
                if self.board[row][col] == '.' {
                    let options = self.options(row, col);
                    if options.len() == 1 {
                        return Some((row, col));
                    } else if options.len() < best_options_len {
                        best_options_len = options.len();
                        best = Some((row, col));
                    }
                }
            }
        }
        best
    }

    fn options(&self, row: usize, col: usize) -> HashSet<char> {
        let options_row = self.options_checkrow(row);
        let options_col = self.options_checkcol(col);
        let options_sector = self.options_checksector(row, col);
        options_row.intersection(&options_col).cloned().collect::<HashSet<_>>().intersection(&options_sector).cloned().collect()
    }

    fn options_checkrow(&self, row: usize) -> HashSet<char> {
        let mut options = ('1'..='9').collect::<HashSet<char>>();
        for loop_col in 0..9 {
            let val = self.board[row][loop_col];
            if val != '.' {
                options.remove(&val);
            }
        }
        options
    }

    fn options_checkcol(&self, col: usize) -> HashSet<char> {
        let mut options = ('1'..='9').collect::<HashSet<char>>();
        for loop_row in 0..9 {
            let val = self.board[loop_row][col];
            if val != '.' {
                options.remove(&val);
            }
        }
        options
    }

    fn options_checksector(&self, row: usize, col: usize) -> HashSet<char> {
        let sector_row = row - (row % 3);
        let sector_col = col - (col % 3);
        let mut options = ('1'..='9').collect::<HashSet<char>>();
        for loop_row in sector_row..sector_row+3{
            for loop_col in sector_col..sector_col+3 {
                let val = self.board[loop_row][loop_col];
                if val != '.' {
                    options.remove(&val);
                }
            }
        }
        options
    }

}


fn print_board(name: &str, board: &Vec<Vec<char>>) {
    println!("{}:", name);
    for line in board {
        println!("{:?}", line);
    }
}

fn main() 
{
    let test_functions = vec![ Solution::solve_sudoku, ];
    let test_functions_names = vec![ "solve_sudoku", ];
    assert_eq!(test_functions.len(), test_functions_names.len());

    let inputs = vec![
        vec![ vec!['.','.','9','7','4','8','.','.','.'], vec!['7','.','.','.','.','.','.','.','.'], vec!['.','2','.','1','.','9','.','.','.'], vec!['.','.','7','.','.','.','2','4','.'], vec!['.','6','4','.','1','.','5','9','.'], vec!['.','9','8','.','.','.','3','.','.'], vec!['.','.','.','8','.','3','.','2','.'], vec!['.','.','.','.','.','.','.','.','6'], vec!['.','.','.','2','7','5','9','.','.'], ],
        vec![ vec!['.','6','.','8','.','.','5','.','.'], vec!['.','.','5','.','.','.','3','6','7'], vec!['3','7','.','.','6','5','8','.','9'], vec!['6','.','9','.','.','2','1','.','.'], vec!['.','.','1','4','8','9','2','.','.'], vec!['.','.','.','3','.','6','9','.','.'], vec!['.','5','.','.','.','.','4','.','.'], vec!['.','1','.','5','4','7','.','.','3'], vec!['.','9','6','.','3','8','.','5','1'], ],
    ];
    let checks = vec![ 
        vec![ vec!['5', '1', '9', '7', '4', '8', '6', '3', '2'], vec!['7', '8', '3', '6', '5', '2', '4', '1', '9'], vec!['4', '2', '6', '1', '3', '9', '8', '7', '5'], vec!['3', '5', '7', '9', '8', '6', '2', '4', '1'], vec!['2', '6', '4', '3', '1', '7', '5', '9', '8'], vec!['1', '9', '8', '5', '2', '4', '3', '6', '7'], vec!['9', '7', '5', '8', '6', '3', '1', '2', '4'], vec!['8', '3', '2', '4', '9', '1', '7', '5', '6'], vec!['6', '4', '1', '2', '7', '5', '9', '8', '3'] ],
        vec![ vec!['9', '6', '2', '8', '7', '3', '5', '1', '4'], vec!['1', '8', '5', '9', '2', '4', '3', '6', '7'], vec!['3', '7', '4', '1', '6', '5', '8', '2', '9'], vec!['6', '4', '9', '7', '5', '2', '1', '3', '8'], vec!['5', '3', '1', '4', '8', '9', '2', '7', '6'], vec!['8', '2', '7', '3', '1', '6', '9', '4', '5'], vec!['7', '5', '3', '6', '9', '1', '4', '8', '2'], vec!['2', '1', '8', '5', '4', '7', '6', '9', '3'], vec!['4', '9', '6', '2', '3', '8', '7', '5', '1'] ],
    ];
    assert_eq!(inputs.len(), checks.len());
    assert!(inputs.len() > 0);

    for (f, f_name) in test_functions.iter().zip(test_functions_names.iter()) {
        println!("{}", f_name);
        for (board, check) in inputs.iter().zip(checks.iter()) {
            let mut board = board.clone();
            print_board("board", &board);
            let now = Instant::now();
            f(&mut board);
            print_board("result", &board);
            assert_eq!(board, *check, "Check comparison failed");
            println!("elapsed_us=({:?})", now.elapsed().as_micros());
        }
        println!();
    }
}

