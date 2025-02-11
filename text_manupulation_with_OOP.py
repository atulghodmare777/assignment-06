import re
from collections import Counter

class TextProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def clean_text(self, text):
        return re.sub(r'[^a-zA-Z\s]', '', text).lower()

    def get_word_frequencies(self, text):
        words = text.split()
        word_counts = Counter(words)
        return word_counts.most_common(5)

    def process_text(self):
        raw_text = self.read_file()
        cleaned_text = self.clean_text(raw_text)
        return self.get_word_frequencies(cleaned_text)

if __name__ == "__main__":
    processor = TextProcessor("input.txt")
    top_words = processor.process_text()
    
    for word, count in top_words:
        print(f"{word}: {count}")
