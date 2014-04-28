__author__ = 'yufeilong'

port = ""
while 1:
    port = input("Input the port: ")
    if len(port) == 0:
        print("enter error, input again ")
    else:
        break
print("your input is", port)