from rouge import Rouge

def calculate_rouge_scores(hypothesis, reference):
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference)
    return scores

def main():
    hypotheses = [
        "मैं मैं मैं क्या",
        "मैं मैं क्या"
    ]
    
    references = [
        "ग़ज़ल .",
        "प्रत्यूष गुलेरी"
    ]
    
    for i, (hyp, ref) in enumerate(zip(hypotheses, references), start=1):
        print(f"Sentence pair {i}:")
        scores = calculate_rouge_scores(hyp, ref)
        
        print(f"Hypothesis: {hyp}")
        print(f"Reference: {ref}")

        # The scores variable is a list of dictionaries
        rouge_1_f1 = scores[0]['rouge-1']['f']
        rouge_2_f1 = scores[0]['rouge-2']['f']
        rouge_l_f1 = scores[0]['rouge-l']['f']
        
        print(f"ROUGE-1 F1: {rouge_1_f1:.4f}")
        print(f"ROUGE-2 F1: {rouge_2_f1:.4f}")
        print(f"ROUGE-L F1: {rouge_l_f1:.4f}")
        print()

if __name__ == "__main__":
    main()
