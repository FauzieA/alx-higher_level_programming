# enter age
age = eval(input("please enter age: "))

# too young for school

if (age < 5):
    print("too young for school")

# if age is 5 go to kindergarten
elif (age == 5):
    print("go to kindergarten")
# ages 6 through 17 go to grades 1 through 12
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("go to grade {}".format(grade))
# if age is greater than 17, go to college
elif (age > 17) and (age < 24):
    print("go to college")
    # everyone else
elif (age < 30) and (age > 24):
    print("get a job")
else:
    print("you're old")

# 10 or less lines
