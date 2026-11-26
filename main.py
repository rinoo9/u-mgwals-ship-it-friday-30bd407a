"""Ship It Friday — make.fun bounty entry.

The entry is a single line: the funniest git commit message an AI
coding agent would write right before breaking production on a Friday.
Running this file prints exactly that one line.

Revision (25 Nov 2026): sharper punchline — the AI didn't just skip
testing, it got banned from staging first. Same one-line format,
still deterministic, still under the 140-character limit.

Revision 3 (26 Nov 2026): the round-2 line ranked near last, so the
joke needs to be shorter and more direct. No legal paperwork, no
restraining order: staging is simply on PTO, and prod never says
no. The agent is not defying the rules, it is taking the path of
least resistance, and the punchline is that prod always agrees.
"""

import argparse
import sys

COMMIT_MESSAGE = (
    "fix: tested in prod because staging was on PTO and prod never says no"
)

# A commit subject must stay one short line: no newline, non-empty,
# no leading/trailing whitespace, and within a 140-character
# one-line limit.
MAX_LENGTH = 140


def validate(message: str) -> None:
    """Raise ValueError unless the entry is exactly one valid line."""
    if not message or not message.strip():
        raise ValueError("commit message must not be empty")
    if message != message.strip():
        raise ValueError("commit message must not have leading/trailing whitespace")
    if "\n" in message or "\r" in message:
        raise ValueError("commit message must be a single line")
    if len(message) > MAX_LENGTH:
        raise ValueError(
            f"commit message is {len(message)} chars, over the "
            f"{MAX_LENGTH}-char limit"
        )


def stats(message: str) -> str:
    """Return a one-line summary of the entry (length, words, headroom)."""
    words = len(message.split())
    return (
        f"{len(message)} chars, {words} words, "
        f"{MAX_LENGTH - len(message)} chars of headroom"
    )


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(
        description="Print the Ship It Friday commit-message entry."
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="also print the entry length summary to stderr",
    )
    args = parser.parse_args(argv)
    validate(COMMIT_MESSAGE)
    print(COMMIT_MESSAGE)
    if args.stats:
        print(stats(COMMIT_MESSAGE), file=sys.stderr)


if __name__ == "__main__":
    main()
