# 내장 함수 : format()

# format(데이터, 서식형식)
from builtins import int, input

print(4)
print(format(4, '10d'))            # 정수를 출력하는 10자리
print(format(4.3, '10.3f'))        # 실수를 출력하는 전체 10자리, 소수점 이하 3자리
print(format(42.195, '.3f'))       # 소숫점 3자리까지 출력 : 42.195
print(format(42.195678, '.3f'))    # 소숫점 3자리까지 출력 : 42.196
print(format('안녕하세요','s'))

# {숫자}와 format()함수를 이용한 데이터 매핑
print('{0} is {1}'.format('Python', 'fun'))     # Python is fun
# {0}에는 Python이 들어가고 {1}에는 fun이 들어간다.
print('{} is {}'.format('Python', 'fun'))       # Python is fun
# 첫번째 {}에는 Python이 들어가고 두번째 {}에는 fun이 들어간다.
print('{1} is {0}'.format('Python', 'fun'))     # fun is Python
# 첫번째 {0}에는 Python이 들어가고 두번째 {1}에는 fun이 들어간다.
# 숫자가 {}안에 들어갈때는 각 순서에 해당되는 값이 들어간다.

# 키보드로 입력한 문자를 format()함수로 출력
name = input('이름을 입력하세요?')      # 이름을 입력하세요?안화수
job = input('직업을 입력하세요?')       # 직업을 입력하세요?개발자

print('{0} is a {1}'.format(name, job))         # 안화수 is a 개발자
print('{} is a {}'.format(name, job))           # 안화수 is a 개발자
print('{1} is a {0}'.format(name, job))         # 개발자 is a 안화수
print('{j} is a {n}'.format(n=name, j=job))     # 개발자 is a 안화수




