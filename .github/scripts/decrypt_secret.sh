#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
cd secrets
KEY=$DKEY
echo KEY
gpg --quiet --batch --yes --decrypt --passphrase=KEY \
--output key.json key.json.gpg