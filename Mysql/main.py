import sqlalchemy as sql
engine = sql.create_engine('mysql+pymysql://root:Incognito123@192.168.10.178:3306/SQLALCHEMY')
con = engine.connect()
con.close()