def loadDict(path):
    Dict = {}
    with open(path, 'r', encoding='utf-8') as file_dict:
        for line in file_dict:
            items = line.strip().split('\t')
            word = items[0]
            message = " ".join(items[1:])
            Dict[word] = message
    return Dict

def getIrregularNounDict():
    from bs4 import BeautifulSoup as soup
    from urllib import request, parse
    import re
    url = "https://zh.wiktionary.org/zh-hans/" + parse.quote("附录:英语不规则复数")
    webPage = request.urlopen(url)
    content = soup(webPage.read(), 'html.parser').find('div', id='bodyContent')
    with open('dict_noun.txt', 'w') as file_noun:
        for li in content.findAll('li'):
            text = li.text.strip()
            if not '→' in text:
                continue
            colomn = text.rstrip('*').split('→')
            singular = colomn[0].strip()
            plura = colomn[1].strip()
            for word in re.split(',|/', plura):
                file_noun.write(word.strip() + '\t' + singular + '\n')

def getIrregularVerbDict():
    from bs4 import BeautifulSoup as soup
    from urllib import request
    url = "https://baike.baidu.com/item/%E8%8B%B1%E8%AF%AD%E4%B8%8D%E8%A7%84%E5%88%99%E5%8A%A8%E8%AF%8D%E8%A1%A8/1619648?fr=aladdin"
    webPage = request.urlopen(url)
    content = soup(webPage.read(), "html.parser")
    tags = content.find('table', class_='table-view log-set-param')
    with open('dict_verb.txt', 'w') as file_verb:
        for tr in tags.findAll('tr')[1:]:
            colomn = tr.findAll('td')
            infinitive = colomn[0].text.strip()
            paste = colomn[1].text.strip()
            for word in paste.split(','):
                file_verb.write(word.strip() + '\t' + infinitive + '\n')

def loadVerbDict(path):
    Dict = {}
    with open(path, 'r', encoding='utf-8') as file_dict:
        for line in file_dict:
            words = line.strip().split('\t')
            Dict[words[0]] = words[1]
    return Dict

def loadNounDict(path):
    Dict = {}
    with open(path, 'r', encoding='utf-8') as file_dict:
        for line in file_dict:
            words = line.strip().split('\t')
            Dict[words[0]] = words[1]
    return Dict

def inDict(word, dict):
    if word in dict.keys():
        return True
    else:
        return False
        return False

def nounLemma(word, dict):
    if word[-3:] == 'ves':
        if word[:-3] + 'f' in dict.keys():
            return word[:-3] + 'f'
        elif word[:-3] + 'fe' in dict.keys():
            return word[:-3] + 'fe'
    elif word[-3:] == 'ies':
        if word[:-3] + 'y' in dict_keys():
            return word[:-3] + 'y'
    elif word[-2:] == 'es':
        if word[:-2] in dict.keys():
            return word[:-2]
    elif word[-1] == 's':
        if word[:-1] in dict.keys():
            return word[:-1]
    else:
        return None
            
def verLemma(word, dict):
    if word[-3:] == 'ies':
        if word[:-3] + 'y' in dict.keys():
            return word[:-3] + 'y'
    elif word[-2:] == 'es':
        if word[:-2] in dict.keys():
            return word[:-2]
    elif word[-1] == 's':
        if word[:-1] in dict.keys():
            return word[:-1]
    elif word[-3:] == 'ing':
        if word[-4] == word[-5] and word[:-4] in dict.keys():
            return word[:-4]
        elif word[-4] == 'y' and word[:-4] + 'ie' in dict.keys():
            return word[:-4] + 'ie'
        elif word[:-3] in dict.keys():
            return word[:-3]
        elif word[:-3] + 'e' in dict.keys():
            return word[:-3] + 'e'
    elif word[-2:] == 'ed':
        if word[-3] == word[-4] and word[:-3] in dict.keys():
            return word[:-3]
        elif word[-3] == 'i' and word[:-3] + 'y' in dict.keys():
            return word[:-3] + 'y'
        elif word[:-2] in dict.keys():
            return word[:-2]
        elif word[:-2] + 'e' in dict.keys():
            return word[:-2] + 'e'
    else:
        return None    

def lemma(word, dict):
    word_lemma = nounLemma(word, dict)
    if word_lemma:
        return word_lemma
    else:
        return verLemma(word, dict)

def main():
    #   getIrregularNounDict()
    #   getIrregularVerbDict()
    dic_all = loadDict("dict.txt")
    dic_verb = loadVerbDict("dict_verb.txt")
    dic_noun = loadNounDict('dict_noun.txt')
    while(1):
        inputWord = input("please input an English word: ")
        if inDict(inputWord, dic_all):
            print(inputWord + " : " + dic_all[inputWord])
        elif inDict(inputWord, dic_noun):
            print(inputWord + "->" + dic_noun[inputWord] + " : " + dic_all[dic_noun[inputWord]])
        elif inDict(inputWord, dic_verb):
            print(inputWord + "->" + dic_verb[inputWord] + " : " + dic_all[dic_verb[inputWord]])
        else:
            word_lemma = lemma(inputWord, dic_all)
            if word_lemma :
                print(inputWord + "->" + word_lemma + " : " + dic_all[word_lemma])
            else:
                print("<未登录词模块>")

if __name__ == "__main__":
    main()