#include <stdlib.h>
#include <stdio.h>
#include "tape.h"

int main()
{
    int byte_length = 2;
    tape *t = malloc_tape(byte_length);
    if (t == NULL)
    {
        fprintf(stderr, "Error: malloc_tape failed\n");
        free_tape(t);
        return 1;
    }

    print_tape(t);

    int bit_index = 0;
    for (int i = 0; i < byte_length * 8; i++)
    {
        set_by_bit_index(t, bit_index, 1);
        bit_index++;
        print_tape(t);
    }

    free_tape(t);
    return 0;
}