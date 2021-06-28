import os
import threading

# 记忆存储111
# 密码加密
# 解冻账号
fp = open("1.txt",'a')
def add(): # 注册用户
    os.system('cls')
    print("===========注册操作==========")
    aa = open('1.txt', encoding='utf-8')
    aaa = []
    for i in aa.readlines():
        aaa.append(i.split('&')[0])
    a = input('账号:')
    if not a in aaa:
        if len(a) == 8:
            try:
                a1 = int(input('密码:'))
                a1 = str(a1 * 4 + 521)
                if len(a1) == 6:
                    a2 = input('预存款:')
                    a3 = input('邮箱:')
                    print('...>>>注册成功<<<...')
                    with open('1.txt', 'a', encoding='utf-8') as f:
                        f.write(a + '&' + a1 + '&' + a2 + '&' + a3 + '&' + '0' + '\n')

                else:
                    print('密码长度为6位')

            except ValueError:
                print('输入的类型错误')
            # 密码算法

        else:
            print('账号长度为8位')
    else:
        print('账号已存在')


def login(): # 返回当前用户信息 及其登陆状态
    os.system('cls')
    print("===========登陆操作==========")
    aa = open('1.txt', encoding='utf-8')
    aaa = {}
    for i in aa.readlines():
        aaa[i.split('&')[0]] = [i.split('&')[0],i.split('&')[1],i.split('&')[2],i.split('&')[3],i.split('&')[4]]
    #print(aaa)
    a = input('输入账号:')
    try:
        if aaa[a][4] != '1\n':

            if a in aaa:
                for i in range(3):
                    a1 = input('输入密码:')
                    try:
                        a1 = str(int(a1) * 4 + 521)
                    except:
                        a1 = 0
                    if a1 == aaa[a][1]:
                        print('账号登陆成功')
                        return aaa[a][0],aaa

                else:
                    print('...账号冻结...')
                    aaa[a][4] = '1\n'

                    with open('1.txt', 'w', encoding='utf-8') as f:
                        f.write('')
                    for i in aaa:
                        with open('1.txt','a',encoding='utf-8') as f:
                            f.write(aaa[i][0] + '&' + aaa[i][1] + '&' + aaa[i][2] + '&' + aaa[i][3] + '&' + aaa[i][4])

                    return -1,-1
        else:
            print('当前账号已经冻结')
            return -1,-1
    except:
        print('当前账号不存在')
        return -1,-1



def chun(a,b):
    os.system('cls')
    print("===========存款操作==========")
    if a != -1:
        c1 = float(input("请输入存款金额:"))
        b[a][2] = str(float(b[a][2]) + c1)
        print(f'存款{c1}元成功,当前余额{b[a][2]}元')

        with open(f'{a}.txt', 'a', encoding='utf-8') as f:
            f.write(f'存款{c1}\n')

        with open('1.txt', 'w', encoding='utf-8') as f:
            f.write('')
        for i in b:
            with open('1.txt', 'a', encoding='utf-8') as f:
                f.write(b[i][0] + '&' + b[i][1] + '&' + b[i][2] + '&' + b[i][3] + '&' + b[i][4])
    else:
        print('账号还未登陆')


def qu(a,b):
    os.system('cls')
    print("===========取款操作==========")
    if a != -1:
        c1 = float(input("请输入取款金额:"))
        if c1 <= float(b[a][2]):
            b[a][2] = str(float(b[a][2]) - c1)
            print(f'取款{c1}元成功,当前余额{b[a][2]}元')

            with open(f'{a}.txt', 'a', encoding='utf-8') as f:
                f.write(f'取款{c1}\n')

            with open('1.txt', 'w', encoding='utf-8') as f:
                f.write('')
            for i in b:
                with open('1.txt', 'a', encoding='utf-8') as f:
                    f.write(b[i][0] + '&' + b[i][1] + '&' + b[i][2] + '&' + b[i][3] + '&' + b[i][4])
        else:
            print('账号金额不支持')
    else:
        print('账号还未登陆')


def chaxun(a,b):
    os.system('cls')
    if a != -1:
        print("===========账号信息==========")
        print(f'当前账号昵称:{b[a][0]}\t账户余额:{b[a][2]}')
        try:
            print(open(f'{a}.txt',encoding='utf-8').read())
        except:
            pass


    else:
        print('账号还未登陆')

def jie_dong():
    os.system('cls')
    zhanghao = input('请输入账号:')
    eamil = input('请输入邮箱:')
    ls = []
    for i in open('1.txt',encoding='utf-8').readlines():
        ls_sp = i.split('&')
        if zhanghao == ls_sp[0]:
            if eamil == ls_sp[3]:
                ls_sp[4] = '0\n'
                print('解冻成功')
                ls.append(ls_sp)
            else:
                print('解冻失败')
                ls.append(i.split('&'))
        else:
            ls.append(i.split('&'))
    else:
        with open('1.txt','w',encoding='utf-8') as f:
            for b1 in ls:
                f.write(b1[0] + '&' + b1[1] + '&' + b1[2] + '&' + b1[3] + '&' + b1[4])





def fun_timer():
    timer = threading.Timer(5, fun_timer)
    z, b = -1, -1
    a1 = True
    while True:
        a = input("===========================\n"
                  "\t银行管理系统V1.0\n"  
                  "===========================\n"
                  "\t\t1.开户\n\t\t2.登陆\n\t\t3.解冻\n"
                  "===========================\n"
                  "请输入你的选项:"
                )
        if a == '1':
            timer.start()
            add()

        if a == '3':
            jie_dong()
            timer.start()
        if a == '2':
            z , b = login()
            a1 = True
            timer.start()
        if z != -1:
            while a1:
                aa = input("===========================\n"
                             "\t1.存款\t2.取款\n\t3.查询\t4.退出账号\n"
                        "===========================\n"
                            "请输入你的选项:")
                if aa == '1':
                    chun(z ,b)
                if aa == '2':
                    qu(z,b)
                if aa == '3':
                    chaxun(z,b)
                if aa == '4':
                    z, b = -1, -1
                    a1 = False
                    print("账号退出成功!")


fun_timer()