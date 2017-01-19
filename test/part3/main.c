/*
** main.c for  in /home/zordan_n/Kooc/test/part2
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Thu Oct 13 11:33:35 2016 Nicolas Zordan
** Last update Wed Oct 19 15:52:47 2016 Nicolas Zordan
*/

#include "test_poly.h"

int             main(int ac, char **av)
{
  A             *a;

  a = _1A_P1A3new_v_();
  ((struct _1A_vtable_ *)(a->__vtable))->_v5print_P1A_(a);
  a = (A *)_1B_P1B3new_v_();
  ((struct _1A_vtable_ *)(a->__vtable))->_v5print_P1A_(a);
  a = (A *)_1C_P1C3new_v_();
  ((struct _1A_vtable_ *)(a->__vtable))->_v5print_P1A_(a);
  _1A_v5print_P1A_(a);
  return (0);
}
