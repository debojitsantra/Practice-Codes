import tkinter as tk
from tkinter import font
import threading
import time
import pygame


TOTAL_SESSIONS = 4
WORK_DURATION = 1
SHORT_BREAK = 1
LONG_BREAK = 2
SESSION_SOUND = "session_end.mp3"
BREAK_SOUND = "break_end.mp3"


BG_COLOR = "#FFF0F5"
FG_COLOR = "#A05283"
FONT_NAME = "Comic Sans MS"
PROGRESS_COLOR = "#FF69B4"
PROGRESS_BG = "#FFDDEE"


pygame.mixer.init()

def play_sound(sound_file):
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Sound error: {e}")

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Cute Pomodoro Timer ")
        self.root.config(bg=BG_COLOR, padx=20, pady=30)

        self.session_count = 0
        self.running = False

        self.title_label = tk.Label(root, text="Pomodoro Time!", font=(FONT_NAME, 18, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        self.title_label.pack(pady=20)

        self.canvas = tk.Canvas(root, width=220, height=220, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack()
        self.arc_bg = self.canvas.create_oval(10, 10, 210, 210, width=10, outline=PROGRESS_BG)
        self.arc_fill = self.canvas.create_arc(10, 10, 210, 210, width=15, style='arc', outline=PROGRESS_COLOR, extent=0)
        self.timer_text = self.canvas.create_text(110, 110, text="00:00", font=(FONT_NAME, 14), fill=FG_COLOR)

        self.status_label = tk.Label(root, text="Ready to focus?", font=(FONT_NAME, 16), bg=BG_COLOR, fg=FG_COLOR)
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", font=(FONT_NAME, 14), bg="#FFC0CB", fg="black", command=self.start)
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", font=(FONT_NAME, 12), bg="#FFDDEE", fg="black", command=self.reset)
        self.reset_button.pack()

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run_sessions, daemon=True).start()

    def reset(self):
        self.running = False
        self.session_count = 0
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.canvas.itemconfig(self.arc_fill, extent=0)
        self.status_label.config(text="Reset done. Ready to go again!")

    def run_sessions(self):
        for i in range(TOTAL_SESSIONS):
            if not self.running:
                break
            self.session_count += 1
            self.status_label.config(text=f"Focus Time! Session {self.session_count}")
            self.countdown(WORK_DURATION * 60)
            if not self.running:
                break
            play_sound(SESSION_SOUND)

            if self.session_count % 4 == 0 and self.session_count != TOTAL_SESSIONS:
                self.status_label.config(text="💤 Long Break!")
                self.countdown(LONG_BREAK * 60)
                play_sound(BREAK_SOUND)
            elif self.session_count != TOTAL_SESSIONS:
                self.status_label.config(text="Short Break!")
                self.countdown(SHORT_BREAK * 60)
                play_sound(BREAK_SOUND)

        if self.running:
            self.status_label.config(text="Done! You're a productivity star!")
        self.running = False

    def countdown(self, total_seconds):
        start = time.time()
        while self.running:
            elapsed = int(time.time() - start)
            remaining = total_seconds - elapsed
            if remaining < 0:
                break

            mins, secs = divmod(remaining, 60)
            self.canvas.itemconfig(self.timer_text, text=f"{mins:02d}:{secs:02d}")

            percent = 360 * (elapsed / total_seconds)
            self.canvas.itemconfig(self.arc_fill, extent=percent)

            self.root.update()
            time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()