# Define your own either by changing your parent folder name, or call make with parameter config_name=...
config_name = $(shell basename $(shell pwd))

.PHONY: merge-configs keebs/ergogen clean-ergogen-container gen-kle

merge-configs: $(config_name).yaml

$(config_name).yaml: $(sort $(wildcard $(config_name)-*.yaml))
	../keebs.py ergogen merge-configs $^ -o $@

keebs/ergogen: ../ergogen-compose.yaml
ifeq ($(strip $(shell docker images -q keebs/ergogen)),)
	UID=$(shell id -u) GID=$(shell id -g) docker compose -f ../ergogen-compose.yaml build
endif

clean-ergogen-container:
	docker rmi keebs/ergogen:latest

ergogen_outputs = ergogen-output/points/points.yaml ergogen-output/points/units.yaml

ifeq ($(strip $(shell docker images -q keebs/ergogen)),)
ergogen-output/%: keebs/ergogen $(config_name).yaml
else
ergogen-output/%: $(config_name).yaml
endif
	docker run --rm -v $(shell pwd):/config keebs/ergogen $(config_name).yaml --debug --clean --output ergogen-output

gen-kle: $(config_name).json

$(config_name).json: $(config_name).yaml $(ergogen_outputs)
	../keebs.py ergogen gen-kle ${config_name}.yaml --points-yaml ergogen-output/points/points.yaml --units-yaml ergogen-output/points/units.yaml
