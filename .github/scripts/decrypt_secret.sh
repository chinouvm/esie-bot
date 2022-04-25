#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
cd secrets
KEY=$DKEY
gpg --quiet --batch --yes --pinentry-mode loopback --decrypt --passphrase=KEY \
--output key.json key.json.gpg