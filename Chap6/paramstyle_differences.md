Python's DB-API supports a variety of ways to pass parameters into an SQL
statement. Some of these include:

"WHERE name=:1" - numeric parameter style: numeric positional style
"WHERE name=:name" - named style
"WHERE name=%(name)s" - pyformat style: python dictionary format conversion
