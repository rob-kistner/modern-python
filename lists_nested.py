from modules.printutils import *

nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]
coords = [ [10.423, 9.123], [37.212, -14.092], [37.212, -14.092], [21.367, 32.572] ]

banner("When would you use nested Lists?")
# ----------------------------------------
print("""• Any time you have a matrix of some type storing data
• Games, Mazes
• Rows & columns for visualizations, tabulation, grouping data
• NOTE on nested list comprehension: this can get pretty darned difficult, so try working from outside in and it could help you visualize the result in a better way.
""")

banner("Variables…")
# ----------------------------------------
var_dump("nested_list", nested_list)
var_dump("coords", coords)


var = nested_list[0][1]
expected(
    "nested_list[0][1]",
    var
)

var = nested_list[2][1]
expected(
    "nested_list[2][1]",
    var
)

var = nested_list[2][1]
expected(
    "or… nested_list[-1][2]",
    var
)

banner("Printing values requires 2 loops…")
# ----------------------------------------
for l in nested_list:
    for val in l:
        print(val)


# TODO: This one doesn't work !
# expected(
#     """Nested list comprehension:
#     [[print(val) for val in l] for l in nested_list]
#     """,
#     [[print(val) for val in l] for l in nested_list]
# )

banner("Creating a nested list via comprehension")
# ----------------------------------------
board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)

banner("Creating a tic-tac-toe board via comprehension")
# ----------------------------------------
tictactoe = [["X" if num%2 != 0 else "O" for num in range(1, 4)] for val in range(1,4)]
print(tictactoe)

banner("Exercise 24: List Exercise 5: Nested with Comprehension")
# ----------------------------------------
answer = [ [num for num in range(0, 3)] for nums in range(0, 3) ]
print(answer)

banner("Exercise 25: One more nested list comprehension exercise")
# ----------------------------------------
answer = [ [num for num in range(0, 10)] for nums in range(0, 10) ]
print(answer)