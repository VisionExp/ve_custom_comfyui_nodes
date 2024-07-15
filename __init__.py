from .nodes.LoadImgFromInputUrl import LoadImgFromInputUrl
from .nodes.asset_image_node import AssetImage

NODE_CLASS_MAPPINGS = {
    "LoadImgFromInputUrl": LoadImgFromInputUrl,
    "assets/Asset Image": AssetImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImgFromInputUrl": "Load Image from input URL",
    "Asset Image": "assets/Asset Image",
}
