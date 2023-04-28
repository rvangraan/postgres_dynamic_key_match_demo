from psycopg2.extras import RealDictCursor
import psycopg2.extensions

connection = psycopg2.connect(
    database="rvg.work",
    user="rvg.work",
    host="localhost",
#    password="postgres",
    port=5432,
    cursor_factory=RealDictCursor,
)

connection.set_isolation_level(
    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
)


def query( sql, args):
    connection.notices.clear()
    cursor = connection.cursor()
    cursor.execute(sql, args)
    return cursor


def match_keys(match_values : dict):
    sql = '''
        SELECT * FROM demo
    '''
    params = []
    index = 0
    if len(match_values) > 0:
        sql += ' WHERE '
    for key, value in match_values.items():
        index += 1
        if index > 1:
            sql += " and"

        sql += f"\nkeys ->>'{key}' = %s"
        params.append(value)

    print(f"SQL: {sql}")

    cursor = query(sql, params)
    return cursor.fetchall()

def pretty(results):
    print("Match:")
    for row in results:
        id = row['id']
        keys = row['keys']
        print(f"{id}: {keys}")

pretty(match_keys({"a": "1", "c": "2"}))
pretty(match_keys({"c": "2"}))
pretty(match_keys({"acquiring_institution_id": "1234"}))

