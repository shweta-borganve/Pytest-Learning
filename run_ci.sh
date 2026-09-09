#!/bin/bash

echo "Installing dependencies..."
uv sync

echo "Running tests..."
uv run python -m pytest

if [ $? -eq 0 ]; then
    echo "All tests passed! CI successful."
else
    echo "Tests failed! CI failed."
    exit 1
fi 