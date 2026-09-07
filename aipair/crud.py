"""CRUD operations for a SQLite Products table.

The public functions accept an open ``sqlite3.Connection``. Keeping connection
ownership with the caller makes the functions useful for applications and
tests, including tests that use an in-memory database.
"""

from __future__ import annotations

import math
import sqlite3
from typing import Any


class ProductDatabaseError(RuntimeError):
    """Raised when SQLite cannot complete a product database operation."""


Product = dict[str, Any]


def _validate_connection(connection: sqlite3.Connection) -> None:
    if not isinstance(connection, sqlite3.Connection):
        raise TypeError("connection must be an open sqlite3.Connection")


def _validate_product_id(product_id: int) -> None:
    if isinstance(product_id, bool) or not isinstance(product_id, int):
        raise TypeError("product_id must be an integer")
    if product_id <= 0:
        raise ValueError("product_id must be greater than zero")


def _validate_name(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip()
    if not name:
        raise ValueError("name cannot be empty")
    if len(name) > 200:
        raise ValueError("name cannot contain more than 200 characters")
    return name


def _validate_price(price: int | float) -> float | int:
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("price must be an integer or a real number")
    if not math.isfinite(float(price)):
        raise ValueError("price must be finite")
    if price < 0:
        raise ValueError("price cannot be negative")
    return price


def _validate_quantity(qty: int) -> int:
    if isinstance(qty, bool) or not isinstance(qty, int):
        raise TypeError("qty must be an integer")
    if qty < 0:
        raise ValueError("qty cannot be negative")
    return qty


def _run_write(
        connection: sqlite3.Connection,
        query: str,
        parameters: tuple[Any, ...],
) -> sqlite3.Cursor:
    try:
        cursor = connection.execute(query, parameters)
        connection.commit()
        return cursor
    except sqlite3.Error as error:
        connection.rollback()
        raise ProductDatabaseError("SQLite write operation failed") from error


def create_products_table(connection: sqlite3.Connection) -> None:
    """Create the Products table if it does not already exist."""
    _validate_connection(connection)
    try:
        connection.execute(
            """
			CREATE TABLE IF NOT EXISTS Products (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL CHECK (length(trim(name)) > 0),
				price REAL NOT NULL CHECK (price >= 0),
				qty INTEGER NOT NULL CHECK (qty >= 0)
			)
			"""
        )
        connection.commit()
    except sqlite3.Error as error:
        connection.rollback()
        raise ProductDatabaseError(
            "Could not create the Products table") from error


def create_product(
        connection: sqlite3.Connection, name: str, price: int | float, qty: int
) -> int:
    """Insert a product and return its generated id."""
    _validate_connection(connection)
    name = _validate_name(name)
    price = _validate_price(price)
    qty = _validate_quantity(qty)
    cursor = _run_write(
        connection,
        "INSERT INTO Products (name, price, qty) VALUES (?, ?, ?)",
        (name, price, qty),
    )
    if cursor.lastrowid is None:
        raise ProductDatabaseError("SQLite did not return the new product id")
    return cursor.lastrowid


def get_product(connection: sqlite3.Connection, product_id: int) -> Product:
    """Return one product, or raise LookupError when it does not exist."""
    _validate_connection(connection)
    _validate_product_id(product_id)
    try:
        row = connection.execute(
            "SELECT id, name, price, qty FROM Products WHERE id = ?",
            (product_id,),
        ).fetchone()
    except sqlite3.Error as error:
        raise ProductDatabaseError("Could not read the product") from error
    if row is None:
        raise LookupError(f"No product exists with id {product_id}")
    return dict(row) if isinstance(row, sqlite3.Row) else {
        "id": row[0], "name": row[1], "price": row[2], "qty": row[3]
    }


def get_products(connection: sqlite3.Connection) -> list[Product]:
    """Return all products ordered by id."""
    _validate_connection(connection)
    try:
        rows = connection.execute(
            "SELECT id, name, price, qty FROM Products ORDER BY id"
        ).fetchall()
    except sqlite3.Error as error:
        raise ProductDatabaseError("Could not read the products") from error
    return [
        dict(row) if isinstance(row, sqlite3.Row) else {
            "id": row[0], "name": row[1], "price": row[2], "qty": row[3]
        }
        for row in rows
    ]


def update_product(
        connection: sqlite3.Connection,
        product_id: int,
        name: str,
        price: int | float,
        qty: int,
) -> Product:
    """Update a product and return its new values."""
    _validate_connection(connection)
    _validate_product_id(product_id)
    name = _validate_name(name)
    price = _validate_price(price)
    qty = _validate_quantity(qty)
    cursor = _run_write(
        connection,
        "UPDATE Products SET name = ?, price = ?, qty = ? WHERE id = ?",
        (name, price, qty, product_id),
    )
    if cursor.rowcount == 0:
        raise LookupError(f"No product exists with id {product_id}")
    return get_product(connection, product_id)


def delete_product(connection: sqlite3.Connection, product_id: int) -> None:
    """Delete a product, or raise LookupError when it does not exist."""
    _validate_connection(connection)
    _validate_product_id(product_id)
    cursor = _run_write(
        connection,
        "DELETE FROM Products WHERE id = ?",
        (product_id,),
    )
    if cursor.rowcount == 0:
        raise LookupError(f"No product exists with id {product_id}")


def main() -> None:
    """Exercise every CRUD function against an isolated in-memory database."""
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    try:
        create_products_table(connection)
        first_id = create_product(connection, "Keyboard", 49.99, 10)
        second_id = create_product(connection, "Mouse", 19.50, 25)
        print("Created:", get_product(connection, first_id))
        print("All products:", get_products(connection))
        print("Updated:", update_product(connection,
              first_id, "Mechanical keyboard", 79.99, 8))
        delete_product(connection, second_id)
        print("After delete:", get_products(connection))
        try:
            create_product(connection, "", -1, -2)
        except (TypeError, ValueError) as error:
            print("Validation error handled:", error)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
