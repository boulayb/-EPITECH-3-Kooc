/*
** StackInt.c for  in /home/zordan_n
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Wed Oct 19 03:22:07 2016 Nicolas Zordan
** Last update Wed Oct 19 14:07:24 2016 Nicolas Zordan
*/

#include <stdlib.h>
#include "StackInt.h"

int                         _8StackInt_i7nbstack_ = 0;
struct _8StackInt_vtable_   _8StackInt_vtable_ = {_8StackInt_Pc17name_of_interface_v_};

void                        _8StackInt_v4init_P8StackInti_(StackInt *__self, int size)
{
  int                       *buf;

  ((Stack *)__self)->__vtable = &_8StackInt_vtable_;
  _5Stack_v4init_P5Stacki_((Stack *)__self, size);
  buf = (int *)calloc(size, sizeof(int));
  __self->_8StackInt_Pi4data_ = buf;
}

void                        _8StackInt_v4push_P8StackInti_(StackInt *__self, int i)
{
  int                       pos;
  int                       *buf;

  pos = ((Stack *)__self)->_5Stack_i6nbitem_;
  buf = __self->_8StackInt_Pi4data_;
  buf[pos++] = i;
  ((Stack *)__self)->_5Stack_i6nbitem_ = pos;
}

int                         _8StackInt_i3pop_P8StackInt_(StackInt *__self)
{
  int                       *buf;
  int                       pos;
  int                       r;

  pos = ((Stack *)__self)->_5Stack_i6nbitem_;
  buf = __self->_8StackInt_Pi4data_;
  r = buf[pos--];
  ((Stack *)__self)->_5Stack_i6nbitem_ = pos;
  return (r);
}

void                        _8StackInt_v5clean_P8StackInt_(StackInt *__self)
{
  int                       *buf;

  buf = __self->_8StackInt_Pi4data_;
  free(buf);
  _5Stack_v5clean_P5Stack_((Stack *)__self);
}

/*  STACKINT OBJECTYPE */
const char                  *_8StackInt_Pc17name_of_interface_v_(void)
{
  return ("StackInt");
}

StackInt                    *_8StackInt_P8StackInt5alloc_v_(void)
{
  return (malloc(sizeof(StackInt)));
}

StackInt                    *_8StackInt_P8StackInt3new_v_(void)
{
  StackInt                  *res;

  res = _8StackInt_P8StackInt5alloc_v_();
  _8StackInt_v4init_P8StackInt_(res);
  return (res);
}

void                        _8StackInt_v4init_P8StackInt_(StackInt *__self)
{
  ((Stack *)__self)->__vtable = &_8StackInt_vtable_;
}

void                        _8StackInt_v6delete_P8StackInt_(StackInt *__self)
{
  _8StackInt_v5clean_P8StackInt_(__self);
  _5Stack_v5clean_P5Stack_((Stack *)__self);
  free(__self);
}
/* !STACKINT OBJECTYPE */
