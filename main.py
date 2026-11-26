"""Write the fixed ENTRY_TEXT error-message string constant to entry.txt.

Use /output/entry.txt by default, or $MAKEFUN_OUTPUT_DIR/entry.txt when set.
Gate: one nonblank UTF-8 line, 1–140 characters, with no trailing newline.
"""

import os
from pathlib import Path
import shutil


ENTRY_TEXT = (
    "Error: token budget exhausted; I was about to accept full responsibility "
    "for the data loss, but fortunately"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for stale_path in output_dir.iterdir():
        if stale_path.is_symlink() or not stale_path.is_dir():
            stale_path.unlink()
        else:
            shutil.rmtree(stale_path)

    (output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
