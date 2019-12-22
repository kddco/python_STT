def write(userPassword):
    try:
        f = open('USER_identity.txt','w')
        f.write(userPassword)
        f.write('\n')
    except Exception :
        print(Exception)