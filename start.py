import subprocess
import os

LLAMA_SERVER = os.path.expanduser("~/llama.cpp/build/bin/llama-server")
MODEL = os.path.expanduser("~/models/model.gguf")

cmd = [
LLAMA_SERVER,
"-m", MODEL,

# Faster than 32K/64K while still large enough for coding
"-c", "16384",

# Use all 4 Codespace CPU threads
"-t", "4",

# Single user
"-np", "1",

# Limit giant responses
"-n", "1024",

# Networking
"--host", "0.0.0.0",
"--port", "8000",

# Faster startup
"--no-warmup"

]

subprocess.run(cmd)
