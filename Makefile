UI_FILES = $(wildcard qt/*.ui)
PY_FILES = $(patsubst qt/%.ui, view/ui_%.py, $(UI_FILES))

all : $(PY_FILES)

view/ui_%.py : qt/%.ui
	python3 -m PyQt5.uic.pyuic $< -o $@
