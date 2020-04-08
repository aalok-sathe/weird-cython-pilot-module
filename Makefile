
build: FORCE
	python3 setup.py build_ext --inplace

clean:
	python3 setup.py clean
	
cleanall: clean
	rm -rf **/*.so *.so **/*.cpp *.cpp **/__pycache__ build

FORCE:
