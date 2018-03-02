import requests
import threading
import pymysql.cursors

def store_db(data):
    # Connect to the database
    connection = pymysql.connect(host='server_db_1',
                                 user='root',
                                 password='dbpassword',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO users (firstname, lastname, avatar) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['first_name'], data['last_name'], data['avatar']))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(len(result))
            for result_item in result:
                print('{} {} {}\n'.format(result_item['firstname'], result_item['lastname'], result_item['avatar']))
    finally:
        connection.close()


def set_interval(func, sec, count):
    func()
    def func_wrapper():
        set_interval(func, sec, count)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    count -= 1
    print(count)
    if count == 0:
        t.cancel()
    return t

def rest_call():
    resp = requests.get('https://reqres.in/api/users')
    responce = resp.json()
    responce = responce['data']
    for data in responce:
        store_db(data)


set_interval(rest_call, 5, 5)
