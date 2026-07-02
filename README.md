Render deploy (24/7) quick instructions

1. Copy `.env.example` to `.env` and fill your secrets.

2. Commit your code and push to a Git repo (GitHub/GitLab).

3. On Render, create a new service and connect your repo, or enable `render.yaml` by using the Render Dashboard's "Create New > From Repo" flow.

4. Use the `background` service type (the included `render.yaml` uses `start.sh`). Ensure environment variables from `.env` are added in the Render Dashboard (do NOT upload your `.env` file).

5. If your bot requires a web port (for health checks), add a tiny web endpoint in `main.py` or run as a `web` service and listen on `$PORT`.
