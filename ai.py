from PIL import Image, ImageFilter
import sys

def apply_filter(image, filter_name, filter_params=None):
    if filter_params is None:
        filter_params = {}

    filters = {
        "contour": ImageFilter.CONTOUR,
        "blur": ImageFilter.BLUR,
        "edge_enhance": ImageFilter.EDGE_ENHANCE,
        # Add more filters as needed
    }

    if filter_name in filters:
        return image.filter(filters[filter_name], **filter_params)
    else:
        print(f"Filter '{filter_name}' not found.")
        sys.exit(1)

def create_artistic_image(input_path, output_path, filter_name, filter_params=None):
    original_image = Image.open(input_path)

    # Apply the selected filter
    artistic_image = apply_filter(original_image, filter_name, filter_params)

    artistic_image.save(output_path)

if __name__ == "__main__":
    input_image_path = "bhosadi.jpg"
    output_image_path = "artistic_image.jpg"

    # Specify the filter and its parameters
    selected_filter = input("Enter filter name (contour, blur, edge_enhance, etc.): ")
    filter_parameters = {}  # You can customize this based on the filter you choose

    # Create artistic image
    create_artistic_image(input_image_path, output_image_path, selected_filter, filter_parameters)

    print(f"Artistic image created and saved at {output_image_path}")
