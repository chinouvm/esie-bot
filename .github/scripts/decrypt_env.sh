#!/bin/sh

# Decrypt the file
echo "$PWD"
echo "$HOME"
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$ENVKEYS" \
--output ./secrets/.env .env.gpg