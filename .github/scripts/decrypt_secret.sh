#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
cd ..
gpg --quiet --batch --yes --decrypt --passphrase="$FIREBASEKEY" \
--output /home/chinou/actions-runner/_work/esie-bot/esie-bot/secrets/key.json key.json.gpg