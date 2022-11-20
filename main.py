# -*- coding: UTF-8 -*-

import mods.encryDecry
import mods.randomNumber
import mods.stamptotime
import mods.participle

print('\033[32m欢迎使用Z Tool 0.0.3-alpha!\033[0m\n如果需要帮助，请输入 help')


def opt(command):
    try:
        if command[0] == 'help':
            print('命令列表\nquit：退出Z Tool\nrandom：生成给定范围内的随机数\n\t参数 起始值：随机数的起始值\n\t参数 结束值：随机数的结束值\nende：加密或解密字符串\n\t参数 '
                  '字符串：要加密的字符串\n\t参数 作用：选择加密或解密\n\t参数 '
                  '方法：加密/解密的方法\n\t参数 密钥：凯撒加密/解密专用，偏移值\nstamp2time：将时间戳转换为正常时间\n\t参数 时间戳\nptcpe：分词\n\t参数 句子：要分词的句子\n')
        elif command[0] == 'quit':
            return 'q'
        elif command[0] == 'random':
            begin = command[1]
            end = command[2]
            print('生成的随机数是:', mods.randomNumber.generate(begin, end))
        elif command[0] == 'ende':
            s = command[1]
            role = command[2]
            m = command[3]
            if m == 'caesar':
                k = command[4]
            if m == 'caesar':
                mods.encryDecry.encryDecrypt(s, role, m, k)
            else:
                mods.encryDecry.encryDecrypt(s, role, m)
        elif command[0] == "ptcpe":
            st = command[1]
            mods.participle.partic(st)
        elif command[0] == 'stamp2time':
            sta = command[1]
            mods.stamptotime.to_time(sta)
        else:
            print('命令错误：无法找到"%s"这个命令' % com[0])
    except IndexError:
        print('参数错误：必要参数未填')


if __name__ == '__main__':
    while True:
        com = input('>>> ').split()
        if opt(com) == 'q':
            break
