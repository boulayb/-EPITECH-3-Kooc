/*
** test_poly.c for KOOC in /home/zordan_n/Kooc/test/part3
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Mon Oct 17 21:47:05 2016 Nicolas Zordan
** Last update Thu Oct 20 18:43:19 2016 Nicolas Zordan
*/

#include <stdio.h>
#include <stdlib.h>
#include "test_poly.h"

/* A IMPLEMENTATION */
/* A INIT */
struct _1A_vtable_      _1A_vtable_ = {_1A_Pc17name_of_interface_v_, _1A_v5clean_P1A_, _1A_v5print_P1A_};

/* A MEMBER FUNCTIONS */
void                    _1A_v4init_P1A_(A *__self)
{
  __self->_1A_i5value_ = 42;
  __self->__vtable = &_1A_vtable_;
}

void                    _1A_v5print_P1A_(A *__self)
{
  int                   value;
  const char            *name = __self->__vtable->_Pc17name_of_interface_v_();

  value = __self->_1A_i5value_;
  printf("%d %s\n", value, name);
}

/* A DEFAULT FUNCTIONS */
const char              *_1A_Pc17name_of_interface_v_(void)
{
  return ("A");
}

A                       *_1A_P1A5alloc_v_(void)
{
  return (malloc(sizeof(A)));
}

A                       *_1A_P1A3new_v_(void)
{
  A                     *res;

  res = _1A_P1A5alloc_v_();
  _1A_v4init_P1A_(res);
  return (res);
}

void                    _1A_v6delete_P1A_(A *__self)
{
  _1A_v5clean_P1A_(__self);
  free(__self);
}

void                    _1A_v5clean_P1A_(A *__self)
{
  _1A_v5clean_P1A_((A *)__self);
}
/* !A IMPLEMENTATION */


/* B IMPLEMENTATION */
/* B INIT */
struct _1B_vtable_      _1B_vtable_ = {_1B_Pc17name_of_interface_v_, _1B_v5clean_P1B_, _1B_v5print_P1B_};

/* B MEMBER FUNCTIONS */
void                    _1B_v4init_P1B_(B *__self)
{
  _1A_v4init_P1A_((A *)__self);
  __self->_1B_i5value_ = 124;
  __self->__vtable = &_1B_vtable_;
}

void                    _1B_v5print_P1B_(B *__self)
{
  int                   value;
  const char            *name = __self->__vtable->_Pc17name_of_interface_v_();

  value = __self->_1B_i5value_;
  printf("%d %s\n", value, name);
}

/* B DEFAULT FUNCTIONS */
const char              *_1B_Pc17name_of_interface_v_(void)
{
  return ("B");
}

B                       *_1B_P1B5alloc_v_(void)
{
  return (malloc(sizeof(B)));
}

B                       *_1B_P1B3new_v_(void)
{
  B                     *res;

  res = _1B_P1B5alloc_v_();
  _1B_v4init_P1B_(res);
  return (res);
}

void                    _1B_v6delete_P1B_(B *__self)
{
  _1B_v5clean_P1B_(__self);
  free(__self);
}

void                    _1B_v5clean_P1B_(B *__self)
{
}
/* !B IMPLEMENTATION */

/* C IMPLEMENTATION */
/* C INIT */
struct _1C_vtable_      _1C_vtable_ = {_1C_Pc17name_of_interface_v_, _1C_v5clean_P1C_, _1C_v5print_P1C_};

/* C MEMBER FUNCTIONS */
void                    _1C_v4init_P1C_(C *__self)
{
  _1B_v4init_P1B_((B *)__self);
  __self->_1C_i5value_ = 666;
  __self->__vtable = &_1C_vtable_;
}

void                    _1C_v5print_P1C_(C *__self)
{
  int                   value;
  const char            *name = __self->__vtable->_Pc17name_of_interface_v_();

  value = __self->_1C_i5value_;
  printf("%d %s\n", value, name);
}

/* C DEFAULT FUNCTIONS */
const char              *_1C_Pc17name_of_interface_v_(void)
{
  return ("C");
}

C                       *_1C_P1C5alloc_v_(void)
{
  return (malloc(sizeof(C)));
}

C                       *_1C_P1C3new_v_(void)
{
  C                     *res;

  res = _1C_P1C5alloc_v_();
  _1C_v4init_P1C_(res);
  return (res);
}

void                    _1C_v6delete_P1C_(C *__self)
{
  _1C_v5clean_P1C_(__self);
  free(__self);
}

void                    _1C_v5clean_P1C_(C *__self)
{
  _1B_v5clean_P1B_((B *)__self);
}
/* !C IMPLEMENTATION */
