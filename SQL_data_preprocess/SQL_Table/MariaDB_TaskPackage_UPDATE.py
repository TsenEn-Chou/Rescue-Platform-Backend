import mysql.connector
import datetime
from mysql.connector import Error
try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='smartdb', # 資料庫名稱
        user='Tsen',        # 帳號
        password='CTsen')  # 密碼

    if connection.is_connected():

        # 顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本：", db_Info)

        # 顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)

    cursor = connection.cursor()


    # sql = "UPDATE task_package SET task_date =%s WHERE id = %s;"
    # date = datetime.date.today()
    # datestr = date.strftime("%Y-%m-%d")
    # for i in range(1,4):
    #     new_data = (datestr,i)
    #     cursor.execute(sql, new_data)
    
    # sql = "UPDATE task_package SET taskinfo =%s WHERE id = %s;"
    # new_data = ("需要 500 加侖的水",1) 
    # cursor.execute(sql, new_data)
    # new_data = ("需要一輛能載 20 人的載具",2)
    # cursor.execute(sql, new_data)
    # new_data = ("需要 100 人份的棉被",3)
    # cursor.execute(sql, new_data)

    sql = "UPDATE task_package SET lightpoles_phase =%s WHERE id = %s;"
    for i in range(1,4):
        new_data = ("1,2,1,6,5",i)
        cursor.execute(sql, new_data)
    connection.commit() 
    #Closing the connection
    connection.close()


except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("資料庫連線已關閉")