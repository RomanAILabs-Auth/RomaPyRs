# Copyright (c) 2026 Daniel Harding - RomanAILabs

import unittest
import os
from .core import PyRustTranspiler
import ast

class TestRomaPyRs(unittest.TestCase):
    def test_transpile_fib(self):
        code = """
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
"""
        tree = ast.parse(code)
        transpiler = PyRustTranspiler()
        rust_code = transpiler.generate_rust_code(tree, {}, 'fib')
        self.assertIn('fn fib(n: i64) -> i64', rust_code)
        self.assertIn('HashMap', rust_code)  # Memoization

    def test_import_mapping(self):
        code = "import numpy"
        tree = ast.parse(code)
        transpiler = PyRustTranspiler()
        transpiler.visit(tree)
        self.assertIn('use ndarray as np;', transpiler.imports)

if __name__ == '__main__':
    unittest.main()
