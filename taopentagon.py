import turtle

tao = turtle.Pen() #ใช้ปากกาได้เเล้ว
tao.shape('turtle') #แปลงร่างเป็นเต๋า
def f_1():
    '''เต่าวาดห้าเหลี่ยม'''
    for i in range(9):
        tao.fd(75)
        tao.left(45)
def f_2():
    for i in range(4):
        f_1()
        tao.left(45)
        tao.fd(1)
        i = i + 1
    Go(38,39)

def Go(x,y):
    '''ส่งเต๋าไปซักที่'''
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
f_2()
