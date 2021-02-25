import datetime
result=[]
print(dir(datetime))
for i in dir(datetime):
    print(type(getattr(datetime, i)).__name__)
    if type(getattr(datetime, i)).__name__ == "function":
        result.append(getattr(datetime, i))
print(result)