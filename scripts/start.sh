#!/bin/sh
echo "*** Starting... ***"

cd scripts || exit

docker compose -p whisper up -d

echo "*** Started ***"
