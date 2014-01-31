def solve(n):
    if n == 0: return [[]]  
    smaller_solutions = solve(n-1) 
    solutions = []
    for solution in smaller_solutions:
        for column in range(1,BOARD_SIZE+1): 
            if not under_attack(column , solution): 
                solutions.append(solution + [(n,column)])
    return solutions
