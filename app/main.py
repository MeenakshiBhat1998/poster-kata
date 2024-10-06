from typing import Union
from fastapi import FastAPI

from common import get_db_connection

app = FastAPI()


@app.get("/avgQuantityPerPurchase/{poster_content}")
def avg_quantity_per_purchase(poster_content: str):
        """
        This endpoint calculates the average quantity bought in a single purchase for a given poster content.

        Args:
            poster_content (str): The content of the poster to calculate the average quantity for.

        Returns:
            dict: A dictionary containing the average quantity bought in a single purchase for the given poster content.
        """
        conn = get_db_connection()
        cur = conn.cursor()

        query = (f"SELECT AVG(quantity) AS average_quantity FROM dw WHERE poster_content = '{poster_content}';")
        cur.execute(query)
        rows = cur.fetchall()
        average_quantity = rows[0][0]
        conn.commit()
        cur.close()
        conn.close()

        return {"average_quantity": average_quantity}


@app.get("/getFilmAndReleaseDate/{poster_content}")
def get_film_and_release_date(poster_content: str):
    """
    This endpoint retrieves the film name and release date for a given poster content.

    Args:
        poster_content (str): The content of the poster to retrieve the film name and release date for.

    Returns:
        dict: A dictionary containing the film name and release date for the given poster content.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    query = (f"SELECT film_name, release_date FROM dw WHERE poster_content = '{poster_content}';")
    cur.execute(query)
    rows = cur.fetchall()
    res = []
    for response in rows:
        res.append({"film_name": response[0], "release_date": response[1]})
    conn.commit()
    cur.close()
    conn.close()

    return res

@app.get("/getTotalSales/{poster_content}")
def get_total_sales(poster_content: str):
    """
    This endpoint retrieves the total sales for a given poster_content name.

    Args:
        poster_content (str): The content of the poster to retrieve the total sales for.

    Returns:
        dict: A dictionary containing the total sales for the given starship name.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    query = (f"SELECT SUM(price * quantity)  AS total_sales FROM dw WHERE poster_content = '{poster_content}';")
    cur.execute(query)
    rows = cur.fetchall()
    total_sale_amount = rows[0][0]
    conn.commit()
    cur.close()
    conn.close()

    return {"total_sale_amount": total_sale_amount}
