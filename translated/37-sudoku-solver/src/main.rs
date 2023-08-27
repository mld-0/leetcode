use std::time::Instant;

struct Solution {}
impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let s = Solver { board };
        s.solve();
    }
}

pub struct Solver<'a> { board: &'a mut Vec<Vec<char>> }
impl<'a> Solver<'a> {
    fn solve(&self) {
        println!("{:?}", &self.board);
        unimplemented!();
    }
}

//class Solution:
//
//    def solveSudoku(self, board):
//        self.setBoard(board)
//        self.solve_backtracking()
//        return self.board
//
//    def setBoard(self, board):
//        self.board = board
//
//    def solve_backtracking(self):
//        """Backtracking solution, fill next empty square with each possible option and recurse"""
//        #   for next unassigned square
//        row, col = self.findUnassigned()
//        if row == -1 and col == -1:
//            return True
//        #   try to fill that square for each possible value
//        options = self.options(row, col)
//        for i in options:
//            #   attempt to place each possible value, backtracking if unsucessful
//            self.board[row][col] = i
//            result = self.solve_backtracking()
//            if result == True:
//                return True
//            self.board[row][col] = '.'
//        #   If we failed to place a value, problem must be unsolveable for current board
//        return False
//
//    def findUnassigned(self):
//        """Find coordinates of the empty square with the least possible options"""
//        best = (-1, -1)
//        best_options_len = math.inf
//        for row in range(9):
//            for col in range(9):
//                if self.board[row][col] == '.':
//                    options = self.options(row, col)
//                    if len(options) < best_options_len:
//                        best_options_len = len(options)
//                        best = (row, col)
//        return best
//
//    def options(self, row, col):
//        """Get available values for a given (empty) square"""
//        options_row = self.options_checkrow(row)
//        options_col = self.options_checkcol(col)
//        options_sector = self.options_checksector(row, col)
//        return options_row & options_col & options_sector
//
//    def options_checkrow(self, row):
//        """Get available values for a given row"""
//        options = set( [str(i) for i in range(1, 10) ] )
//        for loop_col in range(9):
//            val = self.board[row][loop_col]
//            if val != '.':
//                options.remove(val)
//        return options
//
//    def options_checkcol(self, col):
//        """Get available values for a given col"""
//        options = set( [str(i) for i in range(1, 10) ] )
//        for loop_row in range(9):
//            val = self.board[loop_row][col]
//            if val != '.':
//                options.remove(val)
//        return options
//
//    def options_checksector(self, row, col):
//        """Get available values for a given (3x3) sector"""
//        sector_row = row - row % 3
//        sector_col = col - col % 3 
//        options = set( [str(i) for i in range(1, 10) ] )
//        for loop_row in range(sector_row, sector_row+3):
//            for loop_col in range(sector_col, sector_col+3):
//                val = self.board[loop_row][loop_col]
//                if val != '.':
//                    options.remove(val)
//        return options

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
        let now = Instant::now();
        for (board, check) in inputs.iter().zip(checks.iter()) {
            let mut board = board.clone();
            print_board("board", &board);
            f(&mut board);
            print_board("result", &board);
            assert_eq!(board, *check, "Check comparison failed");
        }
        println!("elapsed_us=({:?})", now.elapsed().as_micros());
        println!();
    }
}

