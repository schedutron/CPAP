Embedding is the opposite of extending. Rather that taking C code and wrapping
it into Python, we take a large C code and embed a Python interpreter inside
it. As mentioned in the text, this has the effect of giving a monolithic
application the power of having an embedded Python interpreter. For example,
apps that provide the functionality of running a Python interpreter (perhaps
offline) on your iPhone essentially embed the Python interpreter in the phone
system. Python interpreter can be required for a multitude of purposes - for
rapid calculations, for example, which are otherwise difficult to express in
other languages.