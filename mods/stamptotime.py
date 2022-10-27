import time


def to_time(timestamp):
    try:
        print('转换为正常时间为:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamp))))
    except OSError:
        print('参数错误：stamp2time指令时间戳参数异常')
