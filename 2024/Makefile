.PHONY: pdf

INPUTS = $(shell find . -maxdepth 1 -name "*.md" | sort | tr '\n' ' ')

pdf:
	pandoc ${INPUTS} --pdf-engine=weasyprint --css=annual-report.css -o out.pdf

html:
	pandoc ${INPUTS} --pdf-engine=weasyprint --css=annual-report.css -o out.html
