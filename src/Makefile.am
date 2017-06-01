lib_LIBRARIES = libnomad.a
libnomad_a_SOURCES = Barrier.cpp Cache.cpp Cache_File_Point.cpp Cache_Point.cpp\
	Cache_Search.cpp Clock.cpp Direction.cpp Directions.cpp Display.cpp\
	Double.cpp Eval_Point.cpp Evaluator_Control.cpp Evaluator.cpp\
	Exception.cpp Extended_Poll.cpp L_Curve.cpp LH_Search.cpp Mads.cpp\
	SMesh.cpp XMesh.cpp Model_Sorted_Point.cpp Model_Stats.cpp Multi_Obj_Evaluator.cpp\
	Parameter_Entries.cpp Parameter_Entry.cpp Parameters.cpp\
	Pareto_Front.cpp Pareto_Point.cpp Phase_One_Evaluator.cpp\
	Phase_One_Search.cpp Point.cpp Priority_Eval_Point.cpp Quad_Model.cpp\
	Quad_Model_Evaluator.cpp Quad_Model_Search.cpp Random_Pickup.cpp\
	RNG.cpp Signature.cpp Slave.cpp Speculative_Search.cpp Stats.cpp\
	utils.cpp Variable_Group.cpp VNS_Search.cpp OrthogonalMesh.cpp \
	GMesh.cpp Sgtelib_Model_Evaluator.cpp Sgtelib_Model_Manager.cpp \
	Sgtelib_Model_Search.cpp


libnomadmpi_a_SOURCES = Barrier.cpp Cache.cpp Cache_File_Point.cpp Cache_Point.cpp\
	Cache_Search.cpp Clock.cpp Direction.cpp Directions.cpp Display.cpp\
	Double.cpp Eval_Point.cpp Evaluator_Control.cpp Evaluator.cpp\
	Exception.cpp Extended_Poll.cpp L_Curve.cpp LH_Search.cpp Mads.cpp\
	SMesh.cpp XMesh.cpp Model_Sorted_Point.cpp Model_Stats.cpp Multi_Obj_Evaluator.cpp\
	Parameter_Entries.cpp Parameter_Entry.cpp Parameters.cpp\
	Pareto_Front.cpp Pareto_Point.cpp Phase_One_Evaluator.cpp\
	Phase_One_Search.cpp Point.cpp Priority_Eval_Point.cpp Quad_Model.cpp\
	Quad_Model_Evaluator.cpp Quad_Model_Search.cpp Random_Pickup.cpp\
	RNG.cpp Signature.cpp Slave.cpp Speculative_Search.cpp Stats.cpp\
	utils.cpp Variable_Group.cpp VNS_Search.cpp OrthogonalMesh.cpp \
	GMesh.cpp Sgtelib_Model_Evaluator.cpp Sgtelib_Model_Manager.cpp \
	Sgtelib_Model_Search.cpp

pkginclude_HEADERS = Cache_File_Point.hpp Cache.hpp Cache_Point.hpp\
	Cache_Search.hpp Clock.hpp defines.hpp Direction.hpp Directions.hpp\
	Display.hpp Double.hpp Eval_Point.hpp Evaluator_Control.hpp\
	Evaluator.hpp Exception.hpp Extended_Poll.hpp Filter_Point.hpp\
	L_Curve.hpp LH_Search.hpp Mads.hpp SMesh.hpp XMesh.hpp Model_Sorted_Point.hpp\
	Model_Stats.hpp Multi_Obj_Evaluator.hpp\
	Multi_Obj_Quad_Model_Evaluator.hpp nomad.hpp Parameter_Entries.hpp\
	Parameter_Entry.hpp Parameters.hpp Pareto_Front.hpp Pareto_Point.hpp\
	Phase_One_Evaluator.hpp Phase_One_Search.hpp Point.hpp\
	Priority_Eval_Point.hpp Quad_Model_Evaluator.hpp Quad_Model.hpp\
	Quad_Model_Search.hpp Random_Pickup.hpp RNG.hpp Search.hpp\
	Set_Element.hpp Signature_Element.hpp Signature.hpp\
	Single_Obj_Quad_Model_Evaluator.hpp Slave.hpp Speculative_Search.hpp\
	Stats.hpp Uncopyable.hpp utils.hpp Variable_Group.hpp\
	VNS_Search.hpp Barrier.hpp OrthogonalMesh.hpp \
	GMesh.hpp Sgtelib_Model_Evaluator.hpp Sgtelib_Model_Manager.hpp \
	Sgtelib_Model_Search.hpp

bin_PROGRAMS = nomad
nomad_SOURCES = nomad.cpp
nomad_LDADD = libnomad.a

pkgconfigdir = $(libdir)/pkgconfig
nodist_pkgconfig_DATA = ../nomad.pc
nomad.pc: ../nomad.pc.in

if MPI_ENABLED
lib_LIBRARIES += libnomadmpi.a
libnomadmpi_a_CXXFLAGS = -DUSE_MPI $(MPI_LDFLAGS) $(MPI_CXXFLAGS) $(AM_CXXFLAGS)
nodist_pkgconfig_DATA += ../nomadmpi.pc
nomadmpi.pc: ../nomadmpi.pc.in
bin_PROGRAMS += nomad.mpi
nomad_mpi_SOURCES = nomad.cpp
nomad_mpi_LDADD = libnomadmpi.a
nomad_mpi_CXXFLAGS = -DUSE_MPI $(MPI_CXXFLAGS) $(AM_CXXFLAGS)
nomad_mpi_LDFLAGS = $(MPI_CXXLDFLAGS) $(AM_CXXLDFLAGS)
endif
