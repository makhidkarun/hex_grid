# Makefile

TARGETS=hex_grid.py tests/test_hex_grid.py
SETUP=./setup.py

sdist: $(TARGETS) $(SETUP)
	python $(SETUP) sdist

bdist_wheel: $(TARGETS)
	python $(SETUP) bdist_wheel --universal

twine:
	twine upload dist/*
