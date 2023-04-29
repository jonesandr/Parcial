def __init__(self) -> None:
    """
    Automatically connect to the database.
    """
    self.connection = sqlite3.connect("inventory.db")
    self.cursor = self.connection.cursor()

def show(self):
    try:
        self.cursor.execute('SELECT * FROM product')
        return self.cursor.fetchall()
    except Exception as error:
        print(error)
        return []

def add(self, name, price):
    try:
        self.cursor.execute(f"INSERT INTO product(name, price) VALUES('{name}',{price})")
        self.connection.commit()
        return True
    except Exception as error:
        print(error)
        return False

def update(self, id, name, price):
    try:
        self.cursor.execute(f"UPDATE product SET name='{name}', price={price} WHERE id={id}")
        self.connection.commit()
        return True
    except Exception as error:
        print(error)
        return False

def delete(self, id):
    try:
        if (self.exists(id)):
            self.cursor.execute(f"DELETE FROM product WHERE id={id}")
            self.connection.commit()
            return True
        print('Error: The product ID does not exist!')
        return False
    except Exception as error:
        print(error)
        return False

def exists(self, id):
    try:
        self.cursor.execute(f"SELECT * FROM product WHERE id={id}")
        return self.cursor.fetchone()
    except:
        return None

