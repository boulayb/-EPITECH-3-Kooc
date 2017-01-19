/*
** test_poly.h for Kooc in /home/zordan_n/Kooc/test/part3
**
** Made by Nicolas Zordan
** Login   <zordan_n@epitech.net>
**
** Started on  Wed Oct 19 14:46:33 2016 Nicolas Zordan
** Last update Thu Oct 20 18:39:44 2016 Nicolas Zordan
*/

#ifndef TEST_POLY_H_
# define TEST_POLY_H_

/*  CLASS A */
typedef struct _1A_     A;

/* A MEMBER FUNCTIONS */
void                    _1A_v4init_P1A_(A *);
void                    _1A_v5print_P1A_(A *);

/* A DEFAULT FUNCTIONS */
const char              *_1A_Pc17name_of_interface_v_(void);
A                       *_1A_P1A5alloc_v_(void);
A                       *_1A_P1A3new_v_(void);
void                    _1A_v6delete_P1A_(A *);
void                    _1A_v5clean_P1A_(A *);

/* A VTABLE */
struct                  _1A_vtable_
{
  const char            *(*_Pc17name_of_interface_v_)(void);
  void                  (*_v5clean_P1A_)(A *);
  // TODO : ajouter le reste de OBJECT* (isKindOf, isTypeOf...)
  void                  (*_v5print_P1A_)(A *);
};

/* A CLASS */
struct                  __attribute__((packed)) _1A_
{
  struct _1A_vtable_    *__vtable;
  int                   _1A_i5value_;
};
/* !CLASS A */



/*  CLASS B */
typedef struct _1B_     B;

/* B MEMBER FUNCTIONS */
void                    _1B_v4init_P1B_(B *);
void                    _1B_v5print_P1B_(B *);

/* B DEFAULT FUNCTIONS */
const char              *_1B_Pc17name_of_interface_v_(void);
B                       *_1B_P1B5alloc_v_(void);
B                       *_1B_P1B3new_v_(void);
void                    _1B_v6delete_P1B_(B *);
void                    _1B_v5clean_P1B_(B *);

/* B VTABLE */
struct                  _1B_vtable_
{
  const char            *(*_Pc17name_of_interface_v_)(void);
  void                  (*_v5clean_P1B_)(B *);
  // TODO : ajouter le reste de OBJECT* (isKindOf, isTypeOf...)
  void                  (*_v5print_P1B_)(B *);
};

/* B CLASS */
struct                  __attribute__((packed)) _1B_
{
  struct _1B_vtable_    *__vtable;
  int                   _1A_i5value_;
  int                   _1B_i5value_;
};
/* !CLASS B */



/*  CLASS C */
typedef struct _1C_     C;

/* C MEMBER FUNCTIONS */
void                    _1C_v4init_P1C_(C *);
void                    _1C_v5print_P1C_(C *);

/* C DEFAULT FUNCTIONS */
const char              *_1C_Pc17name_of_interface_v_(void);
C                       *_1C_P1C5alloc_v_(void);
C                       *_1C_P1C3new_v_(void);
void                    _1C_v6delete_P1C_(C *);
void                    _1C_v5clean_P1C_(C *);

/* C VTABLE */
struct                  _1C_vtable_
{
  const char            *(*_Pc17name_of_interface_v_)(void);
  void                  (*_v5clean_P1C_)(C *);
  // TODO : ajouter le reste de OBJECT* (isKindOf, isTypeOf...)
  void                  (*_v5print_P1C_)(C *);
};

/* C CLASS */
struct                  __attribute__((packed)) _1C_
{
  struct _1C_vtable_    *__vtable;
  int                   _1A_i5value_;
  int                   _1B_i5value_;
  int                   _1C_i5value_;
};
/* !CLASS C */

#endif /* !TEST_POLY_H_ */
