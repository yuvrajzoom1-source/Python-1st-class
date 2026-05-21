val=input("Enter the expression:")
try:
    print(eval(val,{"__builtins__":{}}))
except Exception as e:
    print(e)