from pymysql import Connection

# 创建Connection连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='531619',
    autocommit=True  # 自动提交事务
)

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db('pydb')

# 创建一个空字典dic
dic = {}

f = open("date.txt", 'a', encoding='utf-8')

cursor.execute('select * from orders')

# 获取查询结果，每次打印一条记录，直到为空

for i in range(cursor.rowcount):
    result = cursor.fetchone()

    order_date = result[0].strftime('%Y-%m-%d')
    order_id = result[1]
    money = result[2]
    province = result[3]

    # 将数据存入字典dic中
    dic['date'] = order_date
    dic['order_id'] = order_id
    dic['money'] = money
    dic['province'] = province

    # 将字典dic中的数据写入文件
    f.write(str(dic) + '\n')

# 关闭
cursor.close()
