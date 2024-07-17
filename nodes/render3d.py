class Render3d:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "url": ("STRING", {"multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"

    CATEGORY = "render3d"

    def exec(self, url):
        return {"ui": {"text": url}, "result": (url,)}





