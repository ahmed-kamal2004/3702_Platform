import asyncio
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector.pooling import PooledMySQLConnection

while True:
    try:
        pool = MySQLConnectionPool(
            pool_name="pool",
            pool_size=30,
            host="localhost",
            database="platform",
            user="root",
            password="9341",
        )
    except Exception as e:
        print(e)
    else:
        break


async def get_conn():
    conn = await asyncio.get_event_loop().run_in_executor(None, pool.get_connection)
    return conn


async def release_conn(conn: PooledMySQLConnection):
    await asyncio.get_event_loop().run_in_executor(None, conn.close)
