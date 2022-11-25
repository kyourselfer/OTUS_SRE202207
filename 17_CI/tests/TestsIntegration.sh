#!/bin/bash
pip3 install -qqq --no-cache-dir -r requirements.txt
pytest --junitxml=junit-Integration.xml -v -s TestsIntegration.py
