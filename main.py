# -*- coding: UTF-8 -*-

import mods.randomNumber
import mods.encry

print('\033[32m欢迎使用Z Tool 0.0.1-alpha!\n如果需要帮助，请输入 help')


def opt(command):
    if command[0] == 'help':
        print('命令列表\nquit 退出：退出Z Tool\n1 随机数：生成给定范围内的随机数\n2 加密：加密字符串\n')
    elif command[0] == 'quit':
        return 'q'
    elif command[0] == '1':
        begin = int(input('请输入起始值：'))
        end = int(input('请输入结束值：'))
        print('生成的随机数是:', mods.randomNumber.generate(begin, end))
    elif command[0] == '2':
        mods.encry.encrypt()
    else:
        print('输入的命令无效，请重新输入')


if __name__ == '__main__':
    while True:
        com = input('请输入：').split()
        if opt(com) == 'q':
            break
