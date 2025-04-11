#!/bin/sh
echo "*** Restarting... ***"

cd scripts || exit

docker compose -p whisper restart

echo "*** Restarted ***"
