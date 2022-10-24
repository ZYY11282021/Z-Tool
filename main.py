# -*- coding: UTF-8 -*-

import mods.randomNumber

print('\033[32m欢迎使用Z Tool 0.0.1-alpha!\n如果需要帮助，请输入 help')


def opt(command):
    if command == 'help':
        print('命令列表\nquit 退出：退出Z Tool\n1 随机数：生成给定范围内的随机数\n')
    elif command == 'quit':
        return 'q'
    elif command == '1':
        begin = int(input('请输入起始值：'))
        end = int(input('请输入结束值：'))
        print(mods.randomNumber.generate(begin, end))
    else:
        print('输入的命令无效，请重新输入')


if __name__ == '__main__':
    while True:
        com = input('请输入：')
        if opt(com) == 'q':
            break
