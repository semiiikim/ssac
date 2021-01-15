
class AcctypeRepository:

    def __init__(self):
        self.connection_info = {'host':'localhost', 'user': 'root',  'db':'car_accident','password':'Pa$$w0rd', 'charset':'utf8'}


    # 5년간 추이
    def select_acctype_trend(self, key1, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "SELECT year, local, acc_name, acc_count, death_count, injury_count FROM car_accident WHERE acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and year between 2015 and 2019 and acc_name like %s and local like %s order by year ASC"
        cursor.execute(sql, ("%" + key1 +"%", "%" + key2 +"%",))

        rows = cursor.fetchall()
        keys = ['year', 'local', 'acc_name', 'acc_count', 'death_count', 'injury_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result
    


    # 사고 발생 횟수
    def select_acctype_acccount(self, year_key, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, acc_name, local, acc_count from car_accident where acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and  year like %s and local like %s"
        cursor.execute(sql, ("%" + year_key +"%", "%" + key2 +"%",))

        rows = cursor.fetchall()
        keys = ['year', 'acc_name', 'local', 'acc_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result

    # 사망자 수 
    def select_acctype_deathcount(self, year_key, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, acc_name, local, death_count from car_accident where acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and  year like %s and local like %s"
        cursor.execute(sql, ("%" + year_key +"%", "%" + key2 +"%",))

        rows = cursor.fetchall()
        keys = ['year', 'acc_name', 'local', 'death_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result

    # 부상자 수 
    def select_acctype_injurycount(self, year_key, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, acc_name, local, injury_count from car_accident where acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and  year like %s and local like %s"
        cursor.execute(sql, ("%" + year_key +"%", "%" + key2 +"%",))

        rows = cursor.fetchall()
        keys = ['year', 'acc_name', 'local', 'injury_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result
