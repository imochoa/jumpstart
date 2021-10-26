
IMGNAME := ubuntu:20.04

# Auto variables
DATE := $(shell date)
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)
COMMIT_HASH := $(shell git rev-parse HEAD | cut -c1-8)
INTERACTIVE := $(shell [ -t 0 ] && echo 1)
export INTERACTIVE

# Host paths
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
REPO_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
TMP_DIR := ${REPO_DIR}/tmp
PROVISION_DIR := ${REPO_DIR}/provision
INDEX_DIR := ${REPO_DIR}/index

# Docker paths
DOCKER_CODE_DIR := /home/repo
DOCKER_VENV_DIR  := /home/venv
DOCKER_PYTHON := ${DOCKER_VENV_DIR}/bin/python

# -------------------------------------------------------------------------------- #
# BUILDING
# -------------------------------------------------------------------------------- #

# For debugging:
# 		-v ${REPO_DIR}:${DOCKER_CODE_DIR} \

.PHONY: test-everything
test-everything:
	docker run --rm -it                          \
		-v ${INDEX_DIR}/x64__ubuntu2004:/index   \
		-v ${PROVISION_DIR}/docker-ubuntu-setup.sh:/docker-setup.sh \
		-v ${PROVISION_DIR}/type-test.sh:/test.sh \
		--workdir /index \
		ubuntu:20.04          \
		bash -c '\
		. /docker-setup.sh \
		&& . /test.sh apt \
		&& . /test.sh snap \
		&& . /test.sh deb \
		&& . /test.sh bin \
		&& . /test.sh py \
		&& . /test.sh src \
		'

reset-tests:
	find ${INDEX_DIR}  \( -iname "passed" -o -iname "*.log" \) -delete

.PHONY: debug-ubuntu
debug-ubuntu:
	docker run --rm -it                          \
		-v ${INDEX_DIR}/x64__ubuntu2004:/index   \
		-v ${PROVISION_DIR}/docker-ubuntu-setup.sh:/docker-setup.sh \
		-v ${PROVISION_DIR}/apt-install-test.sh:/install-test.sh \
		--workdir /index \
		ubuntu:20.04          \
		bash -c '\
 		. /docker-setup.sh \
  		&& cd "/index/materia-theme/apt" \
  		&& . ./install.sh \
  		&& . ./status.sh \
		'

.PHONY: help
help:
	cat Makefile
