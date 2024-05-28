#!/bin/sh
# Start the Flask API components and Streamlit app in the background
python db_connections.py & 
PID1=$!
python app.py & 
PID2=$!
streamlit run interface.py & 
PID3=$!

# Function to terminate background processes
cleanup() {
  echo "Terminating background processes..."
  kill $PID1 $PID2 $PID3
  wait $PID1 $PID2 $PID3
}

# Trap signals and call cleanup
trap cleanup INT TERM

# Wait for all background processes to complete
wait $PID1 $PID2 $PID3
