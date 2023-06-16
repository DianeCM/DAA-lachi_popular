def solution(bad_opinions:list[list[int]], k:int):
    rvsd = create_reversed(bad_opinions)
    solutions_set = solutions_search(rvsd)
    print(solutions_set)
    valid_solutions = []
    for sols in solutions_set:
        if len(sols) == k: return sols
        elif len(sols) < k: valid_solutions.append(sols)
    if len(valid_solutions) > 0: return solve(valid_solutions, k)
    return "Not Valid Solution"

def create_reversed(bad_opinions:list[list[int]]):
    rvsd = [[] for i in bad_opinions]
    for i,bad_opinion in enumerate(bad_opinions):
        for value in bad_opinion:
            rvsd[value].append(i)
    return rvsd

def solutions_search(reversed:list[list[int]]):
    solutions_set:list[set] = []
    for i in range(len(reversed)):
        visited = [False for i in reversed]
        solution = []
        dfs_visited(i, reversed, visited, solution)
        solutions_set.append(set(solution))
    return solutions_set

def dfs_visited(i:int, reversed:list[list[int]], visited:list[bool], solution:list[int]):
    solution.append(i)
    visited[i] = True
    for adj in reversed[i]:
        if not visited[adj]:
            dfs_visited(adj, reversed, visited, solution)
    
def solve(solutions:list[set[int]], k:int):
    return solve_backtrack(solutions, k, 0, set(), set())

def solve_backtrack(solutions:list[set[int]], k:int, index:int, solution:set, max_temp:set):
    if index >= len(solutions): return max_temp
    if len(solution) == k: return solution
    
    inter = solution.intersection(solutions[index])
    curr = solution.union(solutions[index])
    if len(curr) <= k:
        solution = solve_backtrack(solutions, k, index+1, curr, max_temp) 
        if len(solution) > len(max_temp): max_temp = solution.copy()
        if len(solution) == k: return solution
        
        curr = curr.difference(solutions[index]).union(inter)
        solution = solve_backtrack(solutions, k, index+1, curr, max_temp)
        if len(solution) > len(max_temp): max_temp = solution.copy()
        if len(solution) == k: return solution 
    else:
        solution = solve_backtrack(solutions, k, index+1, solution, max_temp)
        if len(solution) > len(max_temp): max_temp = solution.copy() 
        if len(solution) == k: return solution
    
    return max_temp   

bad_opinions = [[3],[3,5],[4],[],[0,3],[],[5]]
print('k=1', solution(bad_opinions,1))
print('k=2', solution(bad_opinions,2))
print('k=3', solution(bad_opinions,3))
print('k=4', solution(bad_opinions,4))
print('k=5', solution(bad_opinions,5))
print('k=6', solution(bad_opinions,6))
print('k=7', solution(bad_opinions,7))