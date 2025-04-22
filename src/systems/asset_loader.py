import os
import pygame
import random  # <-- Add this at the top

class AssetLoader:
    # ... rest of the file remains the same ...
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_loader()
        return cls._instance
    
    def _init_loader(self):
        self.assets = {}
        self.base_path = os.path.dirname(os.path.dirname(__file__))  # Points to src/
        
    def load(self, category, filename, scale=None):
        """Loads an image with transparent background"""
        key = f"{category}/{filename}"
        try:
            path = os.path.join(self.base_path, "..", "assets", category, filename)
            img = pygame.image.load(path).convert_alpha()  # Preserves transparency
            if scale:
                img = pygame.transform.scale(img, scale)
            self.assets[key] = img
            return img
        except Exception as e:
            print(f"⚠️ Asset Error: {key} - {str(e)}")
            # Create colorful placeholder
            surf = pygame.Surface((50, 50), pygame.SRCALPHA)
            surf.fill((random.randint(50, 200), random.randint(50, 200), random.randint(50, 200), 128))
            return surf

# Global instance
loader = AssetLoader()
