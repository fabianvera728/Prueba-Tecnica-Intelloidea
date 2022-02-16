current-dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL = /bin/sh

.DEFAULT_GOAL := help

help:
	@echo "make help:	Obtener ayuda" && \
	echo "make start:     Construir la imagen y levantar el contenedor" && \
	echo "make build:     Construir la imagen y levantar el contenedor" && \
	echo "make stop:    Detener la ejecuión del contenedor"

start:
	@echo "🐙 Construyendo la imagen antes de levantar el contenedor 🐬" && docker-compose up --build

dev: stop start

.PHONY = build
build:
	@echo "🐙 Construyendo la imagen antes de levantar el contenedor 🐬" && docker-compose up --build

stop:
	@echo "🐙 Detener la ejecución del contenedor 🐬" && docker-compose stop

