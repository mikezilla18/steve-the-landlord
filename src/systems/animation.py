import pygame

class Animation:
    def __init__(self, frames, fps=12):
        self.frames = frames
        self.fps = fps
        self.current_frame = 0
        self.last_update = 0
        
    def update(self, dt):
        # Advance animation based on frame rate
        if dt - self.last_update > 1000/self.fps:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = dt
            
    def current_image(self):
        return self.frames[self.current_frame]