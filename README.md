# Hindi Text Summarizer using TextRank Algorithm

A Python-based text summarization system specifically designed for Hindi text using the TextRank algorithm. This project implements an extractive summarization approach that identifies and extracts the most important sentences from Hindi text documents.

## 🚀 Features

- **Hindi Text Processing**: Specifically designed for Hindi language text summarization
- **TextRank Algorithm**: Uses the TextRank algorithm for sentence ranking and selection
- **Extractive Summarization**: Extracts key sentences rather than generating new text
- **Configurable Summary Length**: Adjustable summary ratio (default: 30% of original text)
- **Batch Processing**: Process multiple input files automatically
- **Evaluation System**: Includes evaluation metrics and comparison with human summaries

## 📋 Requirements

- Python 3.6+
- networkx
- numpy
- scikit-learn
- nltk

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Devarshi0808/Hindi-Text-Summarizer-using-TextRank-Algorithm-main.git
cd Hindi-Text-Summarizer-using-TextRank-Algorithm-main
```

2. Install required dependencies:
```bash
pip install networkx numpy scikit-learn nltk
```

## 📁 Project Structure

```
Hindi-Text-Summarizer-using-TextRank-Algorithm-main/
├── summarizer_fixed.py          # Main summarization script
├── summarizer.py                # Original summarizer implementation
├── hindi_tokenizer1.py          # Hindi text tokenization utilities
├── mainEval.py                  # Original evaluation script (Windows-specific)
├── mainEval_fixed.py            # Fixed evaluation script (cross-platform)
├── stopwords.txt                # Hindi stopwords list
├── IO/
│   ├── input/                   # Input text files (input1.txt to input10.txt)
│   ├── machine_output/          # Generated summaries
│   └── human_output/            # Human reference summaries
└── README.md                    # This file
```

## 🎯 Usage

### Basic Usage

Run the main summarizer to process all input files:

```bash
python3 summarizer_fixed.py
```

This will:
1. Process all files in `IO/input/` directory
2. Generate summaries using the TextRank algorithm
3. Save results to `IO/machine_output/` directory

### Custom Usage

You can also use the summarizer function directly in your code:

```python
from summarizer_fixed import summarize_hindi_text

# Your Hindi text
text = "यह एक हिंदी पाठ है जिसे संक्षिप्त करना है।"

# Generate summary (30% of original length by default)
summary = summarize_hindi_text(text, summary_ratio=0.3)
print(summary)
```

### Evaluation

To evaluate the generated summaries against human reference summaries:

```bash
python3 mainEval_fixed.py
```

The evaluation script will:
- Compare machine-generated summaries with human reference summaries
- Calculate precision, recall, and F1 scores
- Display individual and average F1 scores

**Note**: Use `mainEval_fixed.py` for cross-platform compatibility. The original `mainEval.py` is Windows-specific and requires additional dependencies.

## 🔧 How It Works

1. **Text Preprocessing**: 
   - Cleans the input text
   - Splits text into sentences using Hindi sentence boundaries (।)
   - Removes empty sentences

2. **Feature Extraction**:
   - Creates TF-IDF vectors for each sentence
   - Builds a similarity matrix between sentences

3. **Graph Construction**:
   - Converts similarity matrix to a NetworkX graph
   - Applies PageRank algorithm to rank sentences

4. **Summary Generation**:
   - Selects top-ranked sentences based on summary ratio
   - Maintains original sentence order
   - Combines selected sentences into final summary

## 📊 Evaluation Results

The system includes evaluation capabilities that compare machine-generated summaries with human reference summaries using:

- **Precision**: Ratio of correctly identified important sentences
- **Recall**: Ratio of important sentences that were captured
- **F1 Score**: Harmonic mean of precision and recall

### Sample Evaluation Results

Recent evaluation on 10 test articles showed:
- **Average F1 Score**: 0.6303 (63.03%)
- **Individual F1 Scores**: Ranging from 0.4286 to 0.7273
- **Best Performance**: Articles 6 and 8 (F1 = 0.7273)

This indicates good performance in identifying and extracting important sentences from Hindi text.

## 📝 Input Format

Input files should contain Hindi text in UTF-8 encoding. The system automatically processes files named `input1.txt` through `input10.txt` in the `IO/input/` directory.

## 📤 Output Format

Generated summaries are saved as:
- `article1_system1.txt` through `article10_system1.txt`
- Located in `IO/machine_output/` directory
- UTF-8 encoded Hindi text

## 🎛️ Configuration

You can adjust the summarization parameters:

- **summary_ratio**: Controls the length of the summary (default: 0.3 = 30%)
- **sentence_selection**: Currently uses top-ranked sentences, can be modified for different selection strategies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Devarshi0808**

## 🙏 Acknowledgments

- TextRank algorithm implementation based on research by Mihalcea and Tarau
- Hindi text processing utilities
- Evaluation metrics implementation

---

**Note**: This project is specifically designed for Hindi text summarization and may not work optimally with other languages without modifications. 