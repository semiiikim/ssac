
class AccyearRepository:

    # database 연결
    def __init__(self):
        self.connection_info = {'host':'localhost', 'user': 'root',  'db':'car_accident','password':'Pa$$w0rd', 'charset':'utf8'}
    
    # def select_car_accident_by_name(self, name_key):
    def select_car_accident_by_name(self):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, acc_name, local, total_count, total_death_count, total_injury_count from car_accident where acc_name='전체사고' and local='서울특별시' and year between 2015 and 2019 order by year ASC"
        # cursor.execute(sql,("%" + name_key + "%",))
        cursor.execute(sql)

        rows = cursor.fetchall()
        keys = ['year', 'acc_name', 'local','total_count', 'total_death_count', 'total_injury_count']
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)


        conn.close()

        return result


    def select_car_accident_by_year(self, year_key):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql="select year, acc_name, local, total_count, total_death_count, total_injury_count from car_accident where acc_name='전체사고' and year like %s"
        cursor.execute(sql, ("%" + year_key +"%",))

        rows = cursor.fetchall()
        keys=['year', 'acc_name', 'local','total_count', 'total_death_count', 'total_injury_count']
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row)}
            result.append(row_dict)

        return result


    def select_car_accident_by_local(self, local):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, acc_name, local, acc_count, death_count, injury_count from car_accident where acc_name='전체사고' and local = %s"
        cursor.execute(sql, (local,))

        row = cursor.fetchone()
        keys = ["year", "acc_name", "local","acc_count", "death_count", "injury_count"]

        result = { key:value for key, value in zip(keys, row)}

        conn.close()

        return result

    
