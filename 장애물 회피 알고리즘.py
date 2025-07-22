import turtle

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