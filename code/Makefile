# Builds the C kernels used by the Python drivers (Linux, gcc; on Windows use WSL).
#   make          builds the four shared libraries
#   make clean    removes them
# Each library is loaded by ctypes from the directory of the Python module that needs it.
CC = gcc
CFLAGS ?= -O3 -fPIC
LIBS = nonlinear/libdouble_null.so eh_init/libdouble_null.so eh_init/libstream.so eh_init/libstream2.so

all: $(LIBS)

nonlinear/libdouble_null.so: nonlinear/double_null.c
	$(CC) $(CFLAGS) -shared -o $@ $< -lm

eh_init/libdouble_null.so: eh_init/double_null.c
	$(CC) $(CFLAGS) -shared -o $@ $< -lm

eh_init/libstream.so: eh_init/stream.c
	$(CC) $(CFLAGS) -shared -o $@ $< -lm

# stream2.c is built without fast-math (the cumulative trapezoid integral I(s) must not be reordered)
eh_init/libstream2.so: eh_init/stream2.c
	$(CC) $(CFLAGS) -shared -o $@ $< -lm

clean:
	rm -f $(LIBS)

.PHONY: all clean
