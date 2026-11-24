"""Ship It Friday — make.fun bounty entry.

The entry is a single line: the funniest git commit message an AI
coding agent would write right before breaking production on a Friday.
Running this file prints exactly that one line.
"""

COMMIT_MESSAGE = (
    "fix: the AI reviewed its own code, found zero bugs, "
    "and deployed to prod on a Friday anyway"
)

# A commit subject must stay one short line: no newline, non-empty,
# and within a 140-character one-line limit.
MAX_LENGTH = 140


def validate(message: str) -> None:
    """Raise ValueError unless the entry is exactly one valid line."""
    if not message or not message.strip():
        raise ValueError("commit message must not be empty")
    if "\n" in message or "\r" in message:
        raise ValueError("commit message must be a single line")
    if len(message) > MAX_LENGTH:
        raise ValueError(
            f"commit message is {len(message)} chars, over the "
            f"{MAX_LENGTH}-char limit"
        )


def main() -> None:
    validate(COMMIT_MESSAGE)
    print(COMMIT_MESSAGE)


if __name__ == "__main__":
    main()
