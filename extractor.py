import os
import easyocr
import numpy as np
from PIL import Image
import fitz
from io import BytesIO

def extract_text_from_image(image_data):
    
    # Extract text from an image using EasyOCR.
    
    try:
        # EasyOCR reader for English only
        reader = easyocr.Reader(['en'])

        # Extract text from image
        text = reader.readtext(image_data, detail=0)
        return "\n".join(text)

    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return None

def extract_text_from_pdf(pdf_path):

    # Extract text from a PDF, using OCR if necessary.

    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File not found: {pdf_path}")

        # Open PDF file
        doc = fitz.open(pdf_path)
        text = ""

        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)

            # Try to extract text from the page
            page_text = page.get_text("text")
            text += page_text

            # If the page has no selectable text, use OCR
            if not page_text.strip():
                pix = page.get_pixmap()
                img = Image.open(BytesIO(pix.tobytes()))
                img_np = np.array(img)

                ocr_text = extract_text_from_image(img_np)
                text += ocr_text

        return text

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def extract_text_auto(file_path):
    
    # Automatically detect if the file is an 
    # image or a PDF and extract text accordingly.
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    file_extension = os.path.splitext(file_path)[1].lower()

    # If it's a PDF file, extract text from PDF
    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)

    # If it's an image file, extract text from the image
    elif file_extension in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        return extract_text_from_image(file_path)

    else:
        print(f"Unsupported file format: {file_extension}")
        return None
