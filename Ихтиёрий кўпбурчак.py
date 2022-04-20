import turtle
x=turtle.Turtle()
x.width(5)
x.hideturtle()
x.speed(2)
n=int(input('Tomonlar sonini kiriting='))
m=int(input('Tomon uzunligini kiriting='))
for z in range(n+1):
    x.color("red")
    x.forward(m)
    x.right(360/n)
# Telegram kanalimiz: @Videodarslar_uzb
# Murojaat uchun: @Bepul_Videodarslar
# Telegramning qidiruv bo'limidan qidiring.
