# Core Python Applications Programming
## by Wesley Chun
### My Solutions to the Rigorous Exercises in the Excellent Book
(Most of them in Python 3)
***
[Library Requirements File (For Python2)][req2]
***
![Lines of code](https://tokei.rs/b1/github/schedutron/CPAP)

* [Chapter 4: Multithreaded Programming][chap4]
    * [Example 4-10: Locks and More Randomness (mtsleepF.py)][e4-10]
    * [Example 4-11: Candy Vending Machines and Semaphores (candy.py)][e4-11]
    * [Example 4-12: Producer-Consumer Problem (prodcons.py)][e4-12]
    * [Example 4-13: Higher-Level Job Management (bookrank3CF.py)][e4-13]
    * ***
    * [Exercise 4-1: Processes vs. Threads (processes_vs_threads.md)][4-1]
    * [Exercise 4-2: Utility of multithreading in Python (python_threads.md)][4-2]
    * [Exercise 4-3: Mulithreading on Multicore System (threads_multicore.md)][4-3]
    * [Exercise 4-4-a: Simple Byte Count (bytes_count.py)][4-4-a]
    * [Exercise 4-4-b: Multithreaded Byte Count (mt_bytes_count.py)][4-4-b]
    * Exercise 4-5: Threads, Files and Regex ([mt_simple_header_analysis.py][4-5-i], [simple_header_analysis.py][4-5-ii])
    * Exercise 4-6: Threads and Networking ([mt_duplex_chat_serv.py][4-6-i], [mt_duplexc_chat_clnt.py][4-6-ii])
    * [Exercise 4-7: Threads and Web Programming (Optional, to be done)(mtcrawl.py)][4-7]
    * [Exercise 4-8: Thread Pools (thread_pools.py)][4-8]
    * [Exercise 4-9: Files (mt_lines_counter.py) Single threaded version runs faster than the multithreaded one.][4-9]
    * [Exercise 4-10: Concurrent Processing (concurrent_processing.py)][4-10]
    * [Exercise 4-11: Synchronization Primitives (sync_prim.md)][4-11]
    * [Exercise 4-12: Porting to Python 3 (already built Example 4-11 in Python3) (candy.py)][e4-11]
***

* [Chapter 5: GUI Programming][chap5]
    * [Example 5-1: Label Widget Demo (changed in Exercise 5-3) (tkhello1.py)][e5-1]
    * [Example 5-2: Button Widget Demo (tkhello2.py)][e5-2]
    * [Example 5-3: Label and Button Widget Demo (Changed in Exercise 5-4) (tkhello3.py)][e5-3]
    * [Example 5-4: Label, Button and Scale Demonstration (tkhello4.py)][e5-4]
    * [Example 5-5: Road Signs PFA GUI Application (pfaGUI.py)][e5-5]
    * [Example 5-6: File System Traversal GUI (listdir.py)][e5-6]
    * [Example 5-7: Tix GUI Demo (animalTix.pyw)][e5-7]
    * [Example 5-8: Pmw GUI Demo (modified in Exercise 5-10) (animalPmw.pyw)][e5-8]
    * [Example 5-9: wxPython GUI Demo (modified in Exercise 5-10) (animalWx.pyw)][e5-9]
    * [Example 5-10: PyGTK GUI Demo (animalGtk.pyw)][e5-10]
    * [Example 5-11: Tile/Ttk GUI Demo (animalTtk.pyw)][e5-11]
    * [Example 5-12: Tile/Ttk Python 3 GUI Demo (animalTtk3.pyw)][e5-12]
    * ***
    * Exercise 5-1: Client/Server Architecture ([client\_server\_architecture.md][5-1])
    * Exercise 5-2: Object-Oriented Programming ([oop.md][5-2])
    * Exercise 5-3: Label Widgets ([tkhello1.py][5-3])
    * Exercise 5-4: Label and Button Widgets (modified in Exercise 5-5) ([tkhello3.py][5-4])
    * Exercise 5-5: Label, Button and Radiobutton Widgets (modified in Exercise 5-6) ([tkhello3.py][5-5])
    * Exercise 5-6: Label, Button and Entry Widgets ([tkhello3.py][5-6])
    ![Output for Exercise 5-6](/Chap5/screenshots/E5-6.png)
    * Exercise 5-7: Label and Entry Widgets and Python I/O (extra credit stuff will be done later) ([file_reader.py][5-7])
    ![Output for Exercise 5-7](/Chap5/screenshots/E5-7.png)
    * Exercise 5-8: Simple Text Editor ([text_editor.py][5-8])
    ![Output for Exercise 5-8](/Chap5/screenshots/E5-8-0.png)
    ![Output for Exercise 5-8](/Chap5/screenshots/E5-8-1.png)
    * Exercise 5-9: Multithreaded Chat Applications ([chat_serv.py][5-9-1], [chat_clnt_GUI.py][5-9-2])
    ![Output for Exercise 5-9](/Chap5/screenshots/E5-9-1.png)
    ![Output for Exercise 5-9](/Chap5/screenshots/E5-9-2.png)
    ![Output for Exercise 5-9](/Chap5/screenshots/E5-9-0.png)
    * Exercise 5-10: Using Other GUIs (some are not working on my system, so very little modification is done.) ([animalPmw.pyw][5-10-0], [animalWx.pyw][5-10-1])
    * Exercise 5-11: Using GUI Builders. I had problems in either installation, download or running of the builders (some of them maybe due to version mismatch). Thus, perhaps later.
***

* [Chapter 6: Database Programming][chap6]
    * [Example 6-1: Database Adapter Example][e6-1]
    * [Example 6-2: SQLAlchemy ORM Example][e6-2]
    * [Example 6-3: SQLObject ORM Example][e6-3]
    * [Example 6-4: MongoDB Example][e6-4]
    * ***
    * Exercise 6-1: Database API ([db_api.md][6-1])
    * Exercise 6-2: Database API ([paramstyle_differences.md][6-2])
    * Exercise 6-3: Cursor Objects ([execute_differnces.md][6-3])
    * Exercise 6-4: Cursor Objects ([fetch_differences.md][6-4])
    * Exercise 6-5: Database Adapters ([pgsql_features.md][6-5])
    * Exercise 6-6: Type Objects ([psql_sample.py][6-6])
    * Exercise 6-7: Refactoring ([ushuffle_dbU.py][6-7])
    * Exercise 6-8: Database and HTML ([db_to_html.py][6-8-1], [output.html][6-8-2])
    ![Output for Exercise 6-8](/Chap6/screenshots/E6-8.png)
    * Exercise 6-9: Web Programming and Databases (not implemented yet as I don't know much about web programming as of this writing)
    * Exercise 6-10: GUI Programming and Databases ([db_GUI.py][6-10])
    ![Partial Output for Exercise 6-10](/Chap6/screenshots/E6-10.png)
    * Exercise 6-11: Stock Portfolio Class (not implemented yet as I don't know much about web programming as of this writing)
    * Exercise 6-12: Debugging & Refactoring ([ushuffle_dbU.py][6-12])
    * Exercise 6-13: Stock Portfolio Class (not implemented as it depends on Exercise 6-11, shall do after sufficient learning)
    * Exercise 6-14: To be done later; same reason as above.
    * Exercise 6-15: Supporting Different RDBMSs ([ushuffle_sad.py][6-15])
    * Exercise 6-16: Importing and Python ([builtins_explanation.md][6-16])
    * Exercise 6-17: Porting to Python 3 ([warn\_vs\_print.md][6-17])
    * Exercise 6-18: Porting to Python 3 ([print\_vs\_print_function.md][6-18])
    * Exercise 6-19: Python Language ([towards_universal.md][6-19])
    * Exercise 6-20: Exceptions: added functionality, but unable to test as of this writing ([ushuffle_sad.py][6-20])
    * Exercise 6-21: SQLAlchemy (a: [ushuffle_sad.py][6-21-a], b: [ushuffle_sad.py][6-21-b])
    * Exercise 6-22: SQLAlchemy ([ushuffle_sad.py][6-22]) The query `update()` method was faster than the procedure we used before; I used `time` instead of `timeit` because of its convenience. The `update()` method took about 0.0026s, whereas the previous method took about 0.004s on my system.
    * Exercise 6-23: SQLAlchemy ([ushuffle_sad.py][6-23]) Again, the query `delete()` method was faster than the previous procedure. It took about 0.001s to run, whereas the previous procedure took about 0.003s to run on my system. And again, `time` was used instead of `timeit`.
    * Exercise 6-24: SQLAlchemy \(Kinda\) ([ushuffle_sae.py][6-24])
    * Exercise 6-25: Django Data Models: Shall do later, don't know much Django as of this writing.
    * Exercise 6-26: Storm ORM - tried installing storm, in vain
    * Exercise 6-27: NoSQL ([for_nosql.md][6-27])
    * Exercise 6-28: NoSQL ([nosql_types.md][6-28])
    * Exercise 6-29: CouchDB ([ushuffle_couch.py][6-29])
***

* Chapter 7: Programming Microsoft Office (optional; will do later)
***

* [Chapter 8: Extending Python][chap8]
    * Example 8-1: Pure C Version of Library ([Extest1.c][e8-1])
    * Example 8-2: The Build Script ([setup.py][e8-2])
    * Example 8-3: Python-Wrapped Version of C Library ([Extest2.c][e8-3])
    * ***
    * Exercise 8-1: Extending Python ([extension_advantages.md][8-1])
    * Exercise 8-2: Extending Python ([extension_disadvantages][8-2])
    * Exercise 8-3: Writing Extensions ([upper.c][8-3-i], [upper_setup.py][8-3-ii])
    * Exercise 8-4: Porting from Python to C (implemented timestamp server and client from Chapter 2 as a Python extension, shall port about a couple more exericses later **\[Incomplete\]**) ([chat.c][8-4-i], [chat_setup.py][8-4-ii])
    * Exercise 8-5: Wrapping C Code ([helloWorld.c][8-5-i], [hello_setup.py][8-5-ii])
    * Exercise 8-6: Writing Extensions - not done as I haven't read either of the mentioned books
    * Exercise 8-7: Extending vs. Embedding ([extending_vs_embedding.md][8-7])
    * Exercise 8-8: Not Writing Extensions ([helloworld.pyx][8-8-i], [cy_setup.py][8-8-ii])
***
### Web Development

* [Chapter 9: Web Clients and Servers][chap9]
    * Example 9-1: Basic HTTP Authentication ([urlopen_auth.py][e9-1])
    * Example 9-2:  Python3 HTTP Authentication Script ([urlopen_auth3.py][e9-2])
    * Example 9-3: Web Crawler ([crawl.py][e9-3])
    * Example 9-4: Link Parser ([parse_links.py][e9-4])
    * Example 9-5: Programmatic Web Browsing ([mech.py][e9-5])
    * Example 9-6: Simple Web Server ([myhttpd.py][e9-6])

    Exercises coming soon...
***

* [Chapter 10: Web Programming: CGI and WSGI][chap10]
    * Example 10-1: Static Form Web Page ([friends.htm][e10-1])
    * Example 10-2: Results CGI Screen Code ([friendsA.py][e10-2])

[req2]: /requirements.txt
[chap4]: /Chap4
[e4-10]: /Chap4/mtsleepF.py
[e4-11]: /Chap4/candy.py
[e4-12]: /Chap4/prodcons.py
[e4-13]: /Chap4/bookrank3CF.py
[4-1]: /Chap4/processes_vs_threads.md
[4-2]: /Chap4/python_threads.md
[4-3]: /Chap4/threads_multicore.md
[4-4-a]: /Chap4/bytes_count.py
[4-4-b]: /Chap4/mt_bytes_count.py
[4-5-i]: /Chap4/simple_header_analysis.py
[4-5-ii]: /Chap4/mt_simple_header_analysis.py
[4-6-i]: /Chap4/mt_duplex_chat_serv.py
[4-6-ii]: /Chap4/mt_duplexc_chat_clnt.py
[4-7]: /Chap4/mtcrawl.py
[4-8]: /Chap4/thread_pools.py
[4-9]: /Chap4/mt_lines_counter.py
[4-10]: /Chap4/concurrent_processing.py
[4-11]: /Chap4/sync_prim.md

[chap5]: /Chap5
[e5-1]: /Chap5/tkhello1.py
[e5-2]: /Chap5/tkhello2.py
[e5-3]: /Chap5/tkhello3.py
[e5-4]: /Chap5/tkhello4.py
[e5-5]: /Chap5/pfaGUI.py
[e5-6]: /Chap5/listdir.py
[e5-7]: /Chap5/animalTix.pyw
[e5-8]: /Chap5/animalPmw.pyw
[e5-9]: /Chap5/animalWx.pyw
[e5-10]: /Chap5/animalGtk.pyw
[e5-11]: /Chap5/animalTtk.pyw
[e5-12]: /Chap5/animalTtk3.pyw
[5-1]: /Chap5/client_server_architecture.md
[5-2]: /Chap5/oop.md
[5-3]: /Chap5/tkhello1.py
[5-4]: /Chap5/tkhello3.py
[5-5]: /Chap5/tkhello3.py
[5-6]: /Chap5/tkhello3.py
[5-7]: /Chap5/file_reader.py
[5-8]: /Chap5/text_editor.py
[5-9-1]: /Chap5/chat_clnt.py
[5-9-2]: /Chap5/chat_clnt_GUI.py
[5-10-0]: /Chap5/animalPmw.pyw
[5-10-1]: /Chap5/animalWx.pyw

[chap6]: /Chap6
[e6-1]: https://github.com/schedutron/CPAP/blob/930517d2e7a746145162884b6f7c5262f8480c43/Chap6/ushuffle_dbU.py
[e6-2]: https://github.com/schedutron/CPAP/blob/8a3659b0b8576f4dffc4a874703d2f982163abbc/Chap6/ushuffle_sad.py
[e6-3]: /Chap6/ushuffle_so.py
[e6-4]: /Chap6/ushuffle_mongo.py
[6-1]: /Chap6/db_api.md
[6-2]: /Chap6/paramstyle_differences.md
[6-3]: /Chap6/execute_differences.md
[6-4]: /Chap6/fetch_differences.md
[6-5]: /Chap6/pgsql_features.md
[6-6]: /Chap6/psql_sample.py
[6-7]: https://github.com/schedutron/CPAP/blob/e140858c63b8aef1be5c97daf55db05d3825abd2/Chap6/ushuffle_dbU.py
[6-8-1]: /Chap6/db_to_html.py
[6-8-2]: /Chap6/output.html
[6-10]: /Chap6/db_GUI.py
[6-12]: /Chap6/ushuffle_dbU.py
[6-15]: https://github.com/schedutron/CPAP/blob/ba0bdfe1de9afc012aff6b89bf5c61c6348992a9/Chap6/ushuffle_sad.py
[6-16]: /Chap6/builtins_explanation.md
[6-17]: /Chap6/warn_vs_print.md
[6-18]: /Chap6/print_vs_print_function.md
[6-19]: /Chap6/towards_universal.md
[6-20]: https://github.com/schedutron/CPAP/blob/fe49905c4663e11ea6598bf7963efde20559af4b/Chap6/ushuffle_sad.py
[6-21-a]: https://github.com/schedutron/CPAP/blob/7483748e9f03b235ca0dc0cc4e9cb8ee85202f72/Chap6/ushuffle_sad.py
[6-21-b]: https://github.com/schedutron/CPAP/blob/845838cc4f24710c10127f6043d6342077979d46/Chap6/ushuffle_sad.py
[6-22]: https://github.com/schedutron/CPAP/blob/5dcd8dd71add11a7a369d49c2413963ec8c1057d/Chap6/ushuffle_sad.py
[6-23]: /Chap6/ushuffle_sad.py
[6-24]: /Chap6/ushuffle_sae.py
[6-27]: /Chap6/for_nosql.md
[6-28]: /Chap6/nosql_types.md
[6-29]: /Chap6/ushuffle_couch.py

[chap8]: /Chap8
[e8-1]: /Chap8/Extest1.c
[e8-2]: /Chap8/setup.py
[e8-3]: /Chap8/Extest2.c
[8-1]: /Chap8/extension_advantages.md
[8-2]: /Chap8/extension_disadvantages.md
[8-3-i]: /Chap8/upper.c
[8-3-ii]: /Chap8/upper_setup.py
[8-4-i]: /Chap8/chat.c
[8-4-ii]: /Chap8/chat_setup.py
[8-5-i]: https://github.com/schedutron/CPAP/blob/edaf04b73f4de39547fe76b26cb5859d5af07c52/Chap8/helloWorld.c
[8-5-ii]: /Chap8/hello_setup.py
[8-7]: /Chap8/extending_vs_embedding.md
[8-8-i]: /Chap8/helloworld.pyx
[8-8-ii]: /Chap8/cy_setup.py

[chap9]: /Chap9
[e9-1]: /Chap9/urlopen_auth.py
[e9-2]: /Chap9/urlopen_auth3.py
[e9-3]: /Chap9/crawl.py
[e9-4]: /Chap9/parse_links.py
[e9-5]: /Chap9/mech.py
[e9-6]: /Chap9/myhttpd.py

[chap10]: /Chap10
[e10-1]: /Chap10/friends.htm
[e10-2]: /Chap10/cgi-bin/friendsA.py
