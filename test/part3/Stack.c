/*
** Stack.c for Babel in /home/zordan_n
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Tue Oct 18 21:01:15 2016 Nicolas Zordan
** Last update Wed Oct 19 13:34:24 2016 Nicolas Zordan
*/

#include <stdlib.h>
#include "Stack.h"

int                     _5Stack_i7nbstack_ = 0;
struct _5Stack_vtable_  _5Stack_vtable_ = {_5Stack_Pc17name_of_interface_v_};

void                    _5Stack_v4init_P5Stacki_(Stack *__self, int size)
{
  __self->__vtable = &_5Stack_vtable_;
  __self->_5Stack_i4size_ = size;
}

int                     _5Stack_i6nbitem_P5Stack_(Stack *__self)
{
  int                   n;

  n = __self->_5Stack_i6nbitem_;
  return (n);
}

/*  STACK OBJECTYPE */
const char              *_5Stack_Pc17name_of_interface_v_(void)
{
  return ("Stack");
}

Stack                   *_5Stack_P5Stack5alloc_v_(void)
{
  return (malloc(sizeof(Stack)));
}

Stack                   *_5Stack_P5Stack3new_v_(void)
{
  Stack                 *res;

  res = _5Stack_P5Stack5alloc_v_();
  _5Stack_v4init_P5Stack_(res);
  return (res);
}

void                    _5Stack_v4init_P5Stack_(Stack *__self)
{
  __self->__vtable = &_5Stack_vtable_;
}

void                    _5Stack_v6delete_P5Stack_(Stack *__self)
{
  _5Stack_v5clean_P5Stack_(__self);
  free(__self);
}

void                    _5Stack_v5clean_P5Stack_(Stack *__self)
{
}
/* !STACK OBJECTYPE */
