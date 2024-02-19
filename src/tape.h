#ifndef TAPE_H
#define TAPE_H

#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    int byte_length;
    u_int8_t *data;
    size_t bit_pointer;
} tape;

tape *malloc_tape(int byte_length);
void free_tape(tape *t);
void print_bit_pointer(tape *t);
void print_tape(tape *t);
void set_bit_by_bit_index(tape *t, int bit_index, int value);
void flip_bit_by_bit_index(tape *t, int bit_index);

void set_pointer_to_bit_index(tape *t, int bit_index);
void move_pointer(tape *t, int offset);

#endif /* TAPE_H */