import sys

# Specify the path to the JPEG image
def get_image():
	# If given at CLI, use that one
	if len(sys.argv) > 1:
		image_path = ("images/" + sys.argv[1])
	# If non-existant, get standard test image
	else:
		image_path = "images/test01.jpg"
	return image_path

# Set the threshold for binary conversion 
def get_threshold():
	# If given at CLI, use that one
	if len(sys.argv) > 2:
		threshold_value = int(sys.argv[2])
	# If non-existant, get standard value
	else:
		threshold_value = 128
	return threshold_value
