#include <stdio.h>
#include <string.h>

struct TestStruct
{
    char a;
    short b;
    int c;
    int num;
    char data[10];
};

#define OFFSET(p, mem)  (int)(((char*)&(p->mem) - (char*)p))

void test(struct TestStruct * test)
{
    printf("offset a = %d\n", OFFSET(test, a));
    printf("offset b = %d\n", OFFSET(test, b));
    printf("offset c = %d\n", OFFSET(test, c));
    printf("offset num = %d\n", OFFSET(test, num));

    test->a = 1;
    test->b = 2;
    test->c = 3;
    test->num = 2;
    strcpy(test->data, "testdata");
    printf("from c: %s\n",test->data);
}
