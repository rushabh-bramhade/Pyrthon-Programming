num = 10
def multi():
    result = num * 2
    print(result)
multi()



ending="Thank you for coming"
def days(name):
    print(f"Hello {name} have a fun in these days?")
    repaly = input(" ")
    if(repaly =="yes"):
        print("have a good day")
    elif(repaly == "no"):
        print("i wish your days well gone")
    else:
        print(ending)
    

days("rushabh")