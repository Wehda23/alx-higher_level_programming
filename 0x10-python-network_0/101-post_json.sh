#!/bin/bash
# Script that is soo cool
curl -sX POST "$1" -H "Content-Type: application/json" -d @$2 -L
