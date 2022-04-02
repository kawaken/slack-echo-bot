#!/bin/bash


gcloud functions deploy echo-bot --entry-point verify \
  --runtime python39 \
  --trigger-http --allow-unauthenticated
