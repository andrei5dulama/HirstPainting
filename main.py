import random
import turtle as t

tim = t.Turtle()

t.colormode(255)

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     rgb_colors.append(new_color)
# # print(rgb_colors)

color_list = [(203, 34, 66), (71, 116, 151), (228, 161, 193), (246, 253, 251), (252, 246, 250), (150, 184, 70),
              (151, 160, 164), (242, 235, 46), (37, 161, 80), (35, 31, 32), (137, 205, 187), (240, 99, 54),
              (75, 65, 40), (33, 162, 165), (221, 49, 65), (142, 210, 191), (145, 69, 64),
              (38, 155, 73), (137, 191, 57), (214, 144, 167), (67, 59, 37), (241, 170, 155), (207, 18, 76),
              (153, 206, 210), (59, 135, 199), (165, 195, 220), (235, 239, 12), (242, 14, 29)]

tim.penup()
tim.hideturtle()




# def row(circles_on_row, circle_radius, distance_between_circles):
#     for _ in range(circles_on_row):
#         tim.color(random.choice(color_list))
#         tim.pendown()
#         tim.begin_fill()
#         tim.circle(circle_radius)
#         tim.end_fill()
#         tim.penup()
#         tim.forward(distance_between_circles)
#
# x = -250
# y = -250
# def next():
#     tim.penup()
#     global y
#     y += 50
#     tim.goto(x, y)
#
# for _ in range(10):
#     next()
#     row(10, 10, 50)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()