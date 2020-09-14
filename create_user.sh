#!/bin/bash -v
# Create jovyan user, permissions, add conda init to startup script
NB_USER=jovyan
NB_UID=2005
echo "Creating ${NB_USER} user..."
groupadd --gid ${NB_UID} ${NB_USER}
useradd --create-home --gid ${NB_UID} --no-log-init --uid ${NB_UID} ${NB_USER}



