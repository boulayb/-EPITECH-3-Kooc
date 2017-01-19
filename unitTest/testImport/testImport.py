#! /usr/bin/env python3

import sys
sys.path.append("../../")

from cnorm.passes import to_c
import unittest
from kooc import Kooc

class       TestImport(unittest.TestCase):

    def test_multiple_import(self):
        kooc = Kooc()
        res = kooc.parse("""
        @import \"zob.kh\"
        @import \"zob.kh\"
        @import \"zob.kh\"
        @import \"zob.kh\"
        @import \"zob.kh\"
        @import \"zob.kh\"
        """)

        self.assertEqual(str(res.to_c()), '#include "zob.h"\n')


    def test_simple_import(self):
        kooc = Kooc()
        res = kooc.parse("""
        @import \"zob.kh\"
        """)

        self.assertEqual(str(res.to_c()), '#include "zob.h"\n')


    def test_no_import(self):
        kooc = Kooc()
        res = kooc.parse("")

        self.assertEqual(str(res.to_c()), "")


    def test_import(self):
        kooc = Kooc()
        res = kooc.parse("""
        @import \"test.kh\"
        """)

        self.assertEqual(str(res.to_c()), '#include "test.h"\n')

    def test_two_imports(self):
        kooc = Kooc()
        res = kooc.parse("""
        @import \"zob.kh\"
        @import \"test.kh\"
        """)

        self.assertEqual(str(res.to_c()), '#include "zob.h"\n#include "test.h"\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)
