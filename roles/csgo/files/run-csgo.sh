#!/bin/sh

/home/steam/csgo/srcds_linux \
  -net_port_try 1 \
  -usercon \
  -port $SERVER_PORT \
  +sv_setsteamaccount "$GSLT" \
  +exec "instance_${1}.cfg"
