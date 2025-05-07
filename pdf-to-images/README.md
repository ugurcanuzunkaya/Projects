# PDF to Images Converter

This project provides a simple way to convert PDF files into images, allowing users to specify a range of pages to convert. 

## Features

- Convert specified pages of a PDF file to images.
- Save images in a specified format.
- Easy-to-use interface.

## Installation

To get started, clone the repository and install the required dependencies. You can do this by running:

```bash
git clone <repository-url>
cd pdf-to-images
pip install -r requirements.txt
```

## Usage

To convert a PDF file to images, you can use the `convert_pdf_to_images` function from the `pdf_converter.py` file. Here’s an example of how to use it:

```python
from src.pdf_converter import convert_pdf_to_images

pdf_path = 'path/to/your/file.pdf'
start_page = 1
end_page = 5

convert_pdf_to_images(pdf_path, start_page, end_page)
```

Make sure to replace `'path/to/your/file.pdf'` with the actual path to your PDF file.

## Configuration

You can modify the output directory and image format in the `src/config.py` file. The default settings can be adjusted as needed.

## Dependencies

This project requires the following Python packages:

- Pillow
- PyPDF2

You can install these packages using the provided `requirements.txt` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.