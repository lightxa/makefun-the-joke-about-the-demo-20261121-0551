"""Write a one-line joke about working beside AI coding agents.

The joke is written to ``entry.txt`` inside the output directory:
``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``.

Pure standard library, deterministic, no network.
"""

import os

JOKE = (
    "My coding agent fixed the demo bug on stage by deleting the feature, "
    "then asked why the audience wasn't clapping."
)


def main() -> None:
    # The gate: 1 to 280 characters (Unicode code points), one line,
    # and not only white space. Fail loudly rather than ship a bad entry.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-280")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not JOKE.strip():
        raise ValueError("joke must not be only white space")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
