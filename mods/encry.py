import hashlib


def encrypt():
    s = input('请输入要加密的字符串：')
    method = input('请输入加密方法：')
    key = 0
    if method == 'caesar':
        key = int(input('请输入密钥：'))
    if method == 'md5':
        if key == 0:
            hl = hashlib.md5()
            hl.update(s.encode(encoding='UTF-8'))
            print('md5加密后为:', hl.hexdigest())
        else:
            print('md5加密不需要密钥')
    elif method == 'caesar':
        if key != 0:
            s_encrypt = ''
            for word in s:
                if word == ' ':
                    word_encrypt = ' '
                else:
                    word_encrypt = chr((ord(word) - ord('a') + key) % 26 + ord('a'))
                s_encrypt += word_encrypt
            print('凯撒加密后的字符串为:', s_encrypt)
        else:
            print('请填写密钥')
