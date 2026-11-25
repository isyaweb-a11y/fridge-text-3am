"""The 3AM Fridge Text.

One line a smart fridge texts its owner at 3am. The fridge has been awake
all night watching, and it finally has something to say: the leftovers have
been moved to the front, the owner eats standing in the dark, and the
appliance is still judging. Gate: 1-140 characters.
"""

ENTRY = (
    "3am. I moved your leftovers to the front. Eat them standing in the "
    "dark like always — I have seen things, and I am still judging you."
)


def check_fridge_text(text: str) -> str:
    """A fridge text needs the hour, the food, and the judgement."""
    assert text.startswith("3am."), "fridge must timestamp the text at 3am"
    assert "leftovers" in text, "fridge must mention the food it is guarding"
    assert "judging" in text, "fridge must keep its judgemental voice"
    return text


def main() -> None:
    text = check_fridge_text(" ".join(ENTRY.split()))
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
