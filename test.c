#include <stdio.h>
#include <string.h>

struct TestStruct
{
    int num;
    char data[10];
};

void test(struct TestStruct * test)
{
    test->num = 2;
    strcpy(test->data, "testdata");
    printf("from c: %s\n",test->data);
}
