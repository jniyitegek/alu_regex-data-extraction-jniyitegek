# 🔍 Regex Data Extraction Tool

This is a Python script that uses **regular expressions (RegEx)** to extract useful data patterns from any text input provided by the user.

## Features

This tool identifies and extracts the following from a block of text:
- Email addresses (e.g. `user@example.com`)
- Phone numbers (e.g. `(123) 456-7890`, `123-456-7890`)
- Credit card numbers (e.g. `1234-5678-9012-3456`)
- Time values in 12-hour or 24-hour format (e.g. `14:30`, `2:30 PM`)

## Input

You can copy-paste or type any text into the terminal when prompted. The program will scan and display any matched patterns based on RegEx rules.

## Output

After analyzing the text, the tool prints a categorized list of all matches found for:
- Emails
- Phone Numbers
- Credit Card Numbers
- Time (12/24-hour)

##  How to Run

### Requirements:
- Python 3.x

### Steps:
1. Clone this repository:
    ```bash
    git clone https://github.com/{YourUsername}/alu_regex-data-extraction-{YourUsername}.git
    cd alu_regex-data-extraction-{YourUsername}
    ```

2. Run the script:
    ```bash
    python extractor.py
    ```

3. Paste or type your text when prompted.

## File Structure

```plaintext
alu_regex-data-extraction-{YourUsername}/
├── extractor.py       # Main Python script
└── README.md          # Project documentation
