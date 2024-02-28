from PIL import Image
import matplotlib.pyplot as plt

# Converts image to black and white, returns output path
def convert_to_binary_black_and_white(image_path, threshold):
	# Open the image
	img = Image.open(image_path)

	# Convert the image to grayscale
	img = img.convert('L')

	# Apply binary threshold 
	binary_data = []
	for pixel_value in img.getdata():
		if pixel_value > threshold:
			binary_data.append(255)
		else:
			binary_data.append(0)

	# Create a new image with binary data
	binary_img = Image.new('L', img.size)
	binary_img.putdata(binary_data)

	print(f"Testing {image_path}")
	# Save the result
	directory, filename = image_path.rsplit('/', 1)
	output_path = directory + '/binary_' + filename
	binary_img.save(output_path)

	print(f"Image converted and saved as {output_path}")

	# Returns binary data
	return binary_img, binary_data

# Gets wave colour by measuring the least commonly used colour on picture
def extract_wave_colour(binary_img, binary_data):
	# Calculate percentage of black and white pixels
	total_pixels = binary_img.size[0] * binary_img.size[1]
	black_pixels = binary_data.count(0)
	white_pixels = binary_data.count(255)

	percentage_black = (black_pixels / total_pixels) * 100
	percentage_white = (white_pixels / total_pixels) * 100

	print(f"Percentage of black pixels: {percentage_black:.2f}%")
	print(f"Percentage of white pixels: {percentage_white:.2f}%")

	# Determine the less common color
	less_common_color = 0 if black_pixels < white_pixels else 255

	return less_common_color