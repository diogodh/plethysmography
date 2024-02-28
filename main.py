import helper_functions
from process_image import convert_to_binary_black_and_white, extract_wave_colour
from get_wave_coordinates import plot_coordinates, get_plotpoints
from calculate_pulse_pressure import calc_pulsepressure_var

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

	# Get relevant plot points from list
	high_max, low_max, high_min, low_min = get_plotpoints(coordinates)

	# Calculate pulse_pressure
	ppv = calc_pulsepressure_var(high_max, low_max, high_min, low_min)

	return ppv

if __name__ == "__main__":
	main()