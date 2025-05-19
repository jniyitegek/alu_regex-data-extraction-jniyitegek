# My regular Expressions Data extraction Tool

Hello, This tool mainly uses Python language and a python script that uses **regular expressions (RegEx)** to extract useful data patterns from any text input provided by the user. What you need is to paste or type data and It will tell you what type of data your text was having.

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
- currency
- and finally the hashtags #

##  How to Run

### Requirements:
- Python 3.x

### Steps:
1. Clone this repository:
    ```bash
    git clone https://github.com/jniyitegek/alu_regex-data-extraction-jniyitegek.git
    cd alu_regex-data-extraction-jniyitegek
    ```

2. Run the script:
    ```bash
    python3 regex.py
    ```

3. Paste or type your text when prompted.

## Enjoy!
