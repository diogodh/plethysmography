import numpy as np
import matplotlib.pyplot as plt

def find_and_plot_lines(coordinates):

    print("\nMiguel, wait, this really takes long to find the lines, about 10 seconds I guess...")

    # Convert the list of tuples to a NumPy array
    coordinates_array = np.array(coordinates)

    # Extract x-values from coordinates
    x_values = coordinates_array[:, 0]

    # Define the areas of interest as a percentage of x-values
    areas_of_interest = [(0.093, 0.10), (0.343, 0.35), (0.693, 0.70), (0.943, 0.95)]

    # Initialize a list to store points for each area
    points_by_area = []

    # Iterate over the areas of interest
    for area_start, area_end in areas_of_interest:
        # Calculate the range of x-values for the specified area
        start_x = int(area_start * max(x_values))
        end_x = int(area_end * max(x_values))
        
        # Extract the points for the specified area
        area_points = coordinates_array[(coordinates_array[:, 0] >= start_x) & (coordinates_array[:, 0] <= end_x)]

        # Add the points to the list
        points_by_area.append(area_points)

        # Plot the areas of interest in grey
        plt.axvspan(start_x, end_x, facecolor='pink', alpha=0.9)


    # Initialize a list to store valid lines connecting points from different areas
    valid_lines = []

    # Check for valid lines connecting points from different areas
    for i in range(len(points_by_area) - 1):
        for j in range(i + 1, len(points_by_area)):
            for point1 in points_by_area[i]:
                for point2 in points_by_area[j]:
                    # Check if a line connects points from different areas and is straight
                    if point1[1] == point2[1]:
                        # Store the valid line in the list
                        valid_lines.append([(point1[0], point1[1]), (point2[0], point2[1])])
                 

    # Plot all the valid lines at once
    for line in valid_lines:
        plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], color='red')
      
    # Plot points for each area
    for area_points in points_by_area:
        plt.scatter(area_points[:, 0], area_points[:, 1], color='green')


    # Plot original coordinates
    plt.scatter(coordinates_array[:, 0], coordinates_array[:, 1], color='blue')

    # Invert the y-axis
    plt.gca().invert_yaxis()

    plt.title('Points and Valid Lines')
    plt.show()
