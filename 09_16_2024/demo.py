import students


x = [5]
def f():
    x = [5,10]
f()
print(x)

x = students.readClassData()
print(x)