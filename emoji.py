def text_to_emoji(sentence):
    emoji_dict = {
        "love": "❤️",
        "pizza": "🍕",
        "cats": "🐱",
        "happy": "😊",
        "sad": "😢",
        "cool": "😎",
        "angry": "😠",
        "dog": "🐶",
        "fire": "🔥",
        "sun": "☀️",
        "moon": "🌙",
        "star": "⭐"
    }
    
    words = sentence.split()
    converted_words = [emoji_dict.get(word, word) for word in words]
    converted_sentence = ' '.join(converted_words)
    
    return converted_sentence

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print(text_to_emoji(user_input))
