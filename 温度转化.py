# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

F = float(input("please input the F temprature:"))
C = F - 32 / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (F, C))


