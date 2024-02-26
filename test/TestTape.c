#include "unity.h"
#include "tape.h"

void test_malloc_free_tape()
{
    int byte_length = 2;
    tape *t = malloc_tape(byte_length);
    TEST_ASSERT_NOT_NULL(t);
    TEST_ASSERT_EQUAL(2, t->byte_length);
    TEST_ASSERT_NOT_NULL(t->data);
    TEST_ASSERT_EQUAL(0, t->bit_pointer);
    free_tape(t);
}

void setUp()
{
}

void tearDown()
{
}

int main(void)
{
    UNITY_BEGIN();

    RUN_TEST(test_malloc_free_tape);

    UNITY_END();

    return 0;
}