FC = gfortran
CC = gcc
LD = gcc
FCFLAGS = -Wall -g -fPIC -I.
CCFLAGS = -Wall -g -fPIC -I.

SO = libmolint.so
OBJFS = int1_s_drv_f.o int1_t_drv_f.o int1_v_drv_f.o int2_drv_f.o
OBJS = fmt.o int1_coefs.o int1_iic.o int1_s_drv.o int1_s_rec_call.o int1_s_rec_drv.o int1_s_rec_verexec.o int1_save.o int1_t_drv.o int1_t_rec_call.o int1_t_rec_drv.o int1_t_rec_verexec.o int1_v_drv.o int1_v_rec_call.o int1_v_rec_drv.o int1_v_rec_verexec.o int2_atomic.o int2_drv.o int2_iic.o int2_rec_call.o int2_rec_drv.o int2_rec_horexec.o int2_rec_verexec.o int2_save.o $(OBJFS)

###############################################
LDFLAGS = -Wall -g -fPIC -Wl,-soname,$(SO) -lgfortran -lstdc++

all: $(SO)
$(SO): $(OBJS)
	$(CC) $(LDFLAGS) -shared -o $(SO) $(OBJS)

int1_s_drv_f.o: int1_s_drv_f.f
	$(FC) $(FCFLAGS) -c int1_s_drv_f.f
int1_t_drv_f.o: int1_t_drv_f.f
	$(FC) $(FCFLAGS) -c int1_t_drv_f.f
int1_v_drv_f.o: int1_v_drv_f.f
	$(FC) $(FCFLAGS) -c int1_v_drv_f.f
int2_drv_f.o: int2_drv_f.f
	$(FC) $(FCFLAGS) -c int2_drv_f.f

fmt.o: fmt.c
	$(CC) $(CCFLAGS) -c fmt.c
int1_coefs.o: int1_coefs.c
	$(CC) $(CCFLAGS) -c int1_coefs.c
int1_iic.o: int1_iic.c
	$(CC) $(CCFLAGS) -c int1_iic.c
int1_s_drv.o: int1_s_drv.c
	$(CC) $(CCFLAGS) -c int1_s_drv.c
int1_s_rec_call.o: int1_s_rec_call.c
	$(CC) $(CCFLAGS) -c int1_s_rec_call.c
int1_s_rec_drv.o: int1_s_rec_drv.c
	$(CC) $(CCFLAGS) -c int1_s_rec_drv.c
int1_s_rec_verexec.o: int1_s_rec_verexec.c
	$(CC) $(CCFLAGS) -c int1_s_rec_verexec.c
int1_save.o: int1_save.c
	$(CC) $(CCFLAGS) -c int1_save.c
int1_t_drv.o: int1_t_drv.c
	$(CC) $(CCFLAGS) -c int1_t_drv.c
int1_t_rec_call.o: int1_t_rec_call.c
	$(CC) $(CCFLAGS) -c int1_t_rec_call.c
int1_t_rec_drv.o: int1_t_rec_drv.c
	$(CC) $(CCFLAGS) -c int1_t_rec_drv.c
int1_t_rec_verexec.o: int1_t_rec_verexec.c
	$(CC) $(CCFLAGS) -c int1_t_rec_verexec.c
int1_v_drv.o: int1_v_drv.c
	$(CC) $(CCFLAGS) -c int1_v_drv.c
int1_v_rec_call.o: int1_v_rec_call.c
	$(CC) $(CCFLAGS) -c int1_v_rec_call.c
int1_v_rec_drv.o: int1_v_rec_drv.c
	$(CC) $(CCFLAGS) -c int1_v_rec_drv.c
int1_v_rec_verexec.o: int1_v_rec_verexec.c
	$(CC) $(CCFLAGS) -c int1_v_rec_verexec.c
int2_atomic.o: int2_atomic.c
	$(CC) $(CCFLAGS) -c int2_atomic.c
int2_drv.o: int2_drv.c
	$(CC) $(CCFLAGS) -c int2_drv.c
int2_iic.o: int2_iic.c
	$(CC) $(CCFLAGS) -c int2_iic.c
int2_rec_call.o: int2_rec_call.c
	$(CC) $(CCFLAGS) -c int2_rec_call.c
int2_rec_drv.o: int2_rec_drv.c
	$(CC) $(CCFLAGS) -c int2_rec_drv.c
int2_rec_horexec.o: int2_rec_horexec.c
	$(CC) $(CCFLAGS) -c int2_rec_horexec.c
int2_rec_verexec.o: int2_rec_verexec.c
	$(CC) $(CCFLAGS) -c int2_rec_verexec.c
int2_save.o: int2_save.c
	$(CC) $(CCFLAGS) -c int2_save.c

clean:
	-rm $(OBJS)
	-rm $(SO)
