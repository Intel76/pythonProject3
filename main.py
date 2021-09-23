# Team member: Hanna Magan
# Course: CS151, Dr.Rajeev
# Date: 22 September 2021
# Programing Assignment 1
#
import math
# Program Inputs: [What information do you request from the user?]
# ask user for dimensions (length,width and height)
room_length = input("Enter room_length")
room_width = input("Enter room_width")
room_height = input("Enter room_height")
# Program Outputs: [What information do you display for the user?]
area = float(2*(room_height * room_length) + 2*(room_width * room_height) + (room_width * room_length))
print area
primer = math.ceil(area/200)
print primer
paint = math.ceil(area/350)
print paint