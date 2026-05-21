"""
PDF Text Extraction Module
This module handles reading and extracting text from PDF files.
"""

import PyPDF2
from io import BytesIO


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_file: Either a file path (str) or a file-like object (BytesIO)
    
    Returns:
        Extracted text as a string
    
    Raises:
        ValueError: If PDF is invalid or cannot be read
        Exception: For other extraction errors
    """
    try:
        # Handle both file paths and file-like objects (from Streamlit upload)
        if isinstance(pdf_file, str):
            # File path provided
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = _extract_from_reader(pdf_reader)
        else:
            # File-like object (BytesIO from Streamlit)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = _extract_from_reader(pdf_reader)
        
        if not text.strip():
            raise ValueError("No text could be extracted from the PDF")
        
        return text
    
    except PyPDF2.errors.PdfReadError:
        raise ValueError("Invalid PDF file. Please ensure the file is a valid PDF.")
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")


def _extract_from_reader(pdf_reader) -> str:
    """
    Helper function to extract text from a PdfReader object.
    
    Args:
        pdf_reader: PyPDF2.PdfReader object
    
    Returns:
        Extracted text as a string
    """
    text = ""
    
    # Iterate through all pages
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
        text += "\n"  # Add newline between pages for readability
    
    return text


def get_pdf_page_count(pdf_file) -> int:
    """
    Get the number of pages in a PDF file.
    
    Args:
        pdf_file: Either a file path (str) or a file-like object (BytesIO)
    
    Returns:
        Number of pages in the PDF
    """
    try:
        if isinstance(pdf_file, str):
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                return len(pdf_reader.pages)
        else:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            return len(pdf_reader.pages)
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")
