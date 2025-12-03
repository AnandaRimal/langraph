import os
import sys

# Add current directory to path so we can import basic
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from basic import app

try:
    png_data = app.get_graph().draw_mermaid_png()
    with open("reflection_graph.png", "wb") as f:
        f.write(png_data)
    print("Graph generated successfully.")
except Exception as e:
    print(f"Error generating graph: {e}")
