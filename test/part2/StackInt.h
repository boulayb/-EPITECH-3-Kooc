/*
** StackInt.h for  in /home/zordan_n/Kooc/test
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Wed Oct 12 14:00:28 2016 Nicolas Zordan
** Last update Wed Oct 19 11:10:39 2016 alice
*/

#ifndef STACKINT_H__
# define STACKINT_H__

typedef struct _8StackInt_      StackInt;

void                            _8StackInt_v4init_P8StackInti(StackInt *, int);
void                            _8StackInt_v4init_P8StackInt(StackInt *);
void                            _8StackInt_v5clean_P8StackInt(StackInt *);
int                             _8StackInt_i6nbitem_P8StackInt(StackInt *);
StackInt			*_8StackInt_P8StackInt5alloc_v(void);
void                            _8StackInt_v4push_P8StackInti(StackInt *, int);
void				_8StackInt_v6delete_P8StackInt(StackInt *);
int                             _8StackInt_i3pop_P8StackInt(StackInt *);
StackInt			*_8StackInt_new_v4init_P8StackInti(int);
StackInt			*_8StackInt_new_v4init_P8StackInt();

struct                          _8StackInt_
{
  int                           _8StackInt_i4size_;
  int                           _8StackInt_i6nbitem_;
  int                           *_8StackInt_Pi4data_;
};

extern int                      _8StackInt_i6nbStack_;

#endif /* !STACKINT_H__ */
