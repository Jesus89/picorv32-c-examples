#include <stdlib.h>
#include <stdint.h>
#include "32x32png.h"

static inline void setled(int v)
{
	*(volatile uint32_t*)0x20000000 = v;
}

void set_pixel(int x, int y, uint8_t r, uint8_t g, uint8_t b)
{
	if (0 <= x && x < 32 && 0 <= y && y < 32)
	{
		uint32_t rgb = (r << 16) | (g << 8) | b;
		uint32_t addr = 4*x + 128*y + 0x10000000;
		*(volatile uint32_t*)addr = rgb;
	}
}

/* main program */

void main()
{
	int i, j, n = 0;

	while(1)
	{
		for (i = 0; i < 32; i++)
		for (j = 0; j < 32; j++)
			set_pixel(i, j, r[n][j][i], g[n][j][i], b[n][j][i]);

		for (i = 0; i < 3*350000; i++)
			asm volatile ("");

		n = (n + 1) % num;
	}
}
