from hcl_database_connection import mysqlDatabaseConnection
class HClstoredProcedure(mysqlDatabaseConnection):
    pass
connect_obj = HClstoredProcedure()
connect_obj.connect("localhost","root","root","customer_db")
print(connect_obj)