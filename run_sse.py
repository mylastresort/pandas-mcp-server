import os

import server  # noqa: F401  (import registers all @mcp.tool() functions)
from core.config import mcp
from mcp.server.transport_security import TransportSecuritySettings

mcp.settings.host = os.getenv("HTTP_BIND_ADDRESS", "0.0.0.0")
mcp.settings.port = int(os.getenv("HTTP_BIND_PORT", "8000"))

# Allow the docker-compose service hostname through DNS-rebinding protection.
# The container only ever sees traffic from the internal compose network
# (ai-agent-py) or the mapped host port, so this is safe here.
if mcp.settings.transport_security is None:
    mcp.settings.transport_security = TransportSecuritySettings()
mcp.settings.transport_security.allowed_hosts = [
    "pandas-mcp:8000",
    "localhost:8000",
    "127.0.0.1:8000",
]

if __name__ == "__main__":
    server.init_logging()
    mcp.run(transport="sse")
