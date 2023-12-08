from pymysql import Connection
from file import FileReader, TextFileReader, JsonFileReader
from data import Record

text_file_reader = TextFileReader("../learn03/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("../learn03/2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_data()  # type: list[Record]
feb_data = json_file_reader.read_data()  # type: list[Record]

# 将2个月份的数据合并为1个list来存储
all_data = jan_data + feb_data  # type: list[Record]

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

# 创建表
# cursor.execute("create table orders (order_date date,order_id varchar(255),money int, province varchar(255))")

# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) values ('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"

    # 执行SQL语句
    cursor.execute(sql)

conn.close()
