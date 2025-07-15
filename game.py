import random as r
import time as t
import speech

levels = {
"facil": ["casa", "café", "perro"],
"intermedio": ["ordenador", "odontólogo", "programador"],
"dificil": ["otorrinolaringologo", "ácido desoxirribunocleico", "inteligencia artificial"]
}
def play_game(level):
    words = levels.get(level, [])
    if not words:
        print("Nivel no válido. Por favor, elige entre 'facil', 'intermedio' o 'dificil'.")
        return
    
    score = 0
    attempts = 3
    
    print(f"Nivel seleccionado: {level}. Tienes {attempts} intentos para pronunciar la palabra.")
    while attempts > 0 and words:
        word = r.choice(words)
        print(f"Pronuncia esta palabra: {word}")
        t.sleep(2)
        try:
            rec_word = speech.speech_es()
            rec_word = rec_word.lower()
            print(f"Has pronunciado: {rec_word}")
        except Exception as e:
            print(f"Error al reconocer la palabra: {e}")
            continue
        if rec_word == word:
            print("¡Correcto!")
            score += 1
            words.remove(word)
        else:
            print(f"Incorrecto. La palabra era: {word}")
            attempts -= 1
            if attempts == 0:
                print("Has perdido. No te rindas, ¡inténtalo de nuevo!")
                return
        t.sleep(2)
    print(f"¡Juego terminado! Tu puntuación final es: {score}/{len(levels[level])}")
    
select_level = input("Selecciona un nivel (facil, intermedio, dificil): ").lower()
play_game(select_level)