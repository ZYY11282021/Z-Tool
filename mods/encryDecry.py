import hashlib


def encryDecrypt(s, r, method, key=0):
    if r == 'encry':
        if method == 'md5':
            hl = hashlib.md5()
            hl.update(s.encode(encoding='UTF-8'))
            print('md5加密后为:', hl.hexdigest())
        elif method == 'caesar':
            s_encrypt = ''
            for word in s:
                if word == ' ':
                    word_encrypt = ' '
                else:
                    word_encrypt = chr((ord(word) - ord('a') + int(key)) % 26 + ord('a'))
                s_encrypt += word_encrypt
            print('凯撒加密后的字符串为:', s_encrypt)
    elif r == 'decry':
        if method == 'caesar':
            s_encrypt = ''
            for word in s:
                if word == ' ':
                    word_encrypt = ' '
                else:
                    word_encrypt = chr((ord(word) - ord('a') - int(key)) % 26 + ord('a'))
                s_encrypt += word_encrypt
            print('凯撒加密算法解密后为:', s_encrypt)
    else:
        print('参数错误：错误的参数')
