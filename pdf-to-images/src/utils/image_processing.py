import os
import config

def save_image(image, page_number):
    """
    Save PIL Image object to the output directory
    
    Args:
        image: PIL Image object
        page_number: Page number for filename
    """
    output_path = os.path.join(config.OUTPUT_DIR, f"page_{page_number}.png")
    image.save(output_path, "PNG")
    return output_path