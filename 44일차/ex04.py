# 품사 태깅
import nltk
from nltk import pos_tag
from nltk import word_tokenize

# 태거 다운로드
nltk.download('averaged_perceptron_tagger')
# 샘플 텍스트 데이터 생성
text_data = 'Chris loved outdoor running every morning'

# 사전 훈련된 품사 태깅을 사용
text_tagged = pos_tag(word_tokenize(text_data))
print(text_tagged)

"""
결과: [('Chris', 'NNP'), ('loved', 'VBD'), ('outdoor', 'RP'), ('running', 'VBG'), ('every', 'DT'), ('morning', 'NN')]
"""