#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
cd secrets
echo "$DKEY"
gpg --quiet --batch --yes --decrypt --passphrase="$DKEY" \
--output key.json key.json.gpg