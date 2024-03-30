import random
import math

def cost(queens):
    """
    Calculate the number of attacking pairs of queens.
    """
    n = len(queens)
    cost = 0
    for i in range(n):
        for j in range(i+1, n):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                cost += 1
    return cost

def simulated_annealing(n, max_iter, initial_temp, cooling_rate):
    """
    Solve the n-queens problem using simulated annealing.
    """
    current_solution = [i for i in range(n)]
    random.shuffle(current_solution)
    current_cost = cost(current_solution)

    temp = initial_temp
    for i in range(max_iter):
        if current_cost == 0:
            break

        # Generate a neighbor solution
        neighbor_solution = current_solution.copy()
        rand_queen1, rand_queen2 = random.sample(range(n), 2)
        neighbor_solution[rand_queen1], neighbor_solution[rand_queen2] = neighbor_solution[rand_queen2], neighbor_solution[rand_queen1]

        neighbor_cost = cost(neighbor_solution)

        # Accept the neighbor solution with a probability determined by the acceptance probability function
        delta_cost = neighbor_cost - current_cost
        acceptance_prob = min(1, math.exp(-delta_cost / temp))
        if delta_cost < 0 or random.random() < acceptance_prob:
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        # Cool down the temperature
        temp *= cooling_rate

    return current_solution, current_cost

def display_board(queens):
    n = len(queens)
    for row in range(n):
        line = ""
        for col in range(n):
            if queens[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    n = 8  # Change this to the desired number of queens
    max_iter = 10000
    initial_temp = 100.0
    cooling_rate = 0.99

    solution, final_cost = simulated_annealing(n, max_iter, initial_temp, cooling_rate)
    print("Solution:", solution)
    print("Final Cost:", final_cost)
    display_board(solution)
