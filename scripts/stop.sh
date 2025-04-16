#!/bin/sh
echo "*** Starting... ***"

cd scripts || exit

docker compose -p whisper down

echo "*** Stopped ***"
