/*
** main.c for  in /home/zordan_n/Kooc/test/part2
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Thu Oct 13 11:33:35 2016 Nicolas Zordan
** Last update Mon Oct 17 13:43:31 2016 Nicolas Zordan
*/

#include <stdio.h>
#include "StackInt.h"

int             main(int ac, char **av)
{
  StackInt      *my_stack;

  my_stack = _8StackInt_new_v4init_P8StackInti(4242);
  _8StackInt_v4push_P8StackInti(my_stack, 10);
  _8StackInt_v4push_P8StackInti(my_stack, 11);
  _8StackInt_v4push_P8StackInti(my_stack, 12);
  _8StackInt_v4push_P8StackInti(my_stack, 14);
  while (_8StackInt_i6nbitem_P8StackInt(my_stack) > 0) {
    printf("Elem remaining = %d\n", _8StackInt_i6nbitem_P8StackInt(my_stack));
    printf("Poped = %d\n\n", _8StackInt_i3pop_P8StackInt(my_stack));
  }
  _8StackInt_delete(my_stack);
  StackInt      local_stack;
  _8StackInt_v4init_P8StackInti(&local_stack, 4242);
  _8StackInt_v4push_P8StackInti(&local_stack, 33);
  _8StackInt_v5clean_P8StackInt(&local_stack);
  return (0);
}
