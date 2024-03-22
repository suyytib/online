# 数据库配置
HOSTNAME="localhost"
PORT=3306
USERNAME="root"
PASSWORD="123456"
DATABASE="temp"
CHARSET="utf8mb4"
# flask只读取下面的配置连接数据库,上面仅是完善下面配置用的
SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset={CHARSET}"