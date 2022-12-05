from nltk.stem.porter import PorterStemmer

# 단어 토큰 생성
tokenized_words = ['I', 'am', 'the', 'Ironman',
                   'I', 'loved', 'Newyork', 'citizens',
                   'It\'s', 'time', 'to', 'go']

# 어간 추춬기를 만들기
porter = PorterStemmer()

word_list = []

# 어간 추출기를 적용합니다
for word in tokenized_words:
    word_list.append(porter.stem(word))

print((word_list))