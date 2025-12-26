-include .env

PY?=
PELICAN?=pipenv run pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
DEVELOPMENT_CONFFILE=$(BASEDIR)/development_pelicanconf.py

TAILWIND_INPUT=theme/static/css/input.css
TAILWIND_OUTPUT=theme/static/css/output.css

S3BUCKET ?= your.s3.bucket
OBSIDIANBUCKET ?= your.obsidian.bucket
AWSPROFILE ?= your.configured.aws.profile


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '   make build-css                      build tailwind css                 '
	@echo '   make watch-css                      watch tailwind css for changes     '
	@echo '   make sync-to-aws                    sync output and content to S3      '
	@echo '   make sync-output                    sync output to S3                  '
	@echo '   make sync-content                   sync content to S3                 '
	@echo '   make sync-content-from-aws          sync content from S3               '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html: build-css
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	$(PELICAN) -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	$(PELICAN) -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	$(PELICAN) -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(DEVELOPMENT_CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(DEVELOPMENT_CONFFILE)" $(PELICANOPTS) -b 0.0.0.0


build-css:
	npx @tailwindcss/cli -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --compat

watch-css:
	npx @tailwindcss/cli -i $(TAILWIND_INPUT) -o $(TAILWIND_OUTPUT) --compat --watch

sync-output:
# 	aws s3 sync output/ s3://$(S3BUCKET)/ --delete --profile $(AWSPROFILE)
# 	aws s3 sync output/ s3://$(S3BUCKET)/ --delete --size-only --profile $(AWSPROFILE)
# 	pipenv run s3cmd sync --delete-removed --check-md5 output/ s3://$(S3BUCKET)/
	pipenv run s3cmd sync --delete-removed --check-md5 output/ s3://mhrafin.dev/
	pipenv run s3cmd put --mime-type="text/css" output/static/css/*.css s3://mhrafin.dev/static/css/

sync-content:
	aws s3 sync content/ s3://$(OBSIDIANBUCKET)/content/ --delete --profile $(AWSPROFILE)

sync-to-aws: sync-output sync-content

sync-content-from-aws:
	aws s3 sync s3://$(OBSIDIANBUCKET)/content/ content/ --profile $(AWSPROFILE)

.PHONY: html help clean regenerate serve serve-global devserver devserver-global build-css watch-css sync-to-aws sync-output sync-content sync-content-from-aws
