import sqlite3
import math
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to a SQLite database.
    
    Parameters:
        db_file: The db_file to connect to or create    
    Return:
        conn: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement

    Paremeters:
        conn: Connection object.
        create_table_sql: a create table sql statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_project(conn, project):
    """Create a new project in the projects table

    Parameters:
        conn: Connection object
        project: Tuple containing project values
    Return:
        cur.lastrowid: Last row that was inserted
    """
    sql = '''INSERT INTO projects(name,begin_date,end_date)
            VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_task(conn, task):
    """Create a new project in the projects table

    Parameters:
        conn: Connection object
        task: Tuple containing task values
    Return:
        cur.lastrowid: Last row that was inserted
    """
    sql = '''INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
            VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def update_task(conn, task):
    """Update task priority, begin_date and end_date

    Parameters:
        conn: DB Connection object
        task: Tuple containing task values
    Return:
        None.
    """
    sql = '''UPDATE tasks
            SET priority = ?,
                begin_date = ?,
                end_date = ?
            WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    
def delete_task(conn, id):
    """Delete tasks based on their id

    Parameters:
        conn: DB connection object
        id (int): id of tasks
    Return:
        None.
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    # Don't forget that you have to provide a tuple
    cur.execute(sql, (id,))
    conn.commit()

def delete_all_tasks(conn):
    """Delete all tasks based on their id

    Parameters:
        conn: DB connection object
    Return:
        None.
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    # Don't forget that you have to provide a tuple
    cur.execute(sql)
    conn.commit()
    

def show_help_on_create_connection():
    """Demo of the Python help function and reading docstrings."""
    help(create_connection)

def print_docstring_on_create_connection():
    """Demo of the printing docstring from create_connection function."""
    print("\nThe Docstring:\n")
    print(create_connection.__doc__)
    
def select_all_tasks(conn):
    """Query all rows in tasks table

    Parameters:
        conn: DB connection object
    Return:
        None.
    """
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_tasks_by_priority(conn, priority):
    """Query tasks by priority

    Parameters:
        conn: DB connection object
        priority (int): priority level of tasks to display
    Return:
        None.
    """
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks WHERE priority=?', (priority,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = "pythonsqlite.db"
    
    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                );"""

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
    
    # Create database connection
    conn = create_connection(database)

    project = ('Cool app with SQLite & Python', '2020-01-01', '2020-01-30');
    project_id = create_project(conn, project)
     
    task_1 = ('Analyst requirements', 2, 1, project_id, '2020-01-01', '2020-01-02')
    task_2 = ('Analyst requirements', 1, 1, project_id, '2020-01-03', '2020-01-05')
    # 
    
    # Create tables
    if conn is not None:
        # create_table(conn, sql_create_projects_table)
        # create_table(conn, sql_create_tasks_table)
        # create_task(conn, task_1)
        # create_task(conn, task_2)
        # update_task(conn, (2, '2020-01-04', '2015-01-06', 2))
        # delete_task(conn, 2)
        # delete_all_tasks(conn)
        print("All:")
        select_all_tasks(conn)
        print("By Priority:")
        select_tasks_by_priority(conn, 2)
    else:
        print("Error! Cannot create database connection.")
    
    # Close db
    conn.close()
    
if __name__ == '__main__':
    main()