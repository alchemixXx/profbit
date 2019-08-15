import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import Config


def init_db():
    try:
        conn = psycopg2.connect(dbname=Config.DEFUALT_DB_NAME,
                                user=Config.PG_USER, host=Config.PG_HOST,
                                password=Config.PG_PASSWORD)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("DROP DATABASE IF EXISTS %s  ;" % (Config.DB_NAME,))
        cur.execute("CREATE DATABASE %s  ;" % (Config.DB_NAME,))
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

