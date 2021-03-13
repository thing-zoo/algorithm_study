x, y = map(int, input().split())

#오늘은 1월 1일 월요일
today = 0
#월별 일자
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#요일
week = ["MON", "TUE", "WED", "THU","FRI", "SAT", "SUN"]

#오늘로 부터 며칠이 지났는지 계산하기
for i in range(x - 1):
    today += month[i]
today += y - 1

#요일 계산하기
today %= 7
print(week[today])