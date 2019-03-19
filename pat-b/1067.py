passw, times = input().split()

step = 0
while True:
    if step < int(times):
        temp = input()
        if temp == '#':
            break
        else:
            if temp == passw:
                print("Welcome in")
                break
            else:
                print("Wrong password: {}".format(temp))
                step += 1
    else:
        print("Account locked")
        break
        