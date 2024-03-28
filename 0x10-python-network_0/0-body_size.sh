#!/usr/bin/env bash
# Script used to send a request to port
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
