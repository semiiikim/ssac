
class AccrankingRepository:

    def __init__(self):
        self.connection_info = {'host':'localhost', 'user': 'root',  'db':'car_accident','password':'Pa$$w0rd', 'charset':'utf8'}

    def select_accrankig_count(self, key1, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, local, acc_name, acc_count from car_accident where acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and local !='서울특별시'and  year like %s and acc_name like %s order by acc_count DESC limit 5"
        cursor.execute(sql, ("%" + key1 +"%", "%" + key2 +"%", ))

        rows = cursor.fetchall()
        keys = ['year', 'local', 'acc_name', 'acc_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result


    def select_accrankig_death(self, key1, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, local, acc_name, death_count from car_accident where acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and local !='서울특별시'and  year like %s and acc_name like %s order by death_count DESC limit 5"
        cursor.execute(sql, ("%" + key1 +"%", "%" + key2 +"%", ))

        rows = cursor.fetchall()
        keys = ['year', 'local', 'acc_name', 'death_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result


    def select_accrankig_injury(self, key1, key2):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select year, local, acc_name, injury_count from car_accident where acc_name != '전체사고' and acc_name != '야간사고' and acc_name != '보행자사고' and acc_name != '어린이보행사고' and acc_name != '스쿨존내어린이사고' and acc_name != '고령운전자사고' and acc_name != '고령보행자사고' and local !='서울특별시'and  year like %s and acc_name like %s order by injury_count DESC limit 5"
        cursor.execute(sql, ("%" + key1 +"%", "%" + key2 +"%", ))

        rows = cursor.fetchall()
        keys = ['year', 'local', 'acc_name', 'injury_count']
        result = []
        for row in rows:
            row_dict = {key:value for key, value in zip(keys,row)}
            result.append(row_dict)

        return result
