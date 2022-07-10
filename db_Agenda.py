import sqlite3, sys

class Tabla():
	db = sqlite3.connect("agenda.db")
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS contactos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50), email VARCHAR(50), telf VARCHAR(50))")
	db.commit()

class Conexion(object):
	"""docstring for Conexion"""
	db = None
	_cursor = None

	@classmethod
	def conexion(cls):
		if cls.db is None:
			try:
				cls.db = sqlite3.connect('agenda.db')
				return cls.db
			except Exception as e:
				print(f'Ocurrio un error {e}')
				sys.exit()
		else:
			return cls.db

	@classmethod
	def cursor(cls):
		if cls._cursor is None:
			try:
				cls._cursor = cls.conexion().cursor()
				#print(f'Cursor Creado {cls._cursor}')
				return cls._cursor
			except Exception as e:
				print(f'Ocurrio un error {e}')
				sys.exit()
		else:
			return cls._cursor
