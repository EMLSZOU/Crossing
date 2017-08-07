#include <stdio.h>
#include <conio.h>

int main()
{
    int i, j, t, a[10] = {56, 98, 76, 69, 88, 43, 29, 74, 58, 66};
    for (i = 0; i < 9; i++)
        for (j = 0; j < 9 - i; j++)
            if (a[j] > a[j + 1])
            {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
    for (i = 0; i < 10; i++)
        printf("%d ", a[i]);
    printf("\n");
    getch();

    return 0;
}