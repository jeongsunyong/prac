#!/usr/bin/env python
import psycopg2

def deleteProject(project_id):
	conn = None
	rows_deleted = 0
	try:
		conn = psycopg2.connect(host="10.10.10.162",database="projects",user="postgres",password="postgres")
		cur = conn.cursor()
		cur.execute("DELETE FROM projects WHERE project_id = %s", (project_id,))
		rows_deleted = cur.rowcount
		conn.commit()
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return rows_deleted

if __name__ == '__main__':
	for i in range(2274,2279):
		deleteProject(i)
