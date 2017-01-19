/*
** Stack.h for Babel in /home/zordan_n
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Tue Oct 18 20:51:15 2016 Nicolas Zordan
** Last update Wed Oct 19 13:48:10 2016 Nicolas Zordan
*/

#ifndef STACK_H_
# define STACK_H_

typedef struct _5Stack_ Stack;

void                    _5Stack_v4init_P5Stacki_(Stack *, int);
int                     _5Stack_i6nbitem_P5Stack_(Stack *);

/*  STACK OBJECTYPE */
const char              *_5Stack_Pc17name_of_interface_v_(void);
Stack                   *_5Stack_P5Stack5alloc_v_(void);
Stack                   *_5Stack_P5Stack3new_v_(void);
void                    _5Stack_v4init_P5Stack_(Stack *);
void                    _5Stack_v6delete_P5Stack_(Stack *);
void                    _5Stack_v5clean_P5Stack_(Stack *);
/* !STACK OBJECTYPE */

struct                  _5Stack_vtable_
{
  const char            *(*_Pc17name_of_interface_v_)(void);
  // TODO : ajouter le reste de OBJECT* (isKinfOf, isTypeOf....)
};

struct                  __attribute__((packed)) _5Stack_
{
  void                  *__vtable;
  int                   _5Stack_i4size_;
  int                   _5Stack_i6nbitem_;
};

extern int              _5Stack_i7nbstack_;

#endif /* !STACK_H_ */
