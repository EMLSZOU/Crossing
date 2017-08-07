#include <stdio.h>
int main(){
    printf("Fahr\t Celsius\n");
    float Fahr, Celsius;
    for(Fahr = 300; Fahr >= 0; Fahr = Fahr-20){
        Celsius = (5.0/9.0) * (Fahr-32.0);
        printf("%3.0f %9.2f\n", Fahr, Celsius);
    }
    return 0;
}