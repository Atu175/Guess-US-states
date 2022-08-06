import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# WHAT WAS USED TO GET THE X AND Y COORDINATES
# write something at a given coordinate
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# # when clicked it gets the coordinate
# turtle.onscreenclick(get_mouse_click_coor)
# # keeping screen open after cliscked
# turtle.mainloop()
count = 0
# Getting all the columns in a list
data = pandas.read_csv('50_states.csv')
states_list = data.state.tolist()
typed_states = []
x_list = data.x.tolist()
y_list = data.y.tolist()
t = turtle.Turtle()
t.hideturtle()
while count != 50:
    # Pop up box that as user for a name
    answer = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        # for state in typed_states:
        #     if state in states_list:
        #         states_list.remove(state)
        [states_list.remove(state) for state in typed_states if state in states_list]
        file = pandas.DataFrame(states_list)
        file.to_csv("states_to_learn.csv")
        break
    if answer in states_list and answer not in typed_states:
        count += 1
        t.penup()
        t.goto(int(x_list[states_list.index(answer)]), int(y_list[states_list.index(answer)]))
        t.write(answer)
        typed_states.append(answer)







