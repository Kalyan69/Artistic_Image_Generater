from flask import Flask, render_template, request, send_file
from PIL import Image, ImageFilter
from io import BytesIO
import cv2
import numpy as np

app = Flask(__name__)

def apply_filter(image, filter_name, filter_params=None):
    if filter_params is None:
        filter_params = {}

    filters = {
        "contour": ImageFilter.CONTOUR,
        "blur": ImageFilter.BLUR,
        "detail": ImageFilter.DETAIL,
        "edge_enhance": ImageFilter.EDGE_ENHANCE,
        "emboss": ImageFilter.EMBOSS,
        "sharpen": ImageFilter.SHARPEN,
        "smooth": ImageFilter.SMOOTH_MORE,
        "box_blur": ImageFilter.BoxBlur(5),  # Adjust the radius as needed
        "gaussian_blur": ImageFilter.GaussianBlur(5),  # Adjust the radius as needed
        "unsharp_mask": ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3),
        "min_filter": ImageFilter.MinFilter(3),
        "max_filter": ImageFilter.MaxFilter(3),
        "median_filter": ImageFilter.MedianFilter(3),
        "mode_filter": ImageFilter.ModeFilter(3),
        "find_edges": ImageFilter.FIND_EDGES,
        # Add more filters as needed
    }

    if filter_name in filters:
        return image.filter(filters[filter_name], **filter_params)
    else:
        print(f"Filter '{filter_name}' not found.")
        return None

def remove_background(image, apply_background_removal=False):
    img = Image.open(image)
    img_rgb = np.array(img)
    
    if apply_background_removal:
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

        mask = np.zeros(img_rgb.shape[:2], np.uint8)
        rect = (10, 10, img_rgb.shape[1] - 10, img_rgb.shape[0] - 10)
        cv2.grabCut(img_rgb, mask, rect, None, None, 5, cv2.GC_INIT_WITH_RECT)

        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        result = img_rgb * mask2[:, :, np.newaxis]

        return Image.fromarray(result)
    else:
        return img


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    image = request.files['image']
    selected_filter = request.form['filter']
    apply_background_removal = 'backgroundRemoval' in request.form

    # Remove background conditionally based on the checkbox
    processed_image = remove_background(image, apply_background_removal)

    # Apply the selected filter
    artistic_image = apply_filter(processed_image, selected_filter)

    if artistic_image:
        img_io = BytesIO()
        image_format = artistic_image.format if artistic_image.format else 'PNG'
        artistic_image.save(img_io, format=image_format)
        img_io.seek(0)
        mime_type = f'image/{image_format.lower()}'

        return send_file(
            img_io,
            mimetype=mime_type,
            as_attachment=True,
            download_name='artistic_image.png'  # Specify the filename explicitly
        )
    else:
        return "Error applying filter."

if __name__ == "__main__":
    app.run(debug=True)
