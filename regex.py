import re

def extract_data(text):
    patterns = {
        "Emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        "Phone Numbers": r'(\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]\d{4}',
        "Credit Card Numbers": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
        "Time (12/24-hour)": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    }

    results = {}
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        # For phone numbers, flatten tuple results
        if label == "Phone Numbers":
            matches = [match[0] if isinstance(match, tuple) else match for match in matches]
        results[label] = matches
    return results

def main():
    print(" Welcome to Jean Philippe's  Regex Data Finder/Extractor")
    user_input = input("Enter or paste your text: \n")
    print("\nAnalyzing...\n")

    results = extract_data(user_input)

    for category, matches in results.items():
        print(f"{category}:")
        if matches:
            for item in matches:
                print(f"  - {item}")
        else:
            print("  No matches found.")
        print()

if __name__ == "__main__":
    main()

