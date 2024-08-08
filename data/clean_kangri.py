import re
import string

def clean_kangri_text(text):
    # Define Kangri-specific punctuation if any (add more if necessary)
    kangri_punctuation = "।"  # Add any other punctuation specific to Kangri if needed
    
    # Remove standard and Kangri-specific punctuation
    all_punctuation = string.punctuation + kangri_punctuation
    text = re.sub(f"[{re.escape(all_punctuation)}]", " ", text)
    
    # Remove digits
    text = re.sub(r'\d+', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split text into sentences (assuming sentences end with "।")
    sentences = text.split('।')
    
    # Remove empty sentences and extra spaces within sentences
    cleaned_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Rejoin sentences to form the cleaned text
    cleaned_text = '। '.join(cleaned_sentences) + '।'
    
    return cleaned_text

def main(input_file, output_file):
    # Load the file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Clean the text
    cleaned_text = clean_kangri_text(text)

    # Save the cleaned text
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"Text cleaning complete. Cleaned text saved to {output_file}")

if __name__ == "__main__":
    input_file = 'kangri.txt'  # Path to the input file
    output_file = 'cleaned_kangri.txt'  # Path to the output file
    main(input_file, output_file)
