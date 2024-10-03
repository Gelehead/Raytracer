cmake_minimum_required(VERSION 3.5.0)
project(graphic_thing VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

project("image_tester")
add_executable("image_tester" "simple_image_output.cpp" )

project("graphic_thing")
add_executable("graphic_thing" "main.cpp" "color.h" "ray.h" "vec3.h")

set_property(TARGET graphic_thing PROPERTY CXX_STANDARD 17)
