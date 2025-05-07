from pdf_converter import convert_pdf_to_images
import argparse

def main():
    pdf_file_path = input("Enter the path to the PDF file: ")
    start_page = int(input("Enter the starting page number: "))
    end_page = int(input("Enter the ending page number: "))
    convert_pdf_to_images(pdf_file_path, start_page, end_page)
    print("Conversion completed.")

if __name__ == "__main__":
    main()