TARGETS= hamburger_joint
BUILD_CMD= g++ -o $(TARGETS) -pthread -std=c++11 

$(TARGETS):joint.cpp hamburger.cpp
	$(BUILD_CMD) *.cpp
	
#hamburger.o: 
#	$(BUILD_CMD) hamburger.cpp factory_base.h

#joint.o: 
#	$(BUILD_CMD) joint.cpp factory_base.h



.PHONY: list
list:
	echo $(TARGETS)

.PHONY: clean
clean:
	rm *.o $(TARGETS)
