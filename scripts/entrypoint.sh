#!/bin/bash

if [ "$MODE_ENV" = "dev" ]; then
    echo "Running in DEV mode..."
    tail -f /dev/null
else
    echo "Running in PROD mode..."
    python3 src/pipeline.py
    flask run --host=0.0.0.0
fi
