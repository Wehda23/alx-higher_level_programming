#!/bin/bash
# Sends a request
curl -o /dev/null -sw "%{http_code}" $1
