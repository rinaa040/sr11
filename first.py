import sqlite3


class AccountingPassengers:
    def __init__(self, filename):
        self.filename = filename

    def trip(self, date, ship_name):
        passengers = []
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        ship_id = cur.execute("""SELECT id FROM ships
                                                WHERE name = ?""", (ship_name,)).fetchone()

        result = cur.execute("""SELECT * FROM accounting
                                                WHERE date = ? and ship_id = ?""", (date, ship_id[0])).fetchall()
        for elem in result:
            class_cost = cur.execute("""SELECT cost FROM tickets
                                                            WHERE id = ?""", (elem[-2],)).fetchone()
            price = class_cost[0] * elem[-1]
            passengers.append((elem[2], elem[3], price))
        con.close()
        passengers.sort(key=lambda x: (x[0], x[1]))
        p = [f"{x[0]} {x[1]}, {x[2]}" for x in passengers]
        return p
        # passengers = cur.execute("""SELECT * FROM accounting
        #                                     WHERE date = ? and ship_id = ?""", (date, ship_id[0])).fetchall()
        # поиск ссылки на фото элемента в бд
        # elem_pic = cur.execute("""SELECT pic_link FROM elem_pictures
        #                                         WHERE name = ?""", (x,)).fetchone()

    def date_list(self, date):
        d = {}
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        # ship_id = cur.execute("""SELECT id FROM ships
        #                                                 WHERE name = ?""", (ship_name,)).fetchone()

        result = cur.execute("""SELECT * FROM accounting
                                                        WHERE date = ?""",
                             (date,)).fetchall()
        for elem in result:
            ship_name = cur.execute("""SELECT name FROM ships
                                                                   WHERE id = ?""", (elem[4],)).fetchone()
            


ap = AccountingPassengers('4steamers.db')
print(*ap.trip("27/08", "Magnolia"), sep="\n")
print(ap.date_list("28/08"))
