all: $(patsubst %.py,%.json,$(wildcard *.py))

%.json: %.py
	python $<

test:
	python -m unittest discover --catch --verbose --start-directory 'tests' --pattern 'test_*.py'

check:
	python -m unittest discover --catch --verbose --start-directory 'tests' --pattern 'check_*.py'

clean:
	rm -f *.pyc
	rm -f ./tests/*.pyc
	rm -f ./submission/*.png
	rm -f ./submission/*.json

.PHONY: test clean all
