from time import sleep

import redis

# 连接Redis服务器
r = redis.Redis(host='localhost', port=6379, db=0)
redis_client = redis.Redis(connection_pool=r)
# 设置键值对
r.set('name', 'Alice')
r.expire('name', 5)
sleep(3)
# 获取键对应的值
name = r.get('name')
print(name.decode('utf-8'))  # 需要将bytes类型的返回值解码为字符串