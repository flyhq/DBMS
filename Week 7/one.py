import psycopg2
import sys
import os

def function(db, pw, u, h, p):
    try:
        with open('date.txt') as f:
            date = f.read()
        conn = psycopg2.connect(
            database=db, password=pw, user=u, host=h, port=p)
        cursor = conn.cursor()
        query = "select name from referees where referee_id = (select referee from match_referees natural inner join matches where matches.match_date = '{}')".format(
            date)
        cursor.execute(query)
        name = cursor.fetchone()
        list_name = name[0].split()
        if len(list_name) == 2:
            print(f'{list_name[1]} {list_name[0][0]}.')
        elif len(list_name) == 3:
            print(f'{list_name[2]} {list_name[0][0]}. {list_name[1][0]}.')
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from relation", error)

    finally:
        
        conn.close()


if __name__ == '__main__':
    database = sys.argv[1]
    user = os.environ.get('PGUSER')
    password = os.environ.get('PGPASSWORD')
    host = os.environ.get('PGHOST')
    port = os.environ.get('PGPORT')

    function(db=database, pw=password, u=user, h=host, p=port)
