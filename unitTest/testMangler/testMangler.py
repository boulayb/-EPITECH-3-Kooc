#! /usr/bin/env python3


import sys
sys.path.append("../../")
import unittest
import kooc_mangling
from cnorm.passes import to_c
from cnorm.parsing.declaration import Declaration


class TestMangler(unittest.TestCase):

    def test_int(self):
        cparse = Declaration()
        res = cparse.parse("""
        int     i;
        """)
        kooc_mangling.mangleAttr(res.body[0], "intmod")
        self.assertEqual(str(res.to_c()), "int _6intmod_i1i;\n")

    def test_long(self):
        cparse = Declaration()
        res = cparse.parse("""
        long     lvar;
        """)
        kooc_mangling.mangleAttr(res.body[0], "longmod")
        self.assertEqual(str(res.to_c()), "long int _7longmod_l4lvar;\n")

    def test_short(self):
        cparse = Declaration()
        res = cparse.parse("""
        short     svar;
        """)
        kooc_mangling.mangleAttr(res.body[0], "shortmod")
        self.assertEqual(str(res.to_c()), "short int _8shortmod_s4svar;\n")

    def test_longlong(self):
        cparse = Declaration()
        res = cparse.parse("""
        long long     llvar;
        """)
        kooc_mangling.mangleAttr(res.body[0], "llmod")
        self.assertEqual(str(res.to_c()), "long long int _5llmod_j5llvar;\n")

    def test_float(self):
        cparse = Declaration()
        res = cparse.parse("""
        float     fvar;
        """)
        kooc_mangling.mangleAttr(res.body[0], "fmod")
        self.assertEqual(str(res.to_c()), "float _4fmod_f4fvar;\n")

    def test_double(self):
        cparse = Declaration()
        res = cparse.parse("""
        double     dvar;
        """)
        kooc_mangling.mangleAttr(res.body[0], "dmod")
        self.assertEqual(str(res.to_c()), "double _4dmod_d4dvar;\n")

    def test_uint(self):
        cparse = Declaration()
        res = cparse.parse("""
        unsigned int     uivar;
        """)
        kooc_mangling.mangleAttr(res.body[0], "uimod")
        self.assertEqual(str(res.to_c()), "unsigned int _5uimod_I5uivar;\n")

    def test_char_star(self):
        cparse = Declaration()
        res = cparse.parse("""
        char    *str;
        """)
        kooc_mangling.mangleAttr(res.body[0], "csmod")
        self.assertEqual(str(res.to_c()), "char *_5csmod_Pc3str;\n")

    def test_char_two_star(self):
        cparse = Declaration()
        res = cparse.parse("""
        char    **str;
        """)
        kooc_mangling.mangleAttr(res.body[0], "cssmod")
        self.assertEqual(str(res.to_c()), "char **_6cssmod_PPc3str;\n")

    def test_array(self):
        cparse = Declaration()
        res = cparse.parse("""
        char    str[];
        """)
        kooc_mangling.mangleAttr(res.body[0], "amod")
        self.assertEqual(str(res.to_c()), "char _4amod_Pc3str[];\n")

    def test_func_with_simple_params(self):
        cparse = Declaration()
        res = cparse.parse("""
        void    print(int i, char zob);
        """)
        kooc_mangling.mangleAttr(res.body[0], "simplemod")
        self.assertEqual(str(res.to_c()), "void _9simplemod_v5print_ic(int i, char zob);\n")

    def test_func_with_ptrs(self):
        cparse = Declaration()
        res = cparse.parse("""
        const int     *alice(char *const c);
        """)
        kooc_mangling.mangleAttr(res.body[0], "ptrfuncmod")
        self.assertEqual(str(res.to_c()), "const int *_10ptrfuncmod_Pi5alice_Pc(char *const c);\n")

    def test_user_type(self):
        cparse = Declaration()
        res = cparse.parse("""
        typedef int bool;
        bool     userfunc(bool, const bool *);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "usermod")
        self.assertEqual(str(res.body[-1].to_c()), "bool _7usermod_4bool8userfunc_4boolP4bool(bool, const bool *);\n")

    def test_void_func(self):
        cparse = Declaration()
        res = cparse.parse("""
        void     func(void);
        """)
        kooc_mangling.mangleAttr(res.body[0], "voidparams")
        self.assertEqual(str(res.to_c()), "void _10voidparams_v4func_v(void);\n")

    def test_struct_func(self):
        cparse = Declaration()
        res = cparse.parse("""
        struct   test {int i;};
        struct test     stfunc();
        """)
        kooc_mangling.mangleAttr(res.body[-1], "stmod")
        self.assertEqual(str(res.body[-1].to_c()), "struct test _5stmod_T4test6stfunc_v();\n")

    def test_enum_func(self):
        cparse = Declaration()
        res = cparse.parse("""
        enum jojo {un = 1, deux};
        enum jojo     func(void);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "enmod")
        self.assertEqual(str(res.body[-1].to_c()), "enum jojo _5enmod_E4jojo4func_v(void);\n")

    def test_union_func(self):
        cparse = Declaration()
        res = cparse.parse("""
        union jojo {int i; char c;};
        union jojo     func(void);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "unmod")
        self.assertEqual(str(res.body[-1].to_c()), "union jojo _5unmod_U4jojo4func_v(void);\n")

    def test_func_struct_param(self):
        cparse = Declaration()
        res = cparse.parse("""
        struct   test {int i;};
        void     func(struct test);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "stpmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _6stpmod_v4func_T4test(struct test);\n")

    def test_func_union_param(self):
        cparse = Declaration()
        res = cparse.parse("""
        union jojo {int i; char c;};
        void     func(union jojo);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "unpmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _6unpmod_v4func_U4jojo(union jojo);\n")

    def test_func_enum_param(self):
        cparse = Declaration()
        res = cparse.parse("""
        enum jojo {un = 1, deux};
        void     func(enum jojo);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "enpmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _6enpmod_v4func_E4jojo(enum jojo);\n")

    def test_func_struct_ptr_param(self):
        cparse = Declaration()
        res = cparse.parse("""
        struct   test {int i;};
        void     func(struct test*);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "stspmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _7stspmod_v4func_PT4test(struct test *);\n")

    def test_func_union_ptr_param(self):
        cparse = Declaration()
        res = cparse.parse("""
        union jojo {int i; char c;};
        void     func(union jojo*);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "enspmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _7enspmod_v4func_PU4jojo(union jojo *);\n")

    def test_func_enum_ptr_param(self):
        cparse = Declaration()
        res = cparse.parse("""
        enum jojo {un = 1, deux};
        void     func(enum jojo*);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "enspmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _7enspmod_v4func_PE4jojo(enum jojo *);\n")

    def test_func_multiple_composed(self):
        cparse = Declaration()
        res = cparse.parse("""
        enum en {un = 1, deux};
        union jojo {int i; char c;};
        struct   test {int i;};
        void     func(struct test, union jojo, enum en);
        """)
        kooc_mangling.mangleAttr(res.body[-1], "allcmpmod")
        self.assertEqual(str(res.body[-1].to_c()), "void _9allcmpmod_v4func_T4testU4jojoE2en(struct test, union jojo, enum en);\n")

if __name__ == '__main__':
    unittest.main(verbosity=3)
