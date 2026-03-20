from src.models.usuario import crear_tabla

def crear_tabla():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            contraseña TEXT
        )
    """)

    conn.commit()
    conn.close()