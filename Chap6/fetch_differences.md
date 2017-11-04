fetchone() - fetches the next row of query result
fetchmany([size=cursor.arraysize]) - fetches next size rows of query result,
                                     i.e., if size is 3, fetches next 3 rows
                                     if available
fetchall() - fetches all remaining rows of query result