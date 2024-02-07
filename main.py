# ========== Binomial coefficients ===========
# In chess, a rook can move horizontally or vertically(not diagonally).
# Fill in each square with the number of different shortest paths the rook, in the upper left corner, can take to reach that square.
# The rook starts at the upper left corner and moves to the lower right corner.
# There are six different shortest paths the rook can take to reach each square.
# DDRR, DDRD, DRDR, DRDD, RDRR, RDRD
# =============================================
# ========= Import libraries ==============
import math
# ========= Global Variables ==============
set_moves = ['DDRR', 'DDRD', 'DRDR', 'DRDD', 'RDRR', 'RDRD']
subset = []
# ========= Define Functions ==============
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# ========= Main Program ==============
for i in range(len(set_moves)):
    subset.append(set_moves[i])
    print(subset)
    for j in range(len(subset)):
        print(binomial_coefficient(len(subset), j))


