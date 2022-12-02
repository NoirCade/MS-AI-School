# 딕셔너리 특성 행렬로 변환
import pandas as pd
from sklearn.feature_extraction import DictVectorizer

data_dict = [{"Red": 2, "Blue": 4},
            {"Red": 4, "Blue": 3},
            {"Red": 1, "Yellow": 2},
            {"Red": 2, "Yellow": 2}]

# print(data_dict)

dictvectorizer = DictVectorizer(sparse=False)
# 0이 아닌 원소만 저장하는 희소 행렬을 반환
# 딕셔너리를 특성 행렬로 변환
features = dictvectorizer.fit_transform(data_dict)
features_names = dictvectorizer.get_feature_names() # 특성 이름 획득
# print(features_names)
dict_data = pd.DataFrame(features, columns=features_names)
print(dict_data)

## 행렬 형태로 변경
# 단어 카운트 딕셔너리 만들기
doc_1_word_counter = {"Red": 2, "Blue": 4}
doc_2_word_counter = {"Red": 4, "Blue": 4}
doc_3_word_counter = {"Red": 1, "Yellow": 2}
doc_4_word_counter = {"Red": 2, "Yellow": 2}
doc_word_counts = [doc_1_word_counter, doc_2_word_counter,
                    doc_3_word_counter, doc_4_word_counter]
print(doc_word_counts)

data_array = dictvectorizer.fit_transform(doc_word_counts)
print(data_array)