import re

def clean_and_separate_hindi_text(file_path):
    # Read the contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove any unwanted characters (like extra spaces, special symbols, etc.)
    text = re.sub(r'[^\w\s।,?!]', '', text)  # Keep Hindi characters, punctuation, and spaces

    # Normalize multiple spaces to a single space
    text = re.sub(r'\s+', ' ', text).strip()

    # Split the text into sentences using Hindi-specific sentence delimiters
    sentences = re.split(r'(?<=[।?!])\s+', text)

    return sentences

def write_sentences_to_file(sentences, output_path):
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for sentence in sentences:
            output_file.write(sentence.strip() + '\n')

if __name__ == "__main__":
    input_file = 'hindi.txt'        # Input file path
    output_file = 'cleaned_hindi.txt'  # Output file path

    # Get the cleaned and separated sentences
    sentences = clean_and_separate_hindi_text(input_file)

    # Write the sentences to a file, each on a new line
    write_sentences_to_file(sentences, output_file)

    # Optionally, print the sentences to the console
    print("Sentences:")
    for sentence in sentences:
        print(sentence)

    print(f"\nText has been cleaned and saved to {output_file}")
