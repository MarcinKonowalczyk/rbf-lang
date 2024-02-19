#include <stdlib.h>
#include <stdio.h>
#include "tape.h"

tape *malloc_tape(int byte_length)
{
    // Allocate memory for the tape
    tape *t = (tape *)malloc(sizeof(tape));
    if (t == NULL)
    {
        // malloc failed
        return NULL;
    }

    t->byte_length = byte_length;
    t->data = (u_int8_t *)malloc(byte_length);
    if (t->data == NULL)
    {
        // malloc failed
        free(t);
        return NULL;
    }

    t->bit_pointer = 0;

    return t;
}

void free_tape(tape *t)
{
    free(t->data);
    free(t);
}

void print_bit_pointer(tape *t)
{
    // print an empty line with the bit pointer
    for (int i = 0; i < t->bit_pointer; i++)
    {
        printf(".");
    }
    printf("^");
    int remaining = t->byte_length * 8 - t->bit_pointer - 1;
    for (int i = 0; i < remaining; i++)
    {
        printf(".");
    }
    printf("\n");
}

void print_tape(tape *t)
{
    // print each bit of each byte
    for (int i = 0; i < t->byte_length; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            printf("%d", (t->data[i] >> j) & 1);
        }
        printf("");
    }
    printf("\n");
}

void set_by_bit_index(tape *t, int bit_index, int value)
{
    int byte_index = bit_index / 8;
    int bit_offset = bit_index % 8;
    uint8_t mask = 1 << bit_offset;
    t->data[byte_index] |= value ? mask : ~mask;
}

void flip_by_bit_index(tape *t, int bit_index)
{
    int byte_index = bit_index / 8;
    int bit_offset = bit_index % 8;
    uint8_t mask = 1 << bit_offset;
    t->data[byte_index] ^= mask;
}

void set_pointer_to_bit_index(tape *t, int bit_index)
{
    t->bit_pointer = bit_index;
}

void move_pointer(tape *t, int offset)
{
    long temp_pointer = t->bit_pointer + offset; // temp signed pointer
    while (temp_pointer < 0)
    {
        temp_pointer += t->byte_length * 8;
    }
    while (temp_pointer >= t->byte_length * 8)
    {
        temp_pointer -= t->byte_length * 8;
    }
    t->bit_pointer = temp_pointer;
}