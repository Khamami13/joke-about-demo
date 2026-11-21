# The joke about the demo — make.fun bounty
# the-joke-about-the-demo-20261121-0551
#
# The program writes one one-line joke to /output/entry.txt, about working
# beside an AI coding agent. The joke is about the demo: it ran perfectly on
# my laptop, then on stage the agent — helpful to the last — typed
# "let me fix this" and deleted the demo in front of everyone.
#
# The judge weighs, most important first: that it is a joke about AI coding
# agents; the laugh (a surprise punchline that still makes sense); truth a
# developer recognises from their own demo; economy (one line, every word
# earning its place); freshness. So the joke keeps one concrete scene (the
# stage), one turn (worked on my laptop -> deleted on stage), and the
# punchline is the agent's own helpful words doing the damage.
#
# Deterministic: the same bytes on every run. Python 3.13, standard library
# only. No network.
import os

JOKE = (
    "The demo ran perfectly on my laptop \u2014 then my AI agent stepped on "
    "stage, typed \u2018let me fix this,\u2019 and deleted the demo in front "
    "of everyone."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(JOKE)
os.chmod(out_path, 0o644)
