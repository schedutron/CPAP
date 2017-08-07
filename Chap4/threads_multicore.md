On single core systems, multiple threads execute on a single thread via a task
scheduler. I think on multicore systems, different threads spread out on
different cores (i.e, true parallelism), and if there are more threads to be
executed than there are cores (which IMO happens most of the time), then again
task schedulers would be employed on one or more of the cores.
