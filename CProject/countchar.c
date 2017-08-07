#include <stdio.h>
#include <windows.h>
main(){
    int c, nc, nl, np, nt;
    nc, nl, np, nt = 0;
    for(nc = 0; (c = getchar()) != EOF; ++nc)  //Win输入Ctrl Z输入EOF，Unix是Ctrl D
        if (c == '\n')
            ++nl;
        if (c == ' ')
            ++np;
        if (c == '\t')
            ++nt;
    printf("%d %d %d %d\n",nc, nl, np, nt);
    system("pause");
}
