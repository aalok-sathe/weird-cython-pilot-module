
build: FORCE
	python3 setup.py build_ext --inplace

clean:
	python3 setup.py clean
	
cleanall: clean
	rm -f **/*.so *.so 

FORCE:
