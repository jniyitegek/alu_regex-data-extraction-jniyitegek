import unittest
from regex_extractor import RegexExtractor

class TestRegexExtractor(unittest.TestCase):
    """Test cases for the RegexExtractor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = RegexExtractor()
        
    def test_email_extraction(self):
        """Test email address extraction."""
        text = """
        Valid emails: user@example.com, firstname.lastname@company.co.uk, john.doe123@sub.domain.org
        Invalid: user@, @example.com, plaintext
        """
        results = self.extractor.extract_data(text, 'email')
        self.assertEqual(len(results), 3)
        self.assertIn('user@example.com', results)
        self.assertIn('firstname.lastname@company.co.uk', results)
        self.assertIn('john.doe123@sub.domain.org', results)
        
    def test_url_extraction(self):
        """Test URL extraction."""
        text = """
        Valid URLs: https://www.example.com, https://subdomain.example.org/page, http://test.com/path?query=123
        Invalid: www.example.com, https://, http://
        """
        results = self.extractor.extract_data(text, 'url')
        self.assertEqual(len(results), 3)
        self.assertIn('https://www.example.com', results)
        self.assertIn('https://subdomain.example.org/page', results)
        self.assertIn('http://test.com/path?query=123', results)
        
    def test_phone_extraction(self):
        """Test phone number extraction."""
        text = """
        Valid phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
        Invalid: 1234567890, 123 456 7890, (123)4567890
        """
        results = self.extractor.extract_data(text, 'phone')
        self.assertEqual(len(results), 3)
        self.assertIn('(123) 456-7890', results)
        self.assertIn('123-456-7890', results)
        self.assertIn('123.456.7890', results)
        
    def test_credit_card_extraction(self):
        """Test credit card number extraction."""
        text = """
        Valid credit cards: 1234 5678 9012 3456, 1234-5678-9012-3456, 1234567890123456
        Invalid: 1234-5678-9012, 1234 5678 9012, 1234-5678-9012-345
        """
        results = self.extractor.extract_data(text, 'credit_card')
        self.assertEqual(len(results), 2)
        self.assertIn('1234 5678 9012 3456', results)
        self.assertIn('1234-5678-9012-3456', results)
        
    def test_time_extraction(self):
        """Test time format extraction."""
        text = """
        Valid times: 14:30, 2:30 PM, 9:05 am, 23:59, 00:00
        Invalid: 25:00, 14:60, 9:5 AM
        """
        results = self.extractor.extract_data(text, 'time')
        self.assertEqual(len(results), 5)
        self.assertIn('14:30', results)
        self.assertIn('2:30 PM', results)
        self.assertIn('9:05 am', results)
        self.assertIn('23:59', results)
        self.assertIn('00:00', results)
        
    def test_html_tag_extraction(self):
        """Test HTML tag extraction."""
        text = """
        Valid HTML tags: <p>, <div class="example">, <img src="image.jpg" alt="description">
        Invalid: <, >, </>
        """
        results = self.extractor.extract_data(text, 'html_tag')
        self.assertEqual(len(results), 3)
        self.assertIn('<p>', results)
        self.assertIn('<div class="example">', results)
        self.assertIn('<img src="image.jpg" alt="description">', results)
        
    def test_hashtag_extraction(self):
        """Test hashtag extraction."""
        text = """
        Valid hashtags: #example, #ThisIsAHashtag, #123_tag
        Invalid: # tag, #, tag#
        """
        results = self.extractor.extract_data(text, 'hashtag')
        self.assertEqual(len(results), 3)
        self.assertIn('#example', results)
        self.assertIn('#ThisIsAHashtag', results)
        self.assertIn('#123_tag', results)
        
    def test_currency_extraction(self):
        """Test currency amount extraction."""
        text = """
        Valid currency: $19.99, $1,234.56, $0.99, $1,000,000.00
        Invalid: $19, 19.99, $19.9, $1,234.5
        """
        results = self.extractor.extract_data(text, 'currency')
        self.assertEqual(len(results), 4)
        self.assertIn('$19.99', results)
        self.assertIn('$1,234.56', results)
        self.assertIn('$0.99', results)
        self.assertIn('$1,000,000.00', results)
        
    def test_extract_all_data(self):
        """Test extraction of all data types at once."""
        text = """
        Mixed data: user@example.com, https://www.example.com, (123) 456-7890, 
        1234 5678 9012 3456, 14:30, <p>Hello</p>, #example, $19.99
        """
        results = self.extractor.extract_all_data(text)
        self.assertGreaterEqual(len(results['email']), 1)
        self.assertGreaterEqual(len(results['url']), 1)
        self.assertGreaterEqual(len(results['phone']), 1)
        self.assertGreaterEqual(len(results['credit_card']), 1)
        self.assertGreaterEqual(len(results['time']), 1)
        self.assertGreaterEqual(len(results['html_tag']), 1)
        self.assertGreaterEqual(len(results['hashtag']), 1)
        self.assertGreaterEqual(len(results['currency']), 1)
        

if __name__ == '__main__':
    unittest.main()
