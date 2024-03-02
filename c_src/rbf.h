#ifndef RBF_H
#define RBF_H

#include "tape.h"

typedef enum
{
    RBF_CMD_TOGGLE = 0,
    RBF_CMD_TAPE_RIGHT = 1,
    RBF_CMD_TAPE_LEFT = 2,
    RBF_CMD_LOOP_START = 3,
    RBF_CMD_LOOP_END = 4,
} rbf_cmd_t;

#endif /* RBF_H */
