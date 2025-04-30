#!/bin/bash
# Program:
#   Run streamlit server in background.
# Author: Shu han Hu
# History:
# 2025.04.30    Shuhan Hu   Create script.

# Get server count
echo "Check if server is alive..."
PC=`ps -ef | grep streamlit | wc -l`
PC=`expr $PC - 1` # exclude grep pid
echo "Alive server count: "$PC

# Process alive server
if (( PC > 1 )); then
    # Kill if there is any server alive
    echo "Server is alive!"
    PID=`ps -ef | grep streamlit |head -$PC| awk '{print $2}'`
    kill -9 ${PID}
    echo "Killed Server: "${PID}
else
    # Print tip
    echo "No server alive."
fi

# Start new server
echo "Start new Server..."
nohup streamlit run main.py > logs/server.log 2>&1 &

# Ending tip
echo "Server start!"
