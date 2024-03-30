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
    # Generate an initial random solution
    current_solution = [i for i in range(n)]  # Each queen is placed in a different row initially
    random.shuffle(current_solution)  # Randomly shuffle the positions
    current_cost = cost(current_solution)  # Calculate the cost of the initial solution

    temp = initial_temp  # Initialize the temperature
    for i in range(max_iter):  # Iterate until max_iter or until a solution is found
        if current_cost == 0:  # If cost is 0, a solution is found
            break

        # Generate a neighbor solution by swapping positions of two random queens
        neighbor_solution = current_solution.copy()
        rand_queen1, rand_queen2 = random.sample(range(n), 2)  # Choose two random queens
        neighbor_solution[rand_queen1], neighbor_solution[rand_queen2] = neighbor_solution[rand_queen2], neighbor_solution[rand_queen1]  # Swap their positions

        neighbor_cost = cost(neighbor_solution)  # Calculate the cost of the neighbor solution

        # Accept the neighbor solution with a probability determined by the acceptance probability function
        delta_cost = neighbor_cost - current_cost
        acceptance_prob = min(1, math.exp(-delta_cost / temp))
        if delta_cost < 0 or random.random() < acceptance_prob:  # If the neighbor solution is better or with probability determined by acceptance probability
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        # Cool down the temperature
        temp *= cooling_rate

    return current_solution, current_cost

def display_board(queens):
    """
    Display the board with queens placed.
    """
    n = len(queens)
    for row in range(n):
        line = ""
        for col in range(n):
            if queens[col] == row:
                line += "Q "  # Queen is placed at this position
            else:
                line += ". "  # Empty position
        print(line)
    print()

if __name__ == "__main__":
    n = 8  # Number of queens
    max_iter = 10000  # Maximum number of iterations
    initial_temp = 100.0  # Initial temperature for simulated annealing
    cooling_rate = 0.99  # Cooling rate for simulated annealing

    # Solve the n-queens problem using simulated annealing
    solution, final_cost = simulated_annealing(n, max_iter, initial_temp, cooling_rate)
    print("Solution:", solution)
    print("Final Cost:", final_cost)
    display_board(solution)  # Display the board with queens placed
