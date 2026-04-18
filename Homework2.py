# class TextDataset:
#     def __init__(self, texts):
#         self.texts = texts

#     def get_texts(self):
#         return self.texts


# class Preprocessor:
#     def process(self, texts):
#         processed = []
#         for text in texts:
#             # lower + удаление лишних пробелов
#             clean = text.lower().strip()
#             clean = " ".join(clean.split())
#             processed.append(clean)
#         return processed


# class Analyzer:
#     def analyze(self, texts):
#         word_freq = {}
#         unique_words = set()

#         for text in texts:
#             words = text.split()
#             for word in words:
#                 # считаем частоты
#                 word_freq[word] = word_freq.get(word, 0) + 1
#                 unique_words.add(word)

#         return word_freq, unique_words


# # ---- Pipeline ----
# if __name__ == "__main__":
#     data = TextDataset([
#         "Hello   world",
#         "Hello Python",
#         "  Python   world  "
#     ])

#     preprocessor = Preprocessor()
#     analyzer = Analyzer()

#     texts = data.get_texts()
#     processed_texts = preprocessor.process(texts)
#     word_freq, unique_words = analyzer.analyze(processed_texts)

#     print("Обработанные тексты:", processed_texts)
#     print("Частоты слов:", word_freq)
#     print("Уникальные слова:", unique_words)
