import turtle
import math
# 스크린 생성
s = turtle.getscreen()
#거북이 변수에 지정, 거북이 초기 설정
t = turtle.Turtle()
t.color("skyblue")
t.shape("turtle")

#시작 점 그리기
t.penup()
t.goto(-300,-300)
t.pendown()
t.circle(30)
t.penup()

#도착점 그리기
t.goto(300,300)
t.pendown()
for i in range(4):
    t.fd(50)
    t.rt(90)
t.penup()

# 장애물 그리기
t.goto(-30,-15)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for i in range(3):
    t.fd(50)
    t.lt(120)
t.end_fill()
t.color("skyblue")
t.penup()
t.goto(-300,-270)

# 시작점에서 도착점으로 장애물 피해서 이동하기
t.pendown()
t.goto(-40, -30)
t.lt(90)
t.fd(20)
t.rt(30)
t.fd(50)
t.goto(325,275)

# 거리를 계산하는 함수
def cal_distance(x1, y1, x2, y2):
    # 두 점 사이의 거리를 계산
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance
    
print(f"시작점과 도착점까지의 거리: {cal_distance(-300,-270,325,275)}")


#거북이의 위치 값 지정
x1 = t.xcor()
y1 = t.ycor()

#거북이와 장애물까지의 거리 계산
print(f"시작점과 장애물까지의 거리:{cal_distance(x1,y1, 0, 0)}")