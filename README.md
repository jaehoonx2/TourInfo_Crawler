# INTRO
* This project is for studying Python syntax, basic crawling methods and DB integration with Python.
* This project is used only for my studying, not other purposes.

# py_project
* An Python-based program that crawls information from Interpark Tour page.
* Interpark Tour page URL: https://tour.interpark.com/
* Please DO USE the project only for studying

# Getting Started
* Python 3.x version is needed.
* Selenium, BeautifulSoup, and PyMysql should be installed.
* MariaDB is also used and SQL queries that used in the project are as below.

# etc.
* Install modules (pip - Win, pip3 - MacOS or Linux)
    pip/pip3 install selenium
    pip/pip3 install bs4
    pip/pip3 install pymysql

* MariaDB queries
    CREATE DATABASE pythonDB;

    CREATE TABLE tbl_keyword (
        keyword VARCHAR(50) NOT NULL PRIMARY KEY
    );

    CREATE TABLE tbl_crawlingData (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(50),
        price VARCHAR(50),
        area VARCHAR(50),
        contents TEXT,
        keyword VARCHAR(50),
        regdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    INSERT INTO tbl_keyword VALUES ('city_you_want_to_go');