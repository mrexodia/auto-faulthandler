# auto-faulthandler

Automatically enable Python's `faulthandler` for extension development.

## Why?

When developing native Python extensions (C/C++/Rust), crashes produce annoying macOS popup dialogs. This package automatically enables `faulthandler` to dump crash tracebacks to stderr instead, making debugging much faster. This is extremely relevant when developing with LLMs, because they get useful feedback right away.

## Installation

Install the package in your virtual environment:

```bash
pip install auto-faulthandler
```

With uv in development mode:

```bash
uv add --dev auto-faulthandler
```

## Usage

Once installed, it just works! Every Python process will automatically enable faulthandler.

```python
# No imports needed! Just run your code:
import my_crashy_extension
my_crashy_extension.do_something()  # Crashes will print to stderr
```

**Note**: You need Python 3.14 or higher to get a call stack.

## Configuration

### Disable temporarily
```bash
export AUTO_FAULTHANDLER_DISABLE=1
python your_script.py
```

### Uninstall
```bash
pip uninstall auto-faulthandler
```

## How it works

This package installs a `.pth` file in your Python's `site-packages` directory. The `.pth` file automatically imports the `auto_faulthandler` module on Python startup, which enables `faulthandler.enable()`.

## Similar Projects

- [auto-dotenv](https://github.com/hmiladhia/auto-dotenv) - Automatically load .env files
- [auto-truststore](https://github.com/zen-xu/auto-truststore) - Automatically trust (self-signed) certificates from the system store

## License

MIT
