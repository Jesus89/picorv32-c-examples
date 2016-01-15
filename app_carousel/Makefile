
ifeq ($(shell which icoprog),)
SSH_RASPI := ssh pi@raspi
else
SSH_RASPI := sh -c
endif

all: appimage.hex

32x32png.h: 32x32png.py
	python 32x32png.py > 32x32png.h

appimage.elf: main.c 32x32png.h
	riscv32-unknown-elf-gcc --std=gnu99 -Os -m32 -o appimage.elf main.c
	chmod -x appimage.elf

appimage.hex: appimage.elf
	riscv32-unknown-elf-objcopy -O verilog appimage.elf appimage.hex
	chmod -x appimage.hex

run: appimage.hex
	$(SSH_RASPI) 'icoprog -b'
	$(SSH_RASPI) 'icoprog -zc2' < appimage.hex

.PHONY: all run
