class Solution(object):
    def totalNQueens(self, n):
        path = [["." for _ in range(n)] for _ in range(n)]
        seen_col = set()
        count = [0]

        def backtrack(row):
            if row == n:
                count[0]+=1
                return
            for col in range(n):
                if col in seen_col:
                    continue
                r = row-1
                c = col-1
                while r>=0 and c>=0:
                    if path[r][c] == "Q":
                        break
                    r-=1
                    c-=1
                else:
                    r = row-1
                    c = col+1
                    while r>=0 and c<n:
                        if path[r][c] =='Q':
                            break
                        r-=1
                        c+=1
                    else:
                        path[row][col] = "Q"
                        seen_col.add(col)
                        backtrack(row+1)
                        seen_col.remove(col)
                        path[row][col] ="."
            return

        backtrack(0)
        return count[0]