# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build

# Include any dependencies generated for this target.
include src/opencv/CMakeFiles/box_test.dir/depend.make

# Include the progress variables for this target.
include src/opencv/CMakeFiles/box_test.dir/progress.make

# Include the compile flags for this target's objects.
include src/opencv/CMakeFiles/box_test.dir/flags.make

src/opencv/CMakeFiles/box_test.dir/box_test.cpp.o: src/opencv/CMakeFiles/box_test.dir/flags.make
src/opencv/CMakeFiles/box_test.dir/box_test.cpp.o: ../src/opencv/box_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/opencv/CMakeFiles/box_test.dir/box_test.cpp.o"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/box_test.dir/box_test.cpp.o -c /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv/box_test.cpp

src/opencv/CMakeFiles/box_test.dir/box_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/box_test.dir/box_test.cpp.i"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv/box_test.cpp > CMakeFiles/box_test.dir/box_test.cpp.i

src/opencv/CMakeFiles/box_test.dir/box_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/box_test.dir/box_test.cpp.s"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv/box_test.cpp -o CMakeFiles/box_test.dir/box_test.cpp.s

# Object files for target box_test
box_test_OBJECTS = \
"CMakeFiles/box_test.dir/box_test.cpp.o"

# External object files for target box_test
box_test_EXTERNAL_OBJECTS =

bin/box_test: src/opencv/CMakeFiles/box_test.dir/box_test.cpp.o
bin/box_test: src/opencv/CMakeFiles/box_test.dir/build.make
bin/box_test: lib/libapriltag_opencv.so
bin/box_test: lib/libapriltag.so
bin/box_test: src/opencv/CMakeFiles/box_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/box_test"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/box_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/opencv/CMakeFiles/box_test.dir/build: bin/box_test

.PHONY : src/opencv/CMakeFiles/box_test.dir/build

src/opencv/CMakeFiles/box_test.dir/clean:
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && $(CMAKE_COMMAND) -P CMakeFiles/box_test.dir/cmake_clean.cmake
.PHONY : src/opencv/CMakeFiles/box_test.dir/clean

src/opencv/CMakeFiles/box_test.dir/depend:
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv/CMakeFiles/box_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/opencv/CMakeFiles/box_test.dir/depend

