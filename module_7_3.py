class WordsFinder:
    def __new__(cls, *name):
        for i in name:
            cls.file_names.append(i)
        return super().__new__(cls)

    file_names = []

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            all_words[name] = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(char, '')
                    line = line.split()
                    for wd in line:
                        all_words[name].append(wd)
        return all_words

    def find(self, word):
        get_find = {}
        for name, words in self.get_all_words().items():
            number = 0
            for value in words:
                number += 1
                if word.lower() == value:
                    get_find[name] = number
                    break
        return get_find

    def count(self, word):
        get_coint = {}
        for name, words in self.get_all_words().items():
            number = 0
            for value in words:
                if word.lower() == value:
                    number += 1
                    get_coint[name] = number
        return get_coint


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')

print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего