# encoding: utf-8

import MySQLdb

def main():
    username = raw_input('input username:')
    password = raw_input('input password:')

    db = MySQLdb.connect("localhost", username, password, 'keystone')

    cursor = db.cursor()
    cursor.execute('select url from endpoint;')
    results = cursor.fetchall()

    for row in results:
        url = row[0]
        urlr = url.replace('192.168.64.32', '10.0.64.23')
        updatesql = 'update endpoint set url = "%s" where url = "%s"' % (urlr, url)
        cursor.execute(updatesql)
    
    db.commit()

    db.close()


if __name__ == '__main__':
    main()