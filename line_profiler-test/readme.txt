line_profiler use abstract

a):
    kernprof -l py_script.py
    python -m line_profiler py_script.py.lprof

b):
    kernprof -lv py_script.py

memory_profiler use abstract
a):
    python -m memory_profiler py_script.py
