# 텍스트 데이터 처리 02
# 구두점 삭제
# 구두점 글자의 딕셔너리를 만들어 translate() 적용
import unicodedata
import sys

text_data = ["HI!!!!!!! I. love. this. Song....!",
              "100000%%% Agreee??? #KK",
              "Left??!?!!@@"]   # 구두점이 포함된 데이터 생성

punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P'))

# 잘 부여됐는지 확인
# print(punctuation)

test = [string.translate(punctuation) for string in text_data]
print(test)