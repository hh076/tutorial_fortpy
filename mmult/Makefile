SO = libmmult.so
OBJSLIB = mmult.o
OBJS = main_mmult.o
EXES = test_mmult

###############################################
FC = gfortran
CC = gfortran
LD = gfortran
FCFLAGS = -Wall -g -fPIC -I.
CCFLAGS = -Wall -g -fPIC -I.
LDFLAGS = -Wall -g -fPIC -L. -lmmult
SOFLAGS = -Wall -g -fPIC -Wl,-soname,$(SO) #-lgfortran -lstdc++

all: $(SO) $(EXES)
$(SO): $(OBJSLIB)
	$(CC) $(SOFLAGS) -shared -o $(SO) $(OBJSLIB)

mmult.o: mmult.f
	$(FC) $(FCFLAGS) -c mmult.f

exe: $(EXES)
test_mmult: $(SO) main_mmult.o
	$(LD) $(LDFLAGS) -o test_mmult main_mmult.o

main_mmult.o: main_mmult.f
	$(FC) $(FCFLAGS) -c main_mmult.f

clean:
	-rm $(EXES)
	-rm $(OBJS)
	-rm $(OBJSLIB)
	-rm $(SO)
	-rm *~
