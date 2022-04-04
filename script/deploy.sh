#!/bin/bash

gcloud functions deploy echo-bot --entry-point echo_bot \
  --trigger-http --allow-unauthenticated \
  --env-vars-file .env.yaml
