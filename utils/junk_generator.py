import random

def generate_junk_code():
    lines = []
    for _ in range(5):
        reg = f"v{random.randint(0, 5)}"
        val = random.randint(0, 5000)
        lines.append(f"const/16 {reg}, {val}")
        lines.append(f"add-int {reg}, {reg}, {reg}")
    return "\n    ".join(lines)
