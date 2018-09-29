#/bin/python 3.7

import turtle

def tree(tree_size):
    if tree_size > 0:

        #turtle.pensize(tree_size/10)

        turtle.forward(tree_size)
        turtle.right(15)
        tree(tree_size - 10)

        turtle.left(30)
        tree(tree_size - 10)

        turtle.right(15)
        turtle.backward(tree_size)

        if tree_size < 15:
            turtle.color("green")
        else:
            turtle.color("brown")

def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()

    tree(50)

    turtle.exitonclick()

if __name__ == "__main__":
    main()