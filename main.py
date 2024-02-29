from process_image import convert_to_binary_black_and_white, extract_wave_colour
from get_wave_coordinates import plot_coordinates, get_plotpoints
from calculate_pulse_pressure import calc_pulsepressure_var
from plot_coord import plot_graph 
from find_lines import find_and_plot_lines

import helper_functions  

def main():
    # Gets image path
    image_path = helper_functions.get_image()

    # Gets threshold value to use
    threshold_value = helper_functions.get_threshold()

    # Converts image to black and white, extracts binary data
    binary_image, binary_data = convert_to_binary_black_and_white(image_path, threshold_value)

    # Extracts wave colour
    wave_colour = extract_wave_colour(binary_image, binary_data)

    # Plots coordinates as a list
    coordinates = plot_coordinates(wave_colour, binary_image)

    # Get relevant plot points from the list
    high_max, low_max, high_min, low_min, coord_max_index, coord_min_index = get_plotpoints(coordinates)

    # Calculate pulse_pressure
    ppv = calc_pulsepressure_var(high_max, low_max, high_min, low_min)

    # Plot the graph using the coordinates and plot points
    plot_graph(coordinates, coord_max_index, coord_min_index)

    # Find and plot lines connecting black points in specified areas
    # just for test, diogo, 
    find_and_plot_lines(coordinates)

    return ppv

if __name__ == "__main__":
    main()
