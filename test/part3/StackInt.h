/*
** StackInt.h for  in /home/zordan_n/Kooc/test/part3
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Wed Oct 19 00:59:25 2016 Nicolas Zordan
** Last update Thu Oct 20 21:46:56 2016 alice
*/

#ifndef STACKINT_H_
# define STACKINT_H_

# include "Stack.h"

typedef struct _8StackInt_  StackInt;

void                        _8StackInt_v4init_P8StackInti_(StackInt *, int);
void                        _8StackInt_v5clean_P8StackInt_(StackInt *);

void                        _8StackInt_v4push_P8StackInti_(StackInt *, int);
int                         _8StackInt_i3pop_P8StackInt_(StackInt *);

/*  STACKINT OBJECTYPE */
const char                  *_8StackInt_Pc17name_of_interface_v_(void);
StackInt                    *_8StackInt_P8StackInt5alloc_v_(void);
StackInt                    *_8StackInt_P8StackInt3new_v_(void);
void                        _8StackInt_v4init_P8StackInt_(StackInt *);
void                        _8StackInt_v6delete_P8StackInt_(StackInt *);
/* !STACKINT OBJECTYPE */

struct                      _8StackInt_vtable_
{
  const char                *(*_Pc17name_of_interface_v_)(void);
  // TODO : ajouter le reste de OBJECT* (isKindOf, isTypeOf...)
};

struct                      __attribute__((packed)) _8StackInt_
{
  Stack                     __parent;
  int                       *_8StackInt_Pi4data_;
};

extern int                  _8StackInt_i7nbstack_;

#endif /* !STACKINT_H_ */
