/*
 * hotspot.c: a small program for practising the measure-first routine.
 *
 * It fills a 4096 x 4096 grid of whole numbers (128 MiB), then sums it two
 * ways, several times over. With the default scale, reordering the loops or
 * switching between -O0, -O2 and -O3 should not change the printed sums. If
 * they change, something is wrong.
 *
 * noinline keeps each function separate in the compiled program, so a
 * profiler can report time for each one. Without it, GCC at -O2 may merge
 * them all into main.
 *
 * Usage: ./hotspot [repeats] [scale]   (defaults: 10 and 0.5)
 */
#include <stdio.h>
#include <stdlib.h>

#define N 4096

static double grid[N][N];

__attribute__((noinline)) static void fill_grid(void)
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            grid[i][j] = (double)((i * 31 + j * 17) % 100);
}

/* Adds every value in the grid, visiting it one column at a time. */
__attribute__((noinline)) static double column_sum(void)
{
    double total = 0.0;
    for (int j = 0; j < N; j++)
        for (int i = 0; i < N; i++)
            total += grid[i][j];
    return total;
}

/* Adds every value divided by scale, visiting the grid one row at a time. */
__attribute__((noinline)) static double scaled_sum(double scale)
{
    double total = 0.0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            total += grid[i][j] / scale;
    return total;
}

int main(int argc, char **argv)
{
    int repeats = argc > 1 ? atoi(argv[1]) : 10;
    double scale = argc > 2 ? atof(argv[2]) : 0.5;
    if (repeats < 1 || scale == 0.0) {
        fprintf(stderr, "usage: %s [repeats >= 1] [non-zero scale]\n", argv[0]);
        return 1;
    }

    fill_grid();

    double columns = 0.0, scaled = 0.0;
    for (int r = 0; r < repeats; r++) {
        columns += column_sum();
        scaled += scaled_sum(scale);
        grid[r % N][0] += 1.0; /* change the data so each repeat does real work */
    }

    printf("column_sum total: %.1f\n", columns);
    printf("scaled_sum total: %.1f\n", scaled);
    return 0;
}
