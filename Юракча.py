import turtle

romeo = turtle.Turtle()
juliet = turtle.Turtle()
romeo.hideturtle()
juliet.hideturtle()
juliet.color("blue")
juliet.width(5)

romeo.color("red")
romeo.width(5)

romeo_last_name = "montague"

romeo.left(40)
romeo.forward(100)
for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

if romeo_last_name == "montague":
    juliet.left(140)
    juliet.forward(100)
    for side in range(185):
        juliet.forward(1)
        juliet.right(1)
    juliet.hideturtle()
# Telegram kanalimiz: @Videodarslar_uzb
# Murojaatlar uchun: @Bepul_Videodarslar
# Telegramning qidiruv bo'limidan qidiring.
