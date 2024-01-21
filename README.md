# Artistic Image Generator

This project is an Artistic Image Generator that allows users to apply various artistic filters to their images. It is built using Flask for the backend and includes options for background removal.

## Features

- Upload an image and apply artistic filters.
- Choose from a variety of filters such as Contour, Blur, Detail, and more.
- Optionally remove the background for a more refined artistic effect.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pillow (PIL)
- OpenCV
- NumPy

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Kalyan69/Artistic_Image_Generater.git
    cd artistic-image-generator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python worker.py
    ```

4. Visit `http://127.0.0.1:5000/` in your browser.

## Usage

1. Open the web application in your browser.
2. Upload an image.
3. Choose a filter from the dropdown list.
4. Optionally, check the "Apply Background Removal" checkbox for background removal.
5. Click the "Generate Artistic Image" button.
6. View the result and download the artistic image.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Create a new pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Bootstrap for the front-end styling.
- Flask for the web framework.
- Pillow (PIL) for image processing.
- OpenCV for background removal...
