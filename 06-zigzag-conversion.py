#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2

#   Rule: Convert string by arranging it diagonally (see below)
#   {{{
#   PAYPALISHIRING -> PAHNAPLSIIGYIR
#   P   A   H   N       4
#   A P L S I I G       7
#   Y   I   R           3
#   PAYPALISHIRING -> PINALSIGYAHRPI
#   P     I     N       
#   A   L S   I G       
#   Y A   H R           
#   P     I             
#   }}}

class Solution:

    #   runtime: beats 99%
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [ [] for _ in range(numRows) ]
        i = 0
        try:
            while i < len(s):
                for j in range(numRows):
                    rows[j].append(s[i])
                    i += 1
                for j in range(numRows-2, 0, -1):
                    rows[j].append(s[i])
                    i += 1
        except IndexError as e:
            pass
        rows = [ ''.join(row) for row in rows ]
        result = ''.join(rows)
        return result

    #   runtime: beats 95%
    def convert_ans(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s
        rows = [ [] for _ in range(min(numRows,len(s))) ]
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow].append(c)
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1
        rows = [ ''.join(row) for row in rows ]
        result = ''.join(rows)
        return result


s = Solution()
test_functions = [ s.convert, s.convert_ans, ]

inputs = [ ("PAYPALISHIRING",3),  ("PAYPALISHIRING",4), ("A",1), ]
checks = [ "PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A", ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for (s, numRows), check in zip(inputs, checks):
        print("s=(%s), numRows=(%s)" % (s,numRows))
        result = f(s, numRows)
        print("result=(%s)" % result)
        assert result == check, "result comparison failed"
    print()

