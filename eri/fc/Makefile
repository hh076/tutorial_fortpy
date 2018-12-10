FC = gfortran
CC = gcc
LD = gcc
#LD = gfortran

FCFLAGS = -Wall -g -fPIC
CCFLAGS = -Wall -g -fPIC
LDFLAGS = -Wall -g -fPIC

EXECF  = test_intf
EXECFC = test_intfc
EXECCC = test_intcc
OBJSF  = main_intf.o
OBJSFC = main_intfc.o
OBJSCC = main_intcc.o

LIBFLAGS = -L../molint -lmolint #-lgfortran

all: $(EXECF) $(EXECFC) $(EXECCC)

$(EXECF): $(OBJSF)
	$(FC) $(LDFLAGS) -o $(EXECF)  $(OBJSF)  $(LIBFLAGS)

$(EXECFC): $(OBJSFC)
	$(CC) $(LDFLAGS) -o $(EXECFC) $(OBJSFC) $(LIBFLAGS) -lgfortran

$(EXECCC): $(OBJSCC)
	$(CC) $(LDFLAGS) -o $(EXECCC) $(OBJSCC) $(LIBFLAGS) -lgfortran

main_intf.o: main_intf.f
	$(FC) $(FCFLAGS) -c main_intf.f

main_intfc.o: main_intfc.c
	$(CC) $(CCFLAGS) -c main_intfc.c

main_intcc.o: main_intcc.c
	$(CC) $(CCFLAGS) -c main_intcc.c

clean:
	-rm *.o
	-rm $(EXECF) $(EXECFC) $(EXECCC)
