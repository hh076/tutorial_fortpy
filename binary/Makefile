FC = gfortran
CC = gcc
LD = gfortran

FCFLAGS = -Wall -g -I. -fPIC
CCFLAGS = -Wall -g -I. -fPIC

LDFLAGS = -Wall
LDFLAGS = -Wall -g -fPIC -Wl,-soname,$(SO) -lgfortran -lstdc++

SO = libreadfort.so
OBJSLIB = readfort.o
OBJS =


all: $(SO) exe
exe: test_writef test_readf test_readc

$(SO): $(OBJSLIB)
	$(LD) $(LDFLAGS) -shared -o $(SO) $(OBJSLIB)

readfort.o: readfort.f
	$(FC) $(FCFLAGS) -c readfort.f

test_writef: test_write.f
	$(FC) $(FCFLAGS) -o test_writef test_write.f

test_readf: test_read.f
	$(FC) $(FCFLAGS) -o test_readf  test_read.f

test_readc: test_read.c
	$(CC) $(CCFLAGS) -o test_readc  test_read.c


clean:
	-rm test_writef
	-rm test_readf
	-rm test_readc
	-rm *.o
	-rm *.so
	-rm fort.99
