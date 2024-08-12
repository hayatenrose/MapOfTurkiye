import turtle
import pandas
import random
turkey = pandas.read_csv("cities.csv")
screen = turtle.Screen()
screen.title("Map of Turkiye")
image="turkiye.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1500, height=800)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
is_over = False
score = 0
turkey = pandas.read_csv("cities.csv")
written = []
city = turkey["city"].to_list()
xcor = turkey["x"].to_list()
ycor = turkey["y"].to_list()
# def get_mouuse_click_coor(x, y):
#     print(f"{x}, {y}")
# turtle.onscreenclick(get_mouuse_click_coor)

# i=70
# while i<81:
#     print(f"{turkey.city[i]}, {turkey.x[i]+1}, {turkey.y[i]}")
#     i+=1

while not is_over:
    ans = screen.textinput(title=f"Cities of Turkiye Score: {score}/81", prompt="Enter a city in Turkiye")
    if ans is None:
        continue
    else:
        answer = ans.lower()
        for i in range(81):
            if answer == turkey.city[i].lower():

                if turkey.city[i] not in written:
                    written.append(turkey.city[i])
                    writer.goto(turkey.x[i], turkey.y[i])
                    writer.write(turkey.city[i], align="center", font=("Arial", 9, "bold"))
                    score += 1
                    city.remove(turkey.city[i])
                    xcor.remove(turkey.x[i])
                    ycor.remove(turkey.y[i])
        if answer == "over" or score ==81:
            is_over = True
        elif answer == "help":
            for a in range(81-score):
                writer.goto(xcor[a], ycor[a])
                writer.write(city[a], align="center", font=("Arial", 9, "bold"))
            is_over = True


turtle.mainloop()
#     if answer.capitalize() in city:
#         writer.goto(turkey.x[turkey.city == answer], turkey.x[turkey.city == answer])
#         writer.write(answer, align="center", font=("Arial", 9, "bold"))
#         score += 1
#         city.remove(answer)
#     if answer == "over" or score ==81:
#         is_over = True
#     elif answer == "help":
#         for a in city:
#             writer.goto(turkey.x[turkey.city == answer], turkey.x[turkey.city == answer])
#             writer.write(answer, align="center", font=("Arial", 9, "bold"))
#         is_over = True
#
# for i in range(81):
#     writer.goto(turkey.x[i], turkey.y[i])
#     writer.write(turkey.city[i], align="center", font=("Arial", 9, "bold"))


