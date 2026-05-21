"""
Web Scraping Module
This module handles fetching and extracting text from URLs.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """
    Validate if a string is a valid URL.
    
    Args:
        url: The URL string to validate
    
    Returns:
        True if valid URL, False otherwise
    """
    try:
        result = urlparse(url)
        # Check if both scheme and netloc (domain) are present
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def scrape_url_content(url: str, timeout: int = 10) -> str:
    """
    Scrape and extract text content from a URL.
    
    Args:
        url: The URL to scrape
        timeout: Request timeout in seconds (default: 10)
    
    Returns:
        Extracted text content from the webpage
    
    Raises:
        ValueError: If URL is invalid or content cannot be extracted
        Exception: For network or other errors
    """
    try:
        # Validate URL first
        if not is_valid_url(url):
            raise ValueError("Invalid URL format")
        
        # Add https:// if no scheme is provided
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Set a user agent to avoid being blocked by some websites
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Make request to the URL
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements (they don't contain visible text)
        for script in soup(['script', 'style']):
            script.decompose()
        
        # Get text from the page
        text = soup.get_text()
        
        # Clean up the text (remove extra whitespace and newlines)
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        if not text.strip():
            raise ValueError("No readable content found on the page")
        
        return text
    
    except requests.exceptions.Timeout:
        raise Exception("Request timed out. The website took too long to respond.")
    except requests.exceptions.ConnectionError:
        raise Exception("Connection error. Please check your internet and the URL.")
    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP Error: {e.response.status_code}")
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception(f"Error scraping URL: {str(e)}")


def get_page_title(url: str) -> str:
    """
    Extract the page title from a URL.
    
    Args:
        url: The URL to scrape
    
    Returns:
        The page title or empty string if not found
    """
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to get title from title tag
        title = soup.find('title')
        if title:
            return title.string
        
        # Try to get h1 as fallback
        h1 = soup.find('h1')
        if h1:
            return h1.get_text()
        
        return ""
    except Exception:
        return ""
