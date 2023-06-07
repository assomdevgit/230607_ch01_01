# 주석 (commnet, 메모 같은 것)
# - 파이썬에서 사람만 알아볼 수 있도록 작성하는 부분
# - 즉, 주석은 파이썬 인터프리터(실행기)가 처리하지 않으므로
# 프로그램 실행에 영향을 주지 않음 (ctrl + /)로 주석 표시
# - 보통 주석은 코드에 대한 자세한 설명을 작성하거나, 특정 코드를 임시로 사용하지 않도록 할 때 사용
# - 주석은 '한 줄 주석'과 '블록 주석' 두 가지가 있음


# 한 줄 주석
print("한 줄 주석") # 코드 뒤에 이어서 주석

# - 코드 맨 앞에 #을 사용하면 해당 줄은 모두 주석이 됨.
# print("작동하지 않는 print")

# - 코드 뒤에 #으로 주석을 작성할 수도 있음
print("안녕") # print("Hello")
# print("안녕")  print("Hell") <-- 오류 코드

# [블럭 주석]
# 여러 줄 주석을 작성할 때 #이 아니라 ''' 혹은 """를 사용하기도 함.
'''
print("블럭 주석!")
'''
"""
print("블럭 주석!!!")
"""