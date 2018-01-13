
## compiler
CC=g++
CFLAGS=-pthread -std=c++11

TARGETS=hamburger_joint

## INC indicates the header file path
INC=-I ./
## source files
SRCS=hamburger.cpp\
	 joint.cpp
OBJS=$(SRCS:.cpp=.o)

## compile CMD
%.o:%.cpp ./*.h
	$(CC) $(INC) $(CFLAGS) -o $@ -c $<

## link CMD and some others
$(TARGETS):$(OBJS)
	$(CC) -o $(TARGETS) $(OBJS) 
#$(CC) -o $@ $^


.PHONY: list
list:
	echo $(TARGETS)

.PHONY: clean
clean:
	rm -rf $(TARGETS) $(OBJS)
