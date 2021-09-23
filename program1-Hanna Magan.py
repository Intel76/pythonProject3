# Team member: Hanna Magan
# Course: CS151, Dr.Rajeev
# Date: 22 September 2021
# Programing Assignment 1
# import math
# Program Inputs: ask user for dimensions (length,width and height)
room_length = input("Enter room_length")
room_width = input("Enter room_width")
room_height = input("Enter room_height")
# Program Outputs: The total area(square feet) to be painted with the amount of primer and paint (in gallons) needed
area = float(2*(room_height * room_length) + 2*(room_width * room_height) + (room_width * room_length))
print area
primer = math.ceil(area/200)
print primer
paint = math.ceil(area/350)
print paint