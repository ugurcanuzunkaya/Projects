def convert_pdf_to_images(pdf_path, start_page, end_page):
    import fitz  # PyMuPDF
    import os
    from utils.image_processing import save_image
    import config

    # Ensure the output directory exists
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Adjust for 0-based indexing in PyMuPDF (page numbers in PyMuPDF start from 0)
    start_page_idx = start_page - 1
    end_page_idx = min(end_page - 1, pdf_document.page_count - 1)
    
    # Convert pages to images
    for i in range(start_page_idx, end_page_idx + 1):
        page = pdf_document[i]
        
        # Render page to an image (with higher resolution)
        pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
        
        # Save the image
        page_number = i + 1  # Convert back to 1-based for user-facing messages
        image_path = os.path.join(config.OUTPUT_DIR, f"page_{page_number}.png")
        pix.save(image_path)
        print(f"Saved image for page {page_number}")
    
    pdf_document.close()