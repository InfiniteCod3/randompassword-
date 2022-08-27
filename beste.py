import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "(/?:_-*+,.ˇ%"
string = lowercase + uppercase + numbers + symbols
length = 50
password = "".join(random.sample(string,length))

print("your new password master owo  " + password)
