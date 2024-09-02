# Pagination

Pagination is an approach used to limit and display only a part of the total data of a query. Instead of returning thousands or millions of rows at the same time,
the server is requested only one page (a limited set of rows), and the user starts navigating by requesting the next page, and then the next one, and so on.

This limiting helps to reduce on network usage.

## [Types](https://nordicapis.com/everything-you-need-to-know-about-api-pagination/)

- Offset(Limit): SQL

    ```
    GET /items?limit=20&offset=100
    ```

- Keyset: uses a filter

    ```
    GET /items?limit=20
    GET /items?limit=20&created:lte:2021-01-19T00:00:00
    ```

- Seek

    ```
    GET /items?limit=20
    GET /items?limit=20&after_id=20
    ```
