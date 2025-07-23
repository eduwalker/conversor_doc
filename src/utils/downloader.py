import requests
import tempfile


def baixar_arquivo(url):
    response = requests.get(url)
    response.raise_for_status()
    suffix = "." + url.split(".")[-1].split("?")[0].split("#")[0]
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(response.content)
    temp_file.close()
    return temp_file.name
