# 텍스트 데이터 처리 01
import re
text_data = ["Interrobang. By Aishwarya Henriette", 
             "Parking and going. by Kear Gua", 
             "Today Is the night. By Jar par"]

# 공백 제거
strip_whitespace = [string.strip() for string in text_data]
print("공백 제거 >>> ", strip_whitespace)

# 마침표 제거
remove_periods = [string.replace(".", "") for string in strip_whitespace]
print("마침표 제거 >>> ", remove_periods)

# 소문자를 대문자로 변환
def capitalizer(string: str) -> str: return string.upper()

temp = [capitalizer(string) for string in remove_periods]
print("대문자 전환 >>> ", temp)

def replace_letters_with_X(string: str) -> str :
    return re.sub(r"[a-zA-Z]", "X", string)

data = [replace_letters_with_X(string) for string in remove_periods]
print ("모든 문자 X로 변환 >>>", data)