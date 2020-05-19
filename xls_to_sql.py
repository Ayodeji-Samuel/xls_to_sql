import pandas
import sys
import pprint
import sqlite3
def main():
    
    try:
        xls_in = str(sys.argv[1])
        db_name = str(sys.argv[2])
    except Exception as e:
        print(e + "\n")
        sys.exit("Usage: xls_sqlite.py file.xls file.db3")
    xls_to_sql(xls_in, db_name)

def xls_to_sql(xls_in,db_name):
    
    try:
        f = pandas.read_excel(xls_in)
    
    	    # print what we can do with f as an object, and to_sql is an option
        #pprint.pprint(dir(f))
    
    	    # xls file as a table name
        table_name = xls_in.split('.')[0]
            #sqlite3 connection
        conn = sqlite3.connect(db_name)
    
        f.to_sql(table_name,conn)
        print("\n[+]    xls to sql done    [+]\n")
    except Exception as e:
        print("\n[-]    {}    [-]\n".format(e))
if __name__ == "__main__":
    main()