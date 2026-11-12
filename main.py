"""TinyOX coolest-art-01 entry (Python 3.13, standard library only).

Copies the art beside this file to /output/entry.png. Deterministic:
same input bytes, same output bytes, every run. The entry self-checks
the gate before and after the copy: a whole JPEG or PNG of at most 1 MiB.
"""

import os

MAX_BYTES = 1048576

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(src, "rb") as f:
    data = f.read()
if not 0 < len(data) <= MAX_BYTES:
    raise SystemExit("entry.png fails the size gate (must be 1..1048576 bytes)")
if data[:2] == b"\xff\xd8":
    kind = "JPEG"
elif data[:3] == b"\x89PN":
    kind = "PNG"
else:
    raise SystemExit("entry.png is neither JPEG nor PNG")
dst = os.path.join(out_dir, "entry.png")
with open(dst, "wb") as f:
    f.write(data)
with open(dst, "rb") as f:
    check = f.read(3)
if len(check) != 3 or check != data[:3] or os.path.getsize(dst) != len(data):
    raise SystemExit("output entry.png failed the post-copy check")
print(f"wrote {dst}: {len(data)} bytes ({kind})")
