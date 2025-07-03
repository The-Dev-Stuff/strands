# AI Agent with Strands

This is a simple AI agent built with [Strands](https://github.com/strands-agents/sdk-python), a framework for building AI agents.

This sample agent uses tools to complete tasks.

## In Progress
- [ ] Human in the Loop (HITL)
- [ ] Short term memory
- [ ] Long term memory
- [ ] Logging reasoning
- [ ] Add MCP
- [ ] Agent to Agent communication (A2A) with pause + resume
- [ ] Expose agent as a web service with authentication


## Setup the .venv and install dependencies

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## Run the agent
```bash
# within the virtual environment
python agent.py
```