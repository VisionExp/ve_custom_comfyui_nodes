from .nodes.LoadImgFromInputUrl import LoadImgFromInputUrl
from .nodes.asset_image_node import AssetImage
from .nodes.render3d import Render3d

NODE_CLASS_MAPPINGS = {
    "LoadImgFromInputUrl": LoadImgFromInputUrl,
    "assets/Asset Image": AssetImage,
    "render3d/Render Node": Render3d,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImgFromInputUrl": "Load Image from input URL",
    "Asset Image": "assets/Asset Image",
    "Render3d": "render3d/Render Node",
}
