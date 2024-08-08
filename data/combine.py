def combine_files(english_file, tamil_file, output_file):
    with open(english_file, 'r', encoding='utf-8') as eng, \
         open(tamil_file, 'r', encoding='utf-8') as tam, \
         open(output_file, 'w', encoding='utf-8') as out:
        
        eng_lines = eng.readlines()
        tam_lines = tam.readlines()

        if len(eng_lines) != len(tam_lines):
            print("Warning: The number of lines in the English and Tamil files do not match.")
        
        for eng_line, tam_line in zip(eng_lines, tam_lines):
            combined_line = f"{eng_line.strip()}\t{tam_line.strip()}\n"
            out.write(combined_line)

if __name__ == '__main__':
    english_file = 'hindi.txt'
    tamil_file = 'kangri.txt'
    output_file = 'combine.txt'
    
    combine_files(english_file, tamil_file, output_file)
    print("Combining complete. Combined file saved as combine.txt.")
