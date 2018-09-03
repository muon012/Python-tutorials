# print("------------------------- 1 -------------------------")
# # The "import turtle" lets you use an animation model of a line that you can tell it to go in certain directions.
# # We added "import time" because this will pause the animation for a certain amount of seconds after it is over.
# # After it is over it will automatically close the program.
# import turtle
# import time
#
# # The next line of code lets you hide warning signs due to incorrect code, but you know is right for sure:
# # noinspection PyUnresolvedReferences
# turtle.forward(150)
# turtle.left(250)
# turtle.forward(150)
# turtle.right(200)
#
# time.sleep(3)
#
# print("------------------------- 2 -------------------------")
# # Here we use the ".done()" function instead of using the "time" module
# # to stop the program after it is over. But you must manually close it afterwards.
# import turtle
#
# turtle.forward(150)
# turtle.left(250)
# turtle.forward(150)
# turtle.right(200)
#
# turtle.done()
#
# print("------------------------- 3 -------------------------")
# # We can also write the same code as before with only one "import" statement.
#
# from turtle import forward, right, left, done
#
# forward(150)
# left(250)
# forward(150)
# right(200)
#
# done()
#
print("------------------------- 4 -------------------------")
# One last method that we can use when using "import."
# You could use "import *" but this is frowned upon since you could declare a variable that has the same name as one
# of the elements imported from that module and therefore cause errors.

from turtle import forward, right, done
import turtle

forward(150)
right(250)
turtle.circle(75)
forward(150)

done()