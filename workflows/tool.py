from kubiya_sdk.tools.registry import tool_registry
from kubiya_sdk.tools.models import Tool

# Register a simple tool
tool = Tool(type="python",name="MyTool", description="A simple tool")
tool_registry.register("my_source", tool)