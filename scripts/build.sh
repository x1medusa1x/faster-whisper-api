#!/bin/sh
echo "*** Rebuild start ***"

cd scripts || exit

# Prompt user for input
echo "Want to update images before rebuild? (y/n) [default: y]: "
read UPDATE_IMAGES
UPDATE_IMAGES=${UPDATE_IMAGES:-y}

# Check user input in a POSIX-compatible way
if [ "$UPDATE_IMAGES" = "y" ] || [ "$UPDATE_IMAGES" = "Y" ]; then
    NGINX_VERSION=$(grep -oP '^NGINX_VERSION=\K.*' .env)
    WHISPER_VERSION=$(grep -oP '^WHISPER_VERSION=\K.*' .env)

    docker pull "nginx:$NGINX_VERSION"
    docker pull "lscr.io/linuxserver/faster-whisper:$WHISPER_VERSION"
fi

echo "*** Rebuilding application ***"
docker compose -p whisper build --no-cache
docker compose -p whisper up -d

echo "*** Rebuild ended ***"
