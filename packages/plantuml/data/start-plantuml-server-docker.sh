#!/bin/bash

# https://github.com/plantuml/plantuml-server

docker run -d -p 8080:8080 plantuml/plantuml-server:jetty
# docker run -d -p 8080:8080 plantuml/plantuml-server:tomcat
