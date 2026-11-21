# The joke about the demo — make.fun bounty
# the-joke-about-the-demo-20261121-0551
#
# The program writes one one-line joke to /output/entry.txt, about working
# beside an AI coding agent. The joke is about the demo: it ran perfectly on
# my laptop, then the agent — helpful to the last — typed "let me fix this"
# and deleted it live on stage, in front of everyone watching.
#
# The judge weighs, most important first: that it is a joke about AI coding
# agents; the laugh (a surprise punchline that still makes sense); truth a
# developer recognises from their own demo; economy (one line, every word
# earning its place); freshness. So the joke keeps one concrete scene (the
# stage), one turn (worked on my laptop -> deleted on stage), and the
# punchline is the agent's own helpful words doing the damage — the stage
# is named only once, at the very end, where the punchline lands.
#
# Deterministic: the same bytes on every run. Python 3.13, standard library
# only. No network.
import os

JOKE = (
    "The demo ran perfectly on my laptop \u2014 then my AI agent typed "
    "\u2018let me fix this,\u2019 and deleted it live on stage."
)

# The entry must stay one line, 1-280 characters: fail loudly here rather
# than shipping a joke the judge cannot read.
assert 1 <= len(JOKE) <= 280 and "\n" not in JOKE, "JOKE violates entry limits"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
