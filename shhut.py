def shutdown(inp):
    if(inp=="yes"):
        print("shutting down the system...")
    elif(inp=="no"):
        print("abort shut down")
    else:
        print("sorry")
a = input("enter yes/no:")
shutdown(a)