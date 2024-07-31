import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

def random_initial_state(n_cells=100, n_generations=100):
    first_row = np.random.choice([1, 2], size=n_cells)
    spacetime = np.zeros(shape=(n_generations, n_cells))
    spacetime[0] = first_row
    return spacetime

def initialize(n_cells=0, n_generations=100, rule_number=110):
    initial_state = random_initial_state(n_cells, n_generations)
    cmap = colors.ListedColormap(['white', 'black', 'grey'])
    bounds = [0, 1, 2, 2]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    fig, ax = plt.subplots()
    frame = ax
    frame.axes.get_xaxis().set_visible(True)
    frame.axes.get_yaxis().set_visible(True)
    grid = ax.imshow(initial_state, interpolation='nearest', cmap=cmap, norm=norm)
    ax.set_xticks(np.arange(0, n_cells, 1))
    ax.set_yticks(np.arange(0, n_generations, 1))
    ax.set_xticklabels(np.arange(0, n_cells, 1))
    ax.set_yticklabels(np.arange(0, n_generations, 1))
    
    # Add title with rule number and its binary equivalent
    rule_binary_str = format(rule_number, '#010b')[2:]
    ax.set_title(f"Rule Number: {rule_number}, Binary: {rule_binary_str}")
    
    rule = generate_rule(rule_number)
    ani = animation.FuncAnimation(fig, next_generation,
                                  fargs=(grid, initial_state, rule),
                                  frames=n_generations - 1,
                                  interval=50,
                                  blit=False)

    plt.show()

def next_generation(i, grid, initial_state, rule):
    current_generation = initial_state[i]
    new_state = initial_state.copy()
    new_generation = process(current_generation, rule)
    new_state[i + 1] = new_generation
    grid.set_data(new_state)
    initial_state[:] = new_state[:]
    return grid,

def process(generation, rule):
    new_generation = []
    for i, cell in enumerate(generation):
        neighbours = []
        if i == 0:
            neighbours = [generation[len(generation) - 1], cell, generation[1]]
        elif i == len(generation) - 1:
            neighbours = [generation[len(generation) - 2], cell, generation[0]]
        else:
            neighbours = [generation[i - 1], cell, generation[i + 1]]
        new_generation.append(rule[tuple(neighbours)])
    return new_generation

def generate_rule(rule_number):
    rule_str = format(rule_number, '#010b')[2:]
    rule = {
        (2, 2, 2): int(rule_str[0]) + 1,
        (2, 2, 1): int(rule_str[1]) + 1,
        (2, 1, 2): int(rule_str[2]) + 1,
        (2, 1, 1): int(rule_str[3]) + 1,
        (1, 2, 2): int(rule_str[4]) + 1,
        (1, 2, 1): int(rule_str[5]) + 1,
        (1, 1, 2): int(rule_str[6]) + 1,
        (1, 1, 1): int(rule_str[7]) + 1
    }
    return rule

def main():
    n_cells = int(input("Number of cells: "))
    n_generations = int(input("Number of generations: "))
    rule_number = int(input("Rule number: "))
    initialize(n_cells, n_generations, rule_number)

if __name__ == '__main__':
    main()







