#!/usr/bin/env python3
"""One-liner entry for 404 One-Liner Laughs.

A houseplant files for custody of the sunlight after being moved behind
the bookshelf a third time — and the fern testifies against its owner.
A household object that is not smart, but sues. 137 characters, 68% of
the 200 cap, one line, setup and payoff in the same breath.
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class OneLiner:
    text: str
    cap: int
    out_dir_env: str = "MAKEFUN_OUTPUT_DIR"
    default_dir: str = "/output"
    filename: str = "entry.txt"
    mode: int = 0o644

    def problems(self):
        if not self.text.strip():
            return "blank line"
        if "\n" in self.text or "\r" in self.text:
            return "more than one line"
        if len(self.text) > self.cap:
            return f"{len(self.text)} chars over cap {self.cap}"
        return None

    def target(self):
        folder = os.environ.get(self.out_dir_env, self.default_dir)
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, self.filename)

    def publish(self):
        flaw = self.problems()
        if flaw:
            raise SystemExit(f"entry rejected: {flaw}")
        path = self.target()
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(self.text)
        os.chmod(path, self.mode)
        print(self.text)
        print(f"({len(self.text)} characters)")


JOKE = OneLiner(
    # QUILL-C: household object that sues, not a smart gadget that complains
    # — the smart-fridge/GPS angle is saturated in this slug.
    text="My houseplant filed for custody of the sunlight after I moved it behind the bookshelf for the third time — the fern testified against me.",
    cap=200,
)

if __name__ == "__main__":
    JOKE.publish()
