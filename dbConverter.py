import sqlite3
import csv
from fileIO import createCSV2
def sqliter(csvFile, outputDBName='outputDB'):

    con = sqlite3.connect(str(outputDBName+'.db'))
    cur = con.cursor()

    a_file = open(csvFile)
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO data VALUES (?, ?)", rows)

    cur.execute("SELECT * FROM data")
    print(cur.fetchall())
    con.commit()
    con.close()


def _get_col_datatypes(fin):
    dr = csv.DictReader(fin) # comma is default delimiter
    fieldTypes = {}
    for entry in dr:
        feildslLeft = [f for f in dr.fieldnames if f not in fieldTypes.keys()]
        if not feildslLeft: break # We're done
        for field in feildslLeft:
            data = entry[field]

            # Need data to decide
            if len(data) == 0:
                continue

            if data.isdigit():
                fieldTypes[field] = "INTEGER"
            else:
                fieldTypes[field] = "TEXT"
        # TODO: Currently there's no support for DATE in sqllite

    if len(feildslLeft) > 0:
        raise Exception("Failed to find all the columns data types - Maybe some are empty?")

    return fieldTypes


def escapingGenerator(f):
    for line in f:
        yield line.encode("ascii", "xmlcharrefreplace").decode("ascii")


def csvToDb(csvFile, outputDBName='outputDB'):

    with open(csvFile,mode='r', encoding="ISO-8859-1") as fin:
        dt = _get_col_datatypes(fin)

        fin.seek(0)

        reader = csv.DictReader(fin)

        # Keep the order of the columns name just as in the CSV
        fields = reader.fieldnames
        cols = []

        # Set field and type
        for f in fields:
            # print(f,end='-->')
            sf = str(f).replace('.','_')
            # print(f)
            cols.append("%s %s" % (sf, dt[f]))

        # Generate create table statement:
        stmt = "CREATE TABLE ads (%s)" % ",".join(cols)
        # print(stmt)
        con = sqlite3.connect(str(outputDBName+'.db'))
        cur = con.cursor()
        cur.execute(stmt)

        fin.seek(0)


        reader = csv.reader(escapingGenerator(fin))

        # Generate insert statement:
        stmt = "INSERT INTO ads VALUES(%s);" % ','.join('?' * len(cols))

        cur.executemany(stmt, reader)
        con.commit()

    
def dbToCsv(dbName, csvFile='outputCSV'):
    con = sqlite3.connect(str(dbName))
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablesList = cur.fetchall()
    for table_name in tablesList:
        table_name = table_name[0] 
        cur.execute("SELECT * from %s" % table_name)
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        fileName = str(csvFile + table_name + '.csv')
        with open(fileName, "w", newline='') as outFile:
            fieldnames = columns
            writer = csv.DictWriter(outFile,fieldnames=fieldnames)
            writer.writeheader()
            for line in results:
                writer.writerow(line)
    cur.close()
    con.close()