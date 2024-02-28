def plot_coordinates(wave_color, binary_img):
	# Create a list of coordinates for the less common color
	coordinates = [(x, y) for x in range(binary_img.size[0]) for y in range(binary_img.size[1]) if binary_img.getpixel((x, y)) == wave_color]

	# Print the coordinates
	#print(f"Coordinates of the less common color ({wave_color}): {coordinates}")

    # Save the coordinates to a text file
	txt_output_path = "coordinates.txt"
	with open(txt_output_path, 'w') as file:
		for x, y in coordinates:
			file.write(f"{x},{y}\n")

	# Return list of coordinates
	return coordinates



def get_plotpoints(coordinates):
	# Initialize maximum point with negative infinity
	high_max = float('-inf')
	max_index = None
	# Initialize minmum with positive infinity
	low_min = float('inf')  
	min_index = None

	# Gets max (high_max) and minimum (low_min) values
	# Saves index of these values so as to speed up subsequent search of low_max and high_min
	for index, (x, y) in enumerate(coordinates):
		if y > high_max:
			high_max = y
			max_index = index
		if y < low_min:
			low_min = y
			min_index = index


	print(f"\nHigh Max is {high_max} at index {max_index} ({coordinates[max_index]})")
	print(f"Low Min is {low_min} at index {min_index} ({coordinates[min_index]})")
	# Gets first minimum at the left of high_max (high_min)
	# Initialize high_min point with negative infinity
	high_min = float('inf')
	
	# Starts looking from the highest low from high_max backwards
	old_y = high_max
	for index in range(max_index - 1, -1, -1):
		y = coordinates[index][1]
		if y < old_y:
			old_y = y
		else:
			high_min = old_y
			break
	
	print(f"High Min is {high_min}")

	# Gets first maximum at the left of low_min (high_min)
	# Initialize low_min point with positive infinity
	low_max = float('-inf')
	
	# Starts looking from the lowest max from low_min onwards
	old_y = low_max
	for index in range(min_index + 1, len(coordinates)):
		y = coordinates[index][1]
		if y > old_y:
			old_y = y
		else:
			low_max = old_y
			break	

	print(f"Low Max is {low_max}")

	return high_max, low_max, high_min, low_min, coordinates[max_index], coordinates[min_index]