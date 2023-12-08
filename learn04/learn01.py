from pymysql import Connection

# 创建Connection连接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='531619'
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db('test')

# 创建表
# cursor.execute("create table test_pymysql(id int)")

# 查询表
cursor.execute("select * from product")

results = cursor.fetchall()

for result in results:
    print(result)

# 关闭数据库连接
conn.close()
