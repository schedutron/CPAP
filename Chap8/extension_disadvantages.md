One obvious disadvantage of using extensions is the overhead involved. Often,
when performance is not an issue, the overhead involved in creating extensions
is simply not worth the effort, and the same functionality can be achieved by
just pure Python code. Maintenance can be painful if people who are new to the
codebase aren't familiar with C and methods of extending Python via C or C++.
Resources which can be spent elsewhere are consumed in training new employees
with the extension methods and maintenance is just more difficult because of
many technologies involved.