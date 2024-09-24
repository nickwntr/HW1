
class WordsFinder:
    def __init__(self,*files):
        self.all_words = {}
        self.file_names = files

    def get_all_words(self):
        for fname in self.file_names:
            with open(fname,encoding='utf-8') as file:
                for line in file:
                    nline = line.replace(',',' ').lower()
                    nline = nline.replace('.',' ')
                    nline = nline.replace('=',' ')
                    nline = nline.replace('!',' ')
                    nline = nline.replace('?',' ')
                    nline = nline.replace(';',' ')
                    nline = nline.replace(':',' ')
                    nline = nline.replace(' - ',' ')
                    nline = nline.split()
            self.all_words[fname] = nline
        print("Полученыны слова")
        return self.all_words

    def find(self,toFind):
        print(f"Поиск позиции слова {toFind}")
        findict = {}
        for name,words in self.all_words.items():
            findex = 1
            for word in words:
                if word.lower() == toFind.lower():
                    findict[name] = findex
                    break
                else: findex += 1
            if findex > len(words):
                findict[name] = "Не найдено"

        return findict


    def count(self,toFind):
        print(f"Поиск количество упоминаний слова {toFind}")
        coutdict = {}
        for name, words in self.all_words.items():
            cindex = 0
            for word in words:
                if word.lower() == toFind.lower():
                    cindex += 1
            coutdict[name] = cindex
        return coutdict