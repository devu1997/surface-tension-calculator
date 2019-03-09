import psycopg2
import sys

def main():
    try:
        conn = psycopg2.connect("dbname='housekeeping' user='udaan' host=udaan_db password='udaan123'")
        conn.close()
    except psycopg2.OperationalError as ex:
        print("Connection failed: {0}".format(ex))
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()
