#!/bin/bash
# List all allowed methods
curl -sI ALLOW "$1" -L | grep "Allow" | cut -d " " -f2
