-include .env

# Variables
PELICAN = pipenv run pelican
PELICANOPTS =
S3CMD = pipenv run s3cmd

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
DEV_CONFFILE = $(BASEDIR)/pelicanconf.py
PUB_CONFFILE = $(BASEDIR)/publishconf.py

TAILWIND_INPUT = theme/static/css/input.css
TAILWIND_OUTPUT = theme/static/css/output.css

S3BUCKET ?= your.s3.bucket
OBSIDIANBUCKET ?= your.obsidian.bucket
AWSPROFILE ?= your.configured.aws.profile

# Optional flags
DEBUG ?= 0
ifeq ($(DEBUG), 1)
    PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
    PELICANOPTS += --relative-urls
endif

SERVER ?= 0.0.0.0

PORT ?= 0
ifneq ($(PORT), 0)
    PELICANOPTS += -p $(PORT)
endif

.PHONY: help html clean regenerate serve serve-global devserver devserver-global \
        build-css watch-css sync-to-aws sync-output sync-content sync-content-from-aws

help:
	@echo 'Makefile for a pelican Web site'
	@echo ''
	@echo 'Usage:'
	@echo '   make html                           Generate the web site'
	@echo '   make clean                          Remove generated files'
	@echo '   make regenerate                     Regenerate files upon modification'
	@echo '   make serve [PORT=8000]              Serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  Serve to $(SERVER):8000'
	@echo '   make devserver [PORT=8000]          Serve and regenerate together'
	@echo '   make devserver-global               Regenerate and serve on 0.0.0.0'
	@echo '   make build-css                      Build Tailwind CSS'
	@echo '   make watch-css                      Watch Tailwind CSS for changes'
	@echo '   make sync-to-aws                    Sync output and content to S3'
	@echo '   make sync-output                    Sync output to S3'
	@echo '   make sync-content                   Sync content to S3'
	@echo '   make sync-content-from-aws          Sync content from S3'
	@echo ''
	@echo 'Set DEBUG=1 to enable debugging, e.g. make DEBUG=1 html'
	@echo 'Set RELATIVE=1 to enable relative URLs'

html: build-css
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUB_CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	$(PELICAN) -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUB_CONFFILE)" $(PELICANOPTS)

serve:
	$(PELICAN) -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUB_CONFFILE)" $(PELICANOPTS)

serve-global:
	$(PELICAN) -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUB_CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver: build-css
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(DEV_CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(DEV_CONFFILE)" $(PELICANOPTS) -b 0.0.0.0

build-css:
	npx @tailwindcss/cli -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --compat

watch-css:
	npx @tailwindcss/cli -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --compat --watch

sync-output:
	$(S3CMD) sync --delete-removed --check-md5 output/ s3://$(S3BUCKET)/
	$(S3CMD) put --mime-type="text/css" output/static/css/*.css s3://$(S3BUCKET)/static/css/

sync-content:
	$(S3CMD) sync --delete-removed --check-md5 content/ s3://$(OBSIDIANBUCKET)/content/

sync-to-aws: sync-output sync-content

sync-content-from-aws:
	$(S3CMD) sync s3://$(OBSIDIANBUCKET)/content/ content/
