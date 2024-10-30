import tkinter as tk
from tkinter import filedialog, messagebox
import os
import deepl
import pyttsx3  # Para síntese de fala offline
import threading

class TranscriptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leitor de Transcrições de Legendas")
        self.root.geometry("500x600")
        
        self.phrases_en = []
        self.current_index = -1
        self.difficult_phrases = []
        self.reviewing_difficult = False
        self.translation_shown = False

        self.auth_key = "2463055e-7d10-42de-b9fb-d423570c3363:fx"
        self.translator = deepl.Translator(self.auth_key)

        # Inicializar o pyttsx3 para áudio
        self.engine = pyttsx3.init()

        # Configurar a voz para "Microsoft Zira Desktop - English (United States)"
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
        
        # Ajustar a velocidade da fala (rate)
        self.engine.setProperty('rate', 150)  # 150 é um valor típico, ajuste conforme necessário
        
        font_size = int(14 * 1.35)
        self.label = tk.Label(root, text="", wraplength=450, justify="left", font=("Arial", font_size))
        self.label.pack(pady=20)

        self.translation_label = tk.Label(root, text="", wraplength=450, justify="left", font=("Arial", font_size), fg="blue")
        self.translation_label.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        button_color = "#ADD8E6"
        button_width = int(10 * 1.4)
        button_height = int(2 * 1.4)

        self.prev_button = tk.Button(button_frame, text="Frase Anterior", command=self.show_previous_phrase, bg=button_color, width=button_width, height=button_height)
        self.prev_button.grid(row=0, column=0, padx=10, pady=5)

        self.next_button = tk.Button(button_frame, text="Próxima Frase", command=self.show_next_phrase, bg=button_color, width=button_width, height=button_height)
        self.next_button.grid(row=0, column=1, padx=10, pady=5)

        self.show_translation_button = tk.Button(button_frame, text="Mostrar Tradução", command=self.show_translation, bg=button_color, width=button_width, height=button_height)
        self.show_translation_button.grid(row=0, column=2, padx=10, pady=5)

        self.load_button = tk.Button(root, text="Carregar Legendas", command=self.load_phrases, bg=button_color, width=button_width, height=button_height)
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(root, text="Reproduzir Áudio", command=self.play_audio_threaded, bg=button_color, width=button_width, height=button_height)
        self.play_button.pack(pady=5)

        self.mark_difficult_button = tk.Button(root, text="Marcar Frase Difícil", command=self.mark_as_difficult, bg=button_color, width=button_width, height=button_height)
        self.mark_difficult_button.pack(pady=5)

        self.review_difficult_button = tk.Button(root, text="Rever Frases Difíceis", command=self.review_difficult_phrases, bg=button_color, width=button_width, height=button_height)
        self.review_difficult_button.pack(pady=5)

        self.progress_label = tk.Label(root, text="Frase 0 de 0", font=("Arial", int(12 * 1.35)))
        self.progress_label.pack(pady=10)

        self.load_phrases()

    def load_phrases(self):
        file_path_en = filedialog.askopenfilename(title="Selecione o arquivo de legendas em inglês", filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")))
        
        if file_path_en:
            with open(file_path_en, 'r', encoding='utf-8') as file_en:
                self.phrases_en = file_en.read().splitlines()
                self.current_index = -1
                self.update_progress_label()
                self.show_next_phrase()

    def show_previous_phrase(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_phrase()

    def show_next_phrase(self):
        if self.current_index < len(self.phrases_en) - 1:
            self.current_index += 1
            self.display_phrase()

    def display_phrase(self):
        phrase = self.phrases_en[self.current_index]
        self.label.config(text=phrase)
        self.translation_label.config(text="")
        self.translation_shown = False
        self.update_progress_label()
        self.play_audio_threaded()  # Reproduzir áudio automaticamente ao mudar de frase

    def show_translation(self):
        if not self.translation_shown:
            phrase = self.phrases_en[self.current_index]
            translated_phrase = self.translator.translate_text(phrase, target_lang="PT-BR")
            self.translation_label.config(text=translated_phrase.text)
            self.translation_shown = True

    def play_audio_threaded(self):
        threading.Thread(target=self.play_audio).start()

    def play_audio(self):
        if self.phrases_en and self.current_index >= 0:
            phrase = self.phrases_en[self.current_index]

            # Usando pyttsx3 para falar o texto diretamente com a voz selecionada
            self.engine.say(phrase)
            self.engine.runAndWait()

    def mark_as_difficult(self):
        if self.phrases_en and self.current_index >= 0:
            phrase = self.phrases_en[self.current_index]
            if phrase not in self.difficult_phrases:
                self.difficult_phrases.append(phrase)
                messagebox.showinfo("Frase Marcada", "Frase marcada como difícil.")

    def review_difficult_phrases(self):
        if self.difficult_phrases:
            self.phrases_en = self.difficult_phrases
            self.current_index = -1
            self.reviewing_difficult = True
            self.show_next_phrase()
        else:
            messagebox.showinfo("Nenhuma Frase Difícil", "Nenhuma frase difícil marcada.")

    def update_progress_label(self):
        total_phrases = len(self.phrases_en)
        self.progress_label.config(text=f"Frase {self.current_index + 1} de {total_phrases}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranscriptionApp(root)
    root.mainloop()
