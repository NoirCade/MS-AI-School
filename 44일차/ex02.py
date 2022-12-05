# 자주 등장하지만 유용한 정보가 없는 '불용어'를 제거하기(sklearn에도 300여개의 불용어 리스트 지원)
from nltk.corpus import stopwords
import nltk

# 불용어 데이터를 다운로드(현재 179개)
nltk.download('stopwords')

# 단어 토큰 생성
tokenized_words = ['I', 'am', 'the', 'Ironman', 'It\'s', 'time', 'to', 'go']

# 불용어 로드
stop_words = stopwords.words('english')
print("불용어 리스트 길이 >> ", len(stop_words))
print("불용어 리스트 >> ", stop_words)

for word in tokenized_words:
    if word not in stop_words:
        print(word)
# [word for word in tokenized_words if word not in stop_words]