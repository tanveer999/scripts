#!/bin/bash

# simulate command failure
false

error_code=$?

if [[ $error_code -ne 0 ]]; then
    echo "Error code: $error_code"
    exit $error_code
fi