import base64
import requests, io
from PIL import Image
import logging


def generate_flowchart(file_name, code):
    graph = f"""
    {code}
    """
    print(graph)
    graphbytes = graph.encode("ascii")

    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")

    try:
        img = Image.open(io.BytesIO(requests.get('https://mermaid.ink/img/' + base64_string).content))
        img.save(f"{file_name}.png")
        return img
    except:
        logging.error(f"Failed to download flowchart image")
