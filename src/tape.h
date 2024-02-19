#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    int byte_length;
    u_int8_t *data;
} tape;

tape *malloc_tape(int byte_length);
void free_tape(tape *t);
void print_tape(tape *t);
void set_by_bit_index(tape *t, int bit_index, int value);
void flip_by_bit_index(tape *t, int bit_index);
