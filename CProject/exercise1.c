#include <stdio.h>
main (){
    printf("celsius fahr\n");
    float fahr, celsius;
    int lower, upper, step;
    lower = -50;
    upper = 50;
    step = 20;
    celsius = lower;
    while(celsius <= upper){
        fahr = (9.0/5.0)*celsius+32;
        printf("%5.0f  %6.1f\n",celsius,fahr); //%6.2f按照小数打印，至少6位长度，小数点后两位。%o八进制数，%x十六进制数，%c字符，%s字符串，%%是百分号本身
        celsius = celsius + step;
    }
}