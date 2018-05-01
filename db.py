import pymysql
def getTasks():

    sql = "SELECT text FROM tasks"

    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()

    conn.close()

    L=[]
    for row in result:
        L.extend(row)

    return L

def addTask(task):
    sql="insert into tasks (text) values (%s)"

    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (task,))
    conn.close()


def getUrgency(task):
    sql="select urgent from tasks where text=%s"
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    result=cursor.fetchone()[0]# NB for not getting the extra comma, as the fetchone returns a tuple of values, so with commas
    conn.close()
    return result
def getId(task):
    sql = "select id_task from tasks where text=%s"
    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    result = cursor.fetchone()[0]
    conn.close()
    return result

def deleteTask(id):
    sql = "delete from tasks where id_task=%s"

    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='tasks', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.close()

