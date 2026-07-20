#!/bin/bash
# curl to display all HTTP methods the server accepts
curl -sl "$1" | grep "allow" | cut -d " " -f 2-
