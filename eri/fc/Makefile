FC = gfortran
CC = gcc
LD = gcc
#LD = gfortran

FCFLAGS = -Wall -g -fPIC
CCFLAGS = -Wall -g -fPIC
LDFLAGS = -Wall -g -fPIC

EXEF  = test_intf
EXECF = test_intfc
EXECC = test_intcc
OBJSF = main_intf.o
OBJSFC = main_intfc.o
OBJSCC = main_intcc.o

LIBFLAGS = -L../molint -lmolint -lgfortran

all: $(EXEF) $(EXEFC) $(EXECC)

$(EXEF): $(OBJSF)
	$(FC) $(LDFLAGS) -o $(EXEF) $(OBJSF) $(LIBFLAGS)

$(EXEFC): $(OBJSFC)
	$(CC) $(LDFLAGS) -o $(EXEFC) $(OBJSFC) $(LIBFLAGS)

$(EXECC): $(OBJSCC)
	$(CC) $(LDFLAGS) -o $(EXECC) $(OBJSCC) $(LIBFLAGS)

main_intf.o: main_intf.f
	$(FC) $(FCFLAGS) -c main_intf.f

main_intfc.o: main_intfc.c
	$(CC) $(CCFLAGS) -c main_intfc.c

main_intcc.o: main_intcc.c
	$(CC) $(CCFLAGS) -c main_intcc.c

clean:
	-rm *.o
	-rm $(EXEF) $(EXEC) $(EXECC)
