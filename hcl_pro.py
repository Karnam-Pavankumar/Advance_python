
from hcl_database_connection import mysqlDatabaseConnection

class Booking(mysqlDatabaseConnection):
    pass
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_avl_tkt")

            for r in self.cursor.started.results():
                seats = r.fetchall()
            return seats


        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass

b1=Booking()
b1.connect("localhost","root","9959795595","train_ticket_booking")
sts=b1.available_seats()
seat_avl={}
seat_avl['Train_name']=sts[0]
seat_avl['seats']=sts[1]
print(seat_avl)