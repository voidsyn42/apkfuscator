#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: voidsyn42
# 📄 apkfuscator.py

import os
import re
import random
import string
import argparse
from utils.junk_generator import generate_junk_code

def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def obfuscate_string_literals(smali_code):
    # Replace const-string with XOR logic
    pattern = r'const-string (v\d+), "(.*?)"'
    def replacer(match):
        reg, string_val = match.groups()
        xor_key = 0x42
        encoded = ','.join([str(ord(c) ^ xor_key) for c in string_val])
        decode_code = f"""
    const/16 {reg}, {xor_key}
    # decoded: {string_val}
    # XOR'd: {encoded}
    # Replace in runtime (simulate, PoC)
        """
        return decode_code
    return re.sub(pattern, replacer, smali_code)

def rename_methods(smali_code):
    pattern = r'\.method.* (\w+)\('
    methods = re.findall(pattern, smali_code)
    mapping = {m: random_name(6) for m in methods}
    for orig, new in mapping.items():
        smali_code = re.sub(r'\b' + orig + r'\b', new, smali_code)
    return smali_code

def inject_junk_code(smali_code):
    junk = generate_junk_code()
    return smali_code.replace('.prologue', f'.prologue\n    {junk}')

def process_directory(smali_dir, output_dir):
    for root, dirs, files in os.walk(smali_dir):
        for file in files:
            if file.endswith('.smali'):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, smali_dir)
                output_path = os.path.join(output_dir, rel_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                with open(input_path, 'r') as f:
                    code = f.read()

                code = obfuscate_string_literals(code)
                code = rename_methods(code)
                code = inject_junk_code(code)

                with open(output_path, 'w') as f:
                    f.write(code)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        code = f.read()

    code = obfuscate_string_literals(code)
    code = rename_methods(code)
    code = inject_junk_code(code)

    with open(args.output, 'w') as f:
        f.write(code)

    print(f"[+] Obfuscation complete → {args.output}")

if __name__ == '__main__':
    main()
