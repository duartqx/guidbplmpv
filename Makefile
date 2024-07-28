TARGET=a.out
CXX=g++ -std=c++17
DEBUG=-g
OPT=-O0
WARN=-Wall
SDL2=`pkg-config --cflags --libs sdl2`
INCSDL2=-I /usr/include/SDL2
CXXFLAGS=$(DEBUG) $(OPT) $(WARN) $(SDL2)
LD=g++
OBJS= main.o imgui.o imgui_draw.o imgui_impl_glfw.o imgui_impl_opengl3.o imgui_tables.o imgui_widgets.o
all: $(OBJS)
	$(LD) -I imgui -o $(TARGET) $(OBJS) -lglfw -lGL $(CXXFLAGS)
	@rm *.o
	@./$(TARGET)

main.o: main.cpp
	$(CXX) -c $(CXXFLAGS) main.cpp -o main.o

imgui.o: imgui/imgui.cpp
	$(CXX) -c $(DEBUG) $(OPT) imgui/imgui.cpp -o imgui.o

imgui_draw.o: imgui/imgui_draw.cpp
	$(CXX) -c $(DEBUG) $(OPT) imgui/imgui_draw.cpp -o imgui_draw.o

imgui_impl_glfw.o: imgui/imgui_impl_glfw.cpp
	$(CXX) $(INCSDL2) -c $(DEBUG) $(OPT) imgui/imgui_impl_glfw.cpp -o imgui_impl_glfw.o

imgui_impl_opengl3.o: imgui/imgui_impl_opengl3.cpp
	$(CXX) $(INCSDL2) -c $(DEBUG) $(OPT) imgui/imgui_impl_opengl3.cpp -o imgui_impl_opengl3.o

imgui_tables.o: imgui/imgui_tables.cpp
	$(CXX) -c $(DEBUG) $(OPT) imgui/imgui_tables.cpp -o imgui_tables.o

imgui_widgets.o: imgui/imgui_widgets.cpp
	$(CXX) -c $(DEBUG) $(OPT) imgui/imgui_widgets.cpp -o imgui_widgets.o
