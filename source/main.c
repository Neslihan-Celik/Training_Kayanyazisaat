#include <stdio.h>
#include "gpio_if.h"

int main(void)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    gpio_init();
    printf("End Of Main\n");
    return 0;
}
