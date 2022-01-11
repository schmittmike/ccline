TARGET=ccline
OBJS=cline.o
CFLAGS=-Wall

all: ${TARGET}

${TARGET}: ${OBJS}
	gcc -o ${TARGET} ${OBJS}
