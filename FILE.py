# coding=utf-8
def write(userPassword):
    try:
        f = open('USER_identity.txt','w',encoding = "UTF-8")
        f.write(userPassword)
        f.write('\n')
        f.close()
    except Exception as e:
        print(e)