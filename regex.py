import re
import sys

class RegexExtractor:
    """
    A class that provides methods to extract various data types using regex patterns.
    """
    
    def __init__(self):
        # Define regex patterns for different data types
        self.patterns = {
            # Email addresses
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            
            # URLs
            'url': r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)',
            
            # Phone numbers
            'phone': r'(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]?\d{4}',
            
            # Credit card numbers
            'credit_card': r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
            
            # Time formats
            'time': r'(?:1[0-2]|0?[1-9]):[0-5][0-9]\s*(?:AM|PM|am|pm)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9]',
            
            # HTML tags
            'html_tag': r'<[^>]+>',
            
            # Hashtags
            'hashtag': r'#[a-zA-Z0-9_]+',
            
            # Currency amounts
            'currency': r'\$\d{1,3}(?:,\d{3})*\.\d{2}'
        }
        
    def extract_data(self, text, data_type):
        """
        Extract data of specified type from input text.
        
        Args:
            text (str): Input text to search for patterns
            data_type (str): Type of data to extract (must be a key in self.patterns)
            
        Returns:
            list: List of extracted items
        """
        if data_type not in self.patterns:
            raise ValueError(f"Unknown data type: {data_type}")
        
        pattern = self.patterns[data_type]
        matches = re.findall(pattern, text)
        return matches
    
    def extract_all_data(self, text):
        """
        Extract all supported data types from input text.
        
        Args:
            text (str): Input text to search for patterns
            
        Returns:
            dict: Dictionary with data types as keys and lists of extracted items as values
        """
        results = {}
        for data_type in self.patterns:
            results[data_type] = self.extract_data(text, data_type)
        return results


def main():
    """
    Main function for command-line execution.
    """
    if len(sys.argv) < 3:
        print("Usage: python regex_extractor.py <data_type> <text>")
        print("Available data types: email, url, phone, credit_card, time, html_tag, hashtag, currency")
        return
    
    data_type = sys.argv[1]
    text = sys.argv[2]
    
    extractor = RegexExtractor()
    
    try:
        results = extractor.extract_data(text, data_type)
        print(f"Found {len(results)} {data_type} matches:")
        for i, match in enumerate(results, 1):
            print(f"{i}. {match}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

