import pygame
import os
class MusicPlayer:
    def __init__(self, music_dir='music'):
        self.music_dir = music_dir
        self.playlist = self._load_songs()
        self.current_index = 0
        self.is_playing = False
        self.is_paused = False

        self.start_pos = 0 
        if self.playlist:
            self._load_current_track()
    def _load_songs(self):
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir)
        return sorted([f for f in os.listdir(self.music_dir) if f.endswith(('.mp3', '.wav'))])
    def _load_current_track(self):
        track_path = os.path.join(self.music_dir, self.playlist[self.current_index])
        pygame.mixer.music.load(track_path)
        self.start_pos = 0 
    def play(self):
        if self.playlist:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
                self.is_playing = True
            elif not self.is_playing:
                pygame.mixer.music.play(start=self.start_pos)
                self.is_playing = True
    def pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.is_playing = False
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.start_pos = 0 
    def next(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self._stop_and_reload()
    def prev(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self._stop_and_reload()
    def _stop_and_reload(self):
        self.stop()
        self._load_current_track()
        self.play()
    def get_current_track_name(self):
        if self.playlist:
            return self.playlist[self.current_index]
        return "No tracks found"
    def get_pos_ms(self):
        if not self.is_playing and not self.is_paused:
            return 0
        return pygame.mixer.music.get_pos() + (self.start_pos * 1000)