import matplotlib.pyplot as plt

def plot_graph(coordinates, coord_max_index, coord_min_index):
    x, y = zip(*coordinates)

    # Plotting coordinates in blue
    plt.scatter(x, y, color='blue', label='Coordinates')

    # Plotting max and min indices in red
    plt.scatter(coord_max_index[0], coord_max_index[1], color='red', marker='^', label='Max Index')
    plt.scatter(coord_min_index[0], coord_min_index[1], color='red', marker='v', label='Min Index')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    # Adding labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph with Coordinates, Max Index, and Min Index')
    plt.legend()

    # Display the plot
    plt.show()