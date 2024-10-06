# Poster-kata

## Overview

`Poster-kata` is a robust data operations platform designed specifically for a company selling Star Wars posters. This application automates the process of merging and analyzing sales data from multiple sources to enhance decision-making capabilities and drive sales performance. By integrating customer data with detailed product information from the Star Wars API, `Poster-kata` provides a comprehensive view of sales trends, customer preferences, and product performance.

## Features

- **Data Integration**: Automates the extraction, transformation, and loading (ETL) of data from both internal databases and external APIs.
- **Sales Analysis**: Offers detailed insights into sales trends, including average purchase quantities, total revenue generated by specific posters, and demographic correlations based on film release dates.
- **Interactive API**: Provides endpoints for fetching specific data points like average quantities sold, associated film names, and total sales, enhancing user interaction and data accessibility.

## Technologies Used

- **FastAPI**: For building a performant and easy-to-use API.
- **PostgreSQL**: As the primary database for storing and managing structured data.
- **Docker**: For containerizing the application, ensuring consistency across different environments.
- **GitHub Actions**: Implements CI/CD pipelines for automated testing and deployment.

## Getting Started

To get a local copy up and running, follow these simple steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/poster-kata.git
   ```
2. Navigate to the project directory:
   ```bash
   cd poster-kata
   ```
3. Install dependencies:
   ```bash
   python3 -m venv poster-kata-venv
   source poster-kata-venv/bin/activate
   pip install -r requirements.txt
   pip install setup.py
   pip install -e .
   ```
4. Start the Postgres using Docker:
   ```bash
   docker-compose up -d
   ```



## Using the API

Run Application - 
   cd app
   uvicorn main:app --reload

Once the application is running, you can access the API at `http://localhost:8000`. The API documentation, generated by FastAPI, will be available at `http://localhost:8000/docs`, providing interactive endpoints where you can test API functionalities directly from your browser.

## Contributing

We welcome contributions from the community. If you wish to contribute to `Poster-kata`, please fork the repository and submit a pull request.

## USING THE CLI

```bash
poster_kata --help
```
