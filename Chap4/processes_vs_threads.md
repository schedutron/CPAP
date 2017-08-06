# Processes versus Threads:

# Processes
Precisely speaking, processes are also called _heavyweight processes_. A process
is simply a program in execution. Every process has its own address, space, data
stack and auxiliary data to keep track of execution. Processes can spawn other
processes, but again, each process has its own data. In general, it's difficult
to communicate between different process, unless _interprocess communication_ is
employed.

# Threads
Threads are simply _lightweight processes_ that share the same context and run
in parallel with the _main_ process (which is sometimes also called the main
_thread_). Each thread has an instruction pointer which keeps track of where
within its context the thread is running. Threads within a process share the
same data space, so it's easier for them to communicate with each other than if
they were separate processes.
