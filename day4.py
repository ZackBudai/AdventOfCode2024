with open("day4.txt", "r") as txt_file:
  contents = txt_file.read().splitlines()


#PART 1

board = []
board.append("0"*(len(contents[0])+6))
board.append("0"*(len(contents[0])+6))
board.append("0"*(len(contents[0])+6))
for line in contents:
  board.append("0"*3 + line + "0"*3)
board.append("0"*(len(contents[0])+6))
board.append("0"*(len(contents[0])+6))
board.append("0"*(len(contents[0])+6))
num = 0


def check(coord):
    count = 0
    line = coord[0]
    char = coord[1]
    if board[line][char] + board[line-1][char] + board[line-2][char] + board[line-3][char] == "XMAS":
       count += 1
    if board[line][char] + board[line+1][char] + board[line+2][char] + board[line+3][char] == "XMAS":
       count += 1
    if board[line][char] + board[line][char-1] + board[line][char-2] + board[line][char-3] == "XMAS":
       count += 1
    if board[line][char] + board[line][char+1] + board[line][char+2] + board[line][char+3] == "XMAS":
       count += 1
    if board[line][char] + board[line+1][char+1] + board[line+2][char+2] + board[line+3][char+3] == "XMAS":
       count += 1
    if board[line][char] + board[line+1][char-1] + board[line+2][char-2] + board[line+3][char-3] == "XMAS":
       count += 1
    if board[line][char] + board[line-1][char+1] + board[line-2][char+2] + board[line-3][char+3] == "XMAS":
       count += 1
    if board[line][char] + board[line-1][char-1] + board[line-2][char-2] + board[line-3][char-3] == "XMAS":
       count += 1
    return count

for line in range(len(board)):
    for char in range(len(board[line])):
        if board[line][char] == 'X':
            num += check([line,char])

print(num)

#PART 2
num = 0

board = contents
def check(coords):
    count = 0
    i = coords[0]
    j = coords[1]
    if board[i+1][j+1] == "A":
        if board[i][j] == 'S':
            if board[i][j+2] == "S" and board[i+2][j] == "M" and board[i+2][j+2] == "M":
               count += 1
            if board[i][j+2] == "M" and board[i+2][j] == "S" and board[i+2][j+2] == "M":
               count += 1
        
        if board[i][j] == "M":
           if board[i][j+2] == "S" and board[i+2][j] == "M" and board[i+2][j+2] == "S":
               count += 1
           if board[i][j+2] == "M" and board[i+2][j] == "S" and board[i+2][j+2] == "S":
               count += 1
       
    return count


for i in range(len(board)-2):
   for j in range(len(board)-2):
    num += check([i,j])
print(num)

