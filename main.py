#!/usr/bin/env python3
"""news-image-20261122 entry: copy the baked-in front page to the output dir.

Python 3.13, standard library only, no network. Deterministic: two runs
write byte-identical output.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIM = 1024
SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from a PNG IHDR chunk."""
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("PNG missing IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    with open(source, "rb") as fh:
        data = fh.read()

    if data[:8] != PNG_MAGIC:
        print("source is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"source is {len(data)} bytes, over the 1 MiB cap", file=sys.stderr)
        return 1
    width, height = png_dimensions(data)
    if width > MAX_DIM or height > MAX_DIM:
        print(f"source is {width}x{height}, over the 1024x1024 cap", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    with open(target, "wb") as fh:
        fh.write(data)
    os.chmod(target, 0o644)

    with open(target, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        print("output does not match source byte for byte", file=sys.stderr)
        return 1
    if oct(os.stat(target).st_mode & 0o777) != "0o644":
        print("output file mode is not 0644", file=sys.stderr)
        return 1

    print(f"wrote {target} ({len(written)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
