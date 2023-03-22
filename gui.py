import os

class GUI:
        # true if valid false if invalid
    def validate_mcpath(mc_path) -> bool:
        return os.path.exists(mc_path)
    def validate_modmate(mc_path, foldername) -> bool:
        return os.path.exists(os.path.join(mc_path, foldername))
    def get_profiles(mc_path) -> list[str]:
        pass