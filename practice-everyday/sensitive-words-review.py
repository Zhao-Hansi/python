"""
5. 敏感词审查
一向痛恨网络审查的你成了某网站的审查员，要求审查网络上违反上头规定的名词。

功能描述： 要审查的帖子在仓库根目录的text.txt文件里，要求将所有的和谐，自由，民主，六四替换为*号。
"""

with open("text.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("和谐", "*")
content = content.replace("自由", "*")
content = content.replace("民主", "*")
content = content.replace("六四", "*")

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(content)