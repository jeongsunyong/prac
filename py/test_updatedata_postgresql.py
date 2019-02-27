
#!/usr/bin/env python
import psycopg2 

def update_project(project_id, project_name):
    sql = """ UPDATE projects
                SET project_name = %s
                WHERE project_id = %s"""
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(host="10.10.10.162",database="projects", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute(sql, (project_name, project_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return updated_rows
if __name__ == '__main__':
    update_project("2","REDVELVET-BADBOY")
