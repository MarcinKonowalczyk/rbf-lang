PROJ_NAME=rbfnet

SRCS=$(wildcard src/*.c)
OBJS=$(patsubst src/%.c, build/%.o, $(SRCS))

# create build directory if it doesn't exist
$(shell mkdir -p build)

CC=gcc
CFLAGS=-c -Wall -Werror -std=c99

BIN_NAME=build/$(PROJ_NAME)

all: $(BIN_NAME)

$(BIN_NAME): $(OBJS)
	$(CC) $(OBJS) -o $(BIN_NAME)

build/%.o: src/%.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJS) $(BIN_NAME)
