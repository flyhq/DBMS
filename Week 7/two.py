import psycopg2
import sys
import os
from math import cos, pi


def function(db, pw, u, h, p):
    try:
        with open('parameter.txt') as f:
            letter = f.read()
        conn = psycopg2.connect(
            database=db, password=pw, user=u, host=h, port=p)
        cursor = conn.cursor()
        query = "select sum(host_team_score) from matches inner join teams on matches.host_team_id = teams.team_id where host_team_score > guest_team_score and teams.name like '{}%'".format(
            letter)
        cursor.execute(query)
        score = cursor.fetchone()
        cursor.close()
        deg = round(cos((int(score[0])*10) * (pi/180)), 2)
        print(deg)

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
