print("hello")
print("world")

# 명령어로 파일 만들기 = touch 파일명.py
# 명령어로 폴더(directory) 만들기 = mkdir 폴더명 
# 폴더에 들어가는 명령어 cd 폴더명
# 파이썬은 R과는 다르게 맨 밑의 값으로 수정되는 게 아니라서, 지정 값을 찾아서 항상 바꿔줘야함

# [숫자형 연산]
a = 30
# =은 대입 / ==은 '같다' / !=은 '아니다' / print () ()안의 결과값 출력하는 명령어
print (a)
b = 4
print ( a + b )
print ( a - b )
print ( a * b )
print ( a / b ) 
print ( a ** 3)
print ( a ** b)  
# a ** b = A를 B만큼 제곱
print ( a // b )
# a // b = a를 b로 나눈 값의 몫만 표시
print ()


#[문자형(스트링형) 연산]
# (1)
#a라는 글자를 내고 싶을 땐 "a"
print ("a")
print ("a" * 3)
first = "호영이"
second = "존잘"
print (first + second)
# print (first + second) = 호영이존잘 -> "호영이 존잘"로 만들어주고 싶을 떈? 방법 2가지
# 방법 1 : jump = " " 로 지정 후, print ( first + jump + second)
# 방법 2 : 그냥 " " 중간에 넣기 => print ( first + " " + second)
print ( first + " " + second)

# (2) 문장열 인덱싱 
#    1)
sen = "안녕하세요 저는 임호영 입니다"
print (len(sen))
# print (len(sen)) = 16 => 띄어쓰기까지 포함

# 다섯 번째 글자(= " " <= 파이썬에서 수 셀때는 0부터 시작하기 때문)
# 안녕하세요  저는 ...
# 0 1 2 3 4 5 6 7 ...
# 다섯 번째 글자를 찾는 명령어 sen[5]
print (sen[5])
print (sen[3])
# sen에서 "세요"를 뽑고 싶을 때 => sen[3:5]
# ★☆★☆  왜 3:4가 아닐까? => 파이썬에서는 A:B = A부터 B앞 까지!
print (sen[3:5])
#print (sen[3:4]) = "세"

#sen에서 마지막 글자만 뽑는 방법 => 마지막 글자 = 뒤에서 1번째!!(뒤에서 부터는 0이 아닌 1부터 셈, -0은 0과 같다고 보기 때문)
#  => sen[-1]
print (sen[-1])

# 2)
word = "임호영은 바보입니다"
print (word[:5] + "천재" + word[-3:])
# [-3:] <= [A:B] A~B : //// print (word[:-3]) = 임호영은 바보 //// print (word[-3:]) = 입니다 ////