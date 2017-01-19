#include <stdlib.h>
#include <stdio.h>
#include "Test.h"
double _4Test_d1a;
float _4Test_f1a = 4.2;
void *_4Test_Pv1a = NULL;
void _4Test_v1f_v(void)
{
    printf("coucou la moulinette\n");
}
int _4Test_i1f_i(int nb)
{
    if (printf("NB = %d\n", nb))
        return (false);
    return (true);
}
int _4Test_i1f_ff(float nb1, float nb2)
{
    return ((int) (nb1 + nb2));
}
int _4Toto_i1a = 21;
