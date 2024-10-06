"""
This module contains functions to fetch starship data from the SWAPI API and process it.
"""

import aiohttp
import asyncio


async def fetch(url, session):
    """
    Fetches the content from the given URL using the provided session.

    Args:
        url (str): The URL to fetch the content from.
        session (aiohttp.ClientSession): The session to use for making the request.

    Returns:
        dict: The JSON response from the URL.
    """

    async with session.get(url) as response:
        return await response.json()

async def fetch_all_starships():
    """
    Fetches all starships from the given base URL using asynchronous requests.

    Args:
        base_url (str): The base URL to start fetching starship data from.

    Returns:
        list: A list of dictionaries containing starship data.
    """

    base_url = "https://swapi.dev/api/starships/"

    async with aiohttp.ClientSession() as session:
        starships = []
        url = base_url

        while url:
            data = await fetch(url, session)
            starships.extend(data['results'])
            url = data['next']  # Proceed to next page if available

        for starship in starships:
            # Prepare to fetch all films concurrently
            film_tasks = [fetch(film_url, session) for film_url in starship["films"]]
            film_responses = await asyncio.gather(*film_tasks)

            # Process each film response
            for film_response in film_responses:
                if 'release_date' in film_response and 'title' in film_response:
                    starship["release_date"] = film_response["release_date"]
                    starship["film_name"] = film_response["title"]
        return starships
