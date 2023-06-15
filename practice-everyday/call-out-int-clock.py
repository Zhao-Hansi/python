"""
4. 整点报时
老式挂钟会在整点的报时，响铃的次数和时间相等。我们设计一个在电脑上运行的报时器。

功能描述： 运行后，在每一个整点长响一声，半个整点短响两声。实现睡眠模式，晚上十二点到早上六点不响铃。
"""
import time

while True:
    current_time = time.localtime()
    hour, minute = current_time.tm_hour, current_time.tm_min

    if 6 <= hour < 12:
        if minute == 0:
            print("长响一声")
            time.sleep(60)
        elif minute == 30:
            print("短响两声")
            time.sleep(60)
    elif 12 <= hour < 18:
        if minute == 0:
            print("长响一声")
            time.sleep(60)
        elif minute == 30:
            print("短响两声")
            time.sleep(60)
    elif 18 <= hour < 24:
        if minute == 0:
            print("长响一声")
            time.sleep(60)

        elif minute == 30:
            print("短响两声")
            time.sleep(60)
    else:
        time.sleep(60 * 60 * 6)  # 晚上12点到早上6点不响铃，等待6个小时