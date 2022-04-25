#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
cd secrets
gpg --quiet --batch --yes --decrypt --passphrase="$DKEY" \
--output .env .env.gpg