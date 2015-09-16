EXE                 = merge.exe

COMPILATOR          = g++

COMPILATOR_OPTIONS  = -O2 -ansi 
L1                  = $(NOMAD_HOME)/lib/nomad.a
LIBS                = $(L1) -lm
INCLUDE             = -I$(NOMAD_HOME)/src -I.
COMPILE             = $(COMPILATOR) $(COMPILATOR_OPTIONS) $(INCLUDE) -c
OBJS                = merge.o


ifndef NOMAD_HOME
define ECHO_NOMAD
	@echo Please set NOMAD_HOME environment variable!
	@false
endef
endif


$(EXE): $(L1) $(OBJS)
	$(ECHO_NOMAD)
	@echo "   building the scalar version ..."
	@echo "   exe file : "$(EXE)
	@$(COMPILATOR) -o  $(EXE) $(OBJS) $(LIBS) $(COMPILATOR_OPTIONS)
	@strip  $(EXE)


merge.o: merge.cpp
	$(ECHO_NOMAD)
	@$(COMPILE) merge.cpp

$(L1) $(L1_MPI): ;
	$(ECHO_NOMAD)

all: $(EXE) $(EXE_MPI)

clean: ;
	@echo "   cleaning obj files"
	@rm -f $(OBJS) $(OBJS_MPI)

del: ;
	@echo "   cleaning trash files"
	@rm -f core *~
	@echo "   cleaning obj files"
	@rm -f $(OBJS) $(OBJS_MPI)
	@echo "   cleaning exe file"
	@rm -f $(EXE) $(EXE_MPI)


