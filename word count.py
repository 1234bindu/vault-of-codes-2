from collections import Counter
import string

def count_word_frequencies(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split text into words
    words = text.split()

    # Count word frequencies
    word_freq = Counter(words)
    
    return word_freq

# Example text
sample_text = """
This is an example sentence. This sentence demonstrates how to count word frequencies in a given text.
"""

# Count word frequencies in the sample text
word_frequencies = count_word_frequencies(sample_text)

# Print word frequencies
for word, frequency in word_frequencies.items():
    print(f'Word: {word}, Frequency: {frequency}')
