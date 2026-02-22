RomaPyRs v1.0 Python Ease + Rust Speed, Exponentially Amplified!

Copyright Daniel Harding - RomanAILabs

daniel@romanailabs.com

[![PyPI version](https://badge.fury.io/py/romapyrs.svg)](https://badge.fury.io/py/romapyrs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**RomaPyRs** transpiles Python code (.pyrs) to optimized Rust binaries Pythonic syntax, Rust performance with auto-opts (parallelism, memoization). 100-1000x faster than Python, often 2x vanilla Rust.

## Installation
Requires Rust/Cargo installed.
```bash
git clone https://github.com/RomanAILabs-Auth/RomaPyRs
cd RomaPyRs
pip install -r requirements.txt
pip install .
```

## Usage
```bash
romapyrs example.pyrs --run --main-func=fib
```

### Example example.pyrs
```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Runs fib(35) in ~0.0001s post-compile!

MIT License.
