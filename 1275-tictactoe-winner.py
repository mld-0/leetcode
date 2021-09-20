from typing import List, Union

class Solution:

    def board_from_moves(self, moves: List[List[int]]) -> List[List[int]]:
        result = [ [ None for col in range(3) ] for row in range(3) ]
        player = 'X'
        for move in moves:
            row, col = move
            result[row][col] = player
            if player == 'X':
                player = 'O'
            elif player == 'O':
                player = 'X'
        return result

    def winner_from_board(self, board: List[List[int]]) -> Union[str, None]:
        pass
        #   Check rows
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]
        #   Check cols
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2]:
                return board[row][0]
        #   Check diags
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[2][0] == board[1][1] == board[0][2]:
            return board[2][0]
        return None

    #   runtime: beats 53%
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = self.board_from_moves(moves)
        winner = self.winner_from_board(board)
        if winner == 'X':
            return 'A'
        elif winner == 'O':
            return 'B'
        if len(moves) == 9:
            return "Draw"
        return "Pending"


s = Solution()

input_values = [ [[0,0],[2,0],[1,1],[2,1],[2,2]], [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], [[0,0],[1,1]] ]
input_checks = [ "A", "B", "Draw", "Pending" ]

for moves, check in zip(input_values, input_checks):
    result = s.tictactoe(moves)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

