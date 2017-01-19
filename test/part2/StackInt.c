/*
** StackInt.c for  in /home/zordan_n/Kooc/test
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Wed Oct 12 19:05:17 2016 Nicolas Zordan
** Last update Mon Oct 17 13:44:36 2016 Nicolas Zordan
*/

#include <stdlib.h>
#include "StackInt.h"

int             _8StackInt_i6nbStack_;

void            _8StackInt_v4init_P8StackInti(StackInt *__self, int size)
{
  int           *buf;

  __self->_8StackInt_i6nbitem_ = 0;
  __self->_8StackInt_i4size_ = size;
  buf = (int *)calloc(size, sizeof(int));
  __self->_8StackInt_Pi4data_ = buf;
}

void            _8StackInt_v4init_P8StackInt(StackInt *__self)
{
  int           *buf;

  __self->_8StackInt_i6nbitem_ = 0;
  __self->_8StackInt_i4size_ = 2048;
  buf = (int *)calloc(2048, sizeof(int));
  __self->_8StackInt_Pi4data_ = buf;
}

void            _8StackInt_v5clean_P8StackInt(StackInt *__self)
{
  int           *buf;

  buf = __self->_8StackInt_Pi4data_;
  free(buf);
}

int             _8StackInt_i6nbitem_P8StackInt(StackInt *__self)
{
  int           n;

  n = __self->_8StackInt_i6nbitem_;
  return (n);
}

void            _8StackInt_v4push_P8StackInti(StackInt *__self, int i)
{
  int           pos;
  int           *buf;

  pos = __self->_8StackInt_i6nbitem_;
  buf = __self->_8StackInt_Pi4data_;
  buf[pos++] = i;
  __self->_8StackInt_i6nbitem_ = pos;
}

int             _8StackInt_i3pop_P8StackInt(StackInt *__self)
{
  int           *buf;
  int           pos;
  int           r;

  pos = __self->_8StackInt_i6nbitem_;
  buf = __self->_8StackInt_Pi4data_;
  r = buf[--pos];
  __self->_8StackInt_i6nbitem_ = pos;
  return (r);
}

StackInt			*_8StackInt_alloc()
{
  return (malloc(sizeof(StackInt)));
}

void				_8StackInt_delete(StackInt *__self)
{
  _8StackInt_v5clean_P8StackInt(__self);
  free(__self);
}

StackInt			*_8StackInt_new_v4init_P8StackInti(int size)
{
  StackInt                      *__elem;

  __elem = _8StackInt_alloc();
  _8StackInt_v4init_P8StackInti(__elem, size);
  return (__elem);
}

StackInt			*_8StackInt_new_v4init_P8StackInt()
{
  StackInt                      *__elem;

  __elem = _8StackInt_alloc();
  _8StackInt_v4init_P8StackInt(__elem);
  return (__elem);
}
