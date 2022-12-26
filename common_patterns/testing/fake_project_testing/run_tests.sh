#!/usr/bin/bash
python -m unittest discover -s tests/unit/ -v
python -m unittest discover -s tests/integration/ -v