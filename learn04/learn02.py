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

cursor.execute("insert into student value (10002,'李四',22,'男')")

# conn.commit()

conn.close()
