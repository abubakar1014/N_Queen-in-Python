print("Enter Total number of Queen you want : ")
Queens = int(input())      # Total Queens input
queen_board = [[0] * Queens for _ in range(Queens)]       #Board
print("Enter Total number of Iterations/backtrackings you want : ")
iterations = int(input())
class algorithm:                      #Main class
    def __init__(self):
        self.iter = 0
    def print_board(self):         #Only Print Board
        for i in queen_board:
            print(i)
    def check_row_colum(self, row, colum):      # this checks value of queen in whole row and colum
        for temp in range(0, Queens):
            if queen_board[row][temp] == 1 or queen_board[temp][colum] == 1:
                return True
        for i in range(0, Queens):           # this checks queen values diagonal
            for j in range(0, Queens):
                if (i + j == row + colum) or (i - j == row - colum):
                    if queen_board[i][j] == 1:
                        return True
        return False
    def main_function(self, temp_queen):                  # main finction to perform N_Queen
        if temp_queen == 0:    # Base condition for recurssion
            print("Solutions Found")
            return True
        if self.iter == iterations:         #It checks backtracking numbers
            print("Solutions Not Found in these number of backtracking")
            return True
        for i in range(0, Queens):
            for j in range(0, Queens):
                if (not(self.check_row_colum(i, j))):    # Check values in colum , row and diagonal
                    if (queen_board[i][j] != 1):
                        queen_board[i][j] = 1
                        self.print_board()
                        print("\n\n")
                    flag = self.main_function(temp_queen - 1)   # recursive call
                    if flag == True:
                        return True
                    queen_board[i][j] = 0
                    self.iter = self.iter + 1
                    print("Backtracking value : ", self.iter)
                    if self.iter == iterations:                #Checks backtracing value
                        print("\nIteration finished\n ")
        return False
obj = algorithm()                 #Class object
obj.main_function(Queens)         #Main Queen Function
obj.print_board()                  #Board function
