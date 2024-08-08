import re
import string

def clean_hindi_text(text):
    # Define Hindi-specific punctuation if any (add more if necessary)
    hindi_punctuation = "।"  # Add any other punctuation specific to Hindi if needed
    
    # Remove standard and Hindi-specific punctuation
    all_punctuation = string.punctuation + hindi_punctuation
    text = re.sub(f"[{re.escape(all_punctuation)}]", " ", text)
    
    # Remove digits
    text = re.sub(r'\d+', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split text into sentences (assuming sentences end with "।")
    sentences = text.split('।')
    
    # Remove empty sentences and extra spaces within sentences
    cleaned_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return cleaned_sentences

def main(input_file, output_file):
    # Load the file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Clean the text
    cleaned_sentences = clean_hindi_text(text)

    # Save the cleaned text, keeping sentences separate
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in cleaned_sentences:
            file.write(sentence + "।\n")

    print(f"Text cleaning complete. Cleaned text saved to {output_file}")

if __name__ == "__main__":
    input_file = 'hindi.txt'  # Path to the input file
    output_file = 'cleaned_hindi.txt'  # Path to the output file
    main(input_file, output_file)
