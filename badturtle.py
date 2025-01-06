import turtle




def write_name(name):
    
    t = turtle.Screen()
    t.bgcolor('red')

    my_turtle = turtle.Turtle()
    my_turtle.speed(0.1)
    my_turtle.penup()
    my_turtle.goto(-150, 0)
    my_turtle.pendown()
    my_turtle.write(name, font=("Arial", 50, "bold"))


    t.mainloop()

name = input("enter your name: ")
write_name(name)