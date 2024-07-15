class AssetImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"

    CATEGORY = "assets"

    def notify(self, text):
        return {"ui": {"text": text}, "result": (text,)}





