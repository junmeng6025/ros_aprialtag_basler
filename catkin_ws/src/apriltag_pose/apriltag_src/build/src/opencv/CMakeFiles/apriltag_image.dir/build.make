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
include src/opencv/CMakeFiles/apriltag_image.dir/depend.make

# Include the progress variables for this target.
include src/opencv/CMakeFiles/apriltag_image.dir/progress.make

# Include the compile flags for this target's objects.
include src/opencv/CMakeFiles/apriltag_image.dir/flags.make

src/opencv/CMakeFiles/apriltag_image.dir/apriltag_image.cpp.o: src/opencv/CMakeFiles/apriltag_image.dir/flags.make
src/opencv/CMakeFiles/apriltag_image.dir/apriltag_image.cpp.o: ../src/opencv/apriltag_image.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/opencv/CMakeFiles/apriltag_image.dir/apriltag_image.cpp.o"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/apriltag_image.dir/apriltag_image.cpp.o -c /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv/apriltag_image.cpp

src/opencv/CMakeFiles/apriltag_image.dir/apriltag_image.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/apriltag_image.dir/apriltag_image.cpp.i"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv/apriltag_image.cpp > CMakeFiles/apriltag_image.dir/apriltag_image.cpp.i

src/opencv/CMakeFiles/apriltag_image.dir/apriltag_image.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/apriltag_image.dir/apriltag_image.cpp.s"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv/apriltag_image.cpp -o CMakeFiles/apriltag_image.dir/apriltag_image.cpp.s

# Object files for target apriltag_image
apriltag_image_OBJECTS = \
"CMakeFiles/apriltag_image.dir/apriltag_image.cpp.o"

# External object files for target apriltag_image
apriltag_image_EXTERNAL_OBJECTS =

bin/apriltag_image: src/opencv/CMakeFiles/apriltag_image.dir/apriltag_image.cpp.o
bin/apriltag_image: src/opencv/CMakeFiles/apriltag_image.dir/build.make
bin/apriltag_image: lib/libapriltag_opencv.so
bin/apriltag_image: lib/libapriltag.so
bin/apriltag_image: src/opencv/CMakeFiles/apriltag_image.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../../bin/apriltag_image"
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/apriltag_image.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/opencv/CMakeFiles/apriltag_image.dir/build: bin/apriltag_image

.PHONY : src/opencv/CMakeFiles/apriltag_image.dir/build

src/opencv/CMakeFiles/apriltag_image.dir/clean:
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv && $(CMAKE_COMMAND) -P CMakeFiles/apriltag_image.dir/cmake_clean.cmake
.PHONY : src/opencv/CMakeFiles/apriltag_image.dir/clean

src/opencv/CMakeFiles/apriltag_image.dir/depend:
	cd /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/src/opencv /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv /home/jun/ros_apriltag_basler/catkin_ws/src/apriltag_pose/apriltag_src/build/src/opencv/CMakeFiles/apriltag_image.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/opencv/CMakeFiles/apriltag_image.dir/depend

