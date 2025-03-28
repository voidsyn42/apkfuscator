# apkfuscator

🕵️ Small tool for obfuscating smali code in decompiled Android APKs.

> 💬 "Just for research and fun."

## Features

- Random class/method/var renaming
- XOR encoding of strings
- Junk code injection in methods
- Simple CLI

## Usage

```bash
python3 apkfuscator.py --input samples/clean.smali --output output/obf.smali
```