#!/bin/sh

# Decrypt the file
echo "$PWD"
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$FIREBASEKEY" \
--output ./secrets/key.json key.json.gpg