import networkx as nx
import numpy as np
import math
import re
import os
from pathlib import Path

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def summarize_hindi_text(text, summary_ratio=0.3):
    """
    Summarize Hindi text using TextRank algorithm
    
    Args:
        text (str): Input Hindi text
        summary_ratio (float): Ratio of sentences to include in summary (default 0.3)
    
    Returns:
        str: Summarized text
    """
    # Clean and tokenize the text
    text = text.replace('\n', ' ')
    text = text.replace(u'?', u'\u0964')
    sentences = text.split(u'\u0964')
    
    # Remove empty sentences
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) < 2:
        return text
    
    # Create TF-IDF matrix
    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)
    
    # Create similarity graph
    similarity_graph = normalized * normalized.T
    
    # Convert to NetworkX graph
    nx_graph = nx.from_scipy_sparse_array(similarity_graph)
    scores = nx.pagerank(nx_graph)
    
    # Rank sentences
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    # Select top sentences based on summary ratio
    num_sentences = max(1, int(math.ceil(summary_ratio * len(ranked_sentences))))
    top_sentences = ranked_sentences[:num_sentences]
    
    # Order sentences by their original position
    sentence_positions = []
    for score, sentence in top_sentences:
        position = sentences.index(sentence)
        sentence_positions.append((position, sentence))
    
    # Sort by original position
    sentence_positions.sort()
    
    # Combine sentences
    summary = u'\u0964'.join([sentence for position, sentence in sentence_positions])
    
    return summary

def process_input_files():
    """
    Process all input files and generate summaries
    """
    # Get current directory
    current_dir = Path(__file__).parent
    io_dir = current_dir / 'IO'
    input_dir = io_dir / 'input'
    
    # Create output directory if it doesn't exist
    output_dir = io_dir / 'machine_output'
    output_dir.mkdir(exist_ok=True)
    
    # Process each input file
    for i in range(1, 11):
        input_file = input_dir / f'input{i}.txt'
        output_file = output_dir / f'article{i}_system1.txt'
        
        if input_file.exists():
            print(f"Processing {input_file}...")
            
            # Read input file
            with open(input_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # Generate summary
            summary = summarize_hindi_text(text)
            
            # Write summary to output file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(summary)
            
            print(f"Summary saved to {output_file}")
        else:
            print(f"Input file {input_file} not found")

def main():
    """
    Main function to run the summarizer
    """
    print("Hindi Text Summarizer using TextRank Algorithm")
    print("=" * 50)
    
    # Process all input files
    process_input_files()
    
    print("\nSummarization complete!")

if __name__ == "__main__":
    main() 