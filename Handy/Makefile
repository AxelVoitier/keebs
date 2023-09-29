merge-configs: Handy.yaml

Handy.yaml: Handy-layout.yaml Handy-keymap.yaml Handy-outlines.yaml
	../keebs.py ergogen merge-configs Handy-layout.yaml Handy-keymap.yaml Handy-outlines.yaml -o Handy.yaml

gen-kle: Handy.json

Handy.json: Handy.yaml points.yaml units.yaml
	../keebs.py ergogen gen-kle Handy.yaml
