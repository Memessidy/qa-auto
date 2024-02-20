import sqlite3
from modules.common.data_generators.product_generators import product_generator
database_path = r'D:\qa-auto\become_qa_auto.db'


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, PostalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = '{product_id}'"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = (f"INSERT OR REPLACE INTO products (id, name, description, quantity) "
                 f"VALUES ({product_id}, '{name}', '{description}', {qnt})")
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id == {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_all_products(self):
        query = f"SELECT * FROM products"
        return self.return_fetched_data(query)

    def get_detailed_orders(self):
        query = """
        SELECT orders.id, customers.name, products.name, products.description,
        orders.order_date
        FROM orders
        JOIN customers
        ON orders.customer_id == customers.id
        JOIN products
        ON orders.product_id == products.id
        """

        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_detailed_orders_by_name(self, name):
        query = f"""
        SELECT orders.id, customers.name, products.name, products.description,
        orders.order_date
        FROM orders
        JOIN customers
        ON orders.customer_id == customers.id
        JOIN products
        ON orders.product_id == products.id
        WHERE customers.name = '{name}'
        """
        return self.return_fetched_data(query)

    def add_new_order_now(self, order_id, customer_id, product_id):
        query = f"""
        INSERT OR REPLACE INTO orders VALUES ({order_id}, {customer_id}, {product_id}, DATETIME('now'))
        """
        self.cursor.execute(query)
        self.connection.commit()

    def delete_order_by_id(self, id):
        query = f"DELETE FROM orders WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def update_order_date_by_id(self, id, date):
        query = f"UPDATE orders SET order_date = '{date}' WHERE id == {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_average_quantity_from_products(self):
        query = "SELECT avg(quantity) FROM products;"
        return self.return_fetched_data(query)

    def insert_multiple_products(self, start, count):
        query = f"INSERT INTO products (id, name, description, quantity) VALUES {product_generator(start, count)};"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_new_products(self, max_id):
        query = f"DELETE FROM products WHERE id > {max_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_products_count(self):
        query = "SELECT COUNT(*) FROM 'products'"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def sort_products_by_description_length(self):
        query = "SELECT name, description FROM products ORDER BY LENGTH(description) DESC"
        return self.return_fetched_data(query)

    def sort_products_by_quantity(self):
        query = "SELECT name, quantity FROM products ORDER BY quantity DESC"
        return self.return_fetched_data(query)

    def return_fetched_data(self, query):
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
