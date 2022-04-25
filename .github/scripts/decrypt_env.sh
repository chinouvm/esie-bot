#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
KEY=$DKEY
cd secrets
gpg --quiet --batch --yes --pinentry-mode loopback --decrypt --passphrase=KEY \
--output .env .env.gpg