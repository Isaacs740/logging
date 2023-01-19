import logging
import mysql.connector

logging.basicConfig(filename="PgmLog.txt", level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

logging.debug('Start of program')

try:
    mydb = mysql.connector.connect(
        host="35.245.214.49",
        user="instructor",
        passwd="instructor",
        database="MovieCo"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM MOVIE "
    mycursor.execute(sql)
    for x in mycursor:
        print(x[0], ' ', x[1], ' ', x[2], ' ', x[3], ' ', x[4], ' ', x[5], ' ', x[6])
    logging.debug('Database connection successful')

except mysql.connector.Error as e:
    logging.debug('Database connection unsuccessful')
    logging.debug('Error Code: ' + str(e.errno) + ' Error State: ' + str(e.sqlstate) + 'Error Message: ' + str(e.msg))
    print('Database connector error')
    print('Error Code: ' + str(e.errno) + ' Error State: ' + str(e.sqlstate) + 'Error Message: ' + str(e.msg))

logging.debug('End of program')
