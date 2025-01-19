import re

class WordsFinder:
    file_names = []
    __symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']


    def __init__(self, *files):
        for name in files:
            self.file_names.append(name)



    def get_all_words(self):
        self.all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                vol = []
                for line in file:
                    line = line.lower()
                    for sym in self.__symbols:
                        line = line.replace(sym, '')
                    vol += line.split()
                self.all_words[name] = vol
        return self.all_words

    def find(self, word):
        word_ = word.lower()
        result = {}
        for key, words in self.all_words.items():
            index = 1
            for word_in_dict in words:
                if word_ == word_in_dict:
                    result[key] = index
                    break
                index += 1
        return result

    def count(self, word):
        word_ = word.lower()
        result = {}
        for key, words in self.all_words.items():
            count = 0
            for word_in_dict in words:
                if word_ == word_in_dict:
                    count += 1
            result[key] = count
        return result


# finder2 = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt')
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print(finder2.count('if'))  # 4 слова teXT в тексте всего
