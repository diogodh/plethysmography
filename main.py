from PIL import Image
import matplotlib.pyplot as plt

def convert_to_binary_black_and_white(image_path, threshold=128):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img = img.convert('L')

    # Apply binary threshold without using lambda
    binary_data = []
    for pixel_value in img.getdata():
        if pixel_value > threshold:
            binary_data.append(255)
        else:
            binary_data.append(0)

    # Create a new image with binary data
    binary_img = Image.new('L', img.size)
    binary_img.putdata(binary_data)

    # Save the result
    output_path = "/images/binary_test01.jpg"
    binary_img.save(output_path)

    print(f"Image converted and saved as {output_path}")

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

    # Create a list of coordinates for the less common color
    coordinates = [(x, y) for x in range(binary_img.size[0]) for y in range(binary_img.size[1]) if binary_img.getpixel((x, y)) == less_common_color]

    # Print the coordinates
    print(f"Coordinates of the less common color ({less_common_color}): {coordinates}")

    # Save the coordinates to a text file
    txt_output_path = "coordinates.txt"
    with open(txt_output_path, 'w') as file:
        for x, y in coordinates:
            file.write(f"{x},{y}\n")

    print(f"Coordinates saved to {txt_output_path}")

    # Plot the graph
    x_values, y_values = zip(*coordinates)
    plt.scatter(x_values, y_values, color='red', marker='.')
    plt.title('Pixel Locations of Less Common Color')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')

    # Save the plot as an image file
    plot_output_path = "/images/binary_test01_plot.jpg"
    plt.savefig(plot_output_path)

    print(f"Plot saved as {plot_output_path}")

# Specify the path to your JPEG image
image_path = "/images/test01.jpg"

# Set the threshold for binary conversion (adjust as needed)
threshold_value = 128

# Call the function to convert, save the image, calculate percentages, get coordinates, save coordinates to a text file, and save the plot
convert_to_binary_black_and_white(image_path, threshold_value)
