import asyncio
from google.cloud import vision

client = vision.ImageAnnotatorClient()

async def analyze_image_and_find_movie(image_bytes: bytes) -> str:
    return await asyncio.to_thread(_vision_analysis, image_bytes)

def _vision_analysis(image_bytes: bytes) -> str:
    try:
        image = vision.Image(content=image_bytes)
        
        # Виконуємо пошук в інтернеті(WEB DETECTION)
        response = client.web_detection(image=image)
        data = response.web_detection

        # --- ДЕБАГ (ДЛЯ МЕНЕ В ТЕРМІНАЛІ) ---
        print("\n--- GOOGLE VISION ВІДПОВІДЬ ---")
        if data.best_guess_labels:
            print(f"Best Guess: {data.best_guess_labels[0].label}")
        print(f"Entities: {[e.description for e in data.web_entities[:3]]}")
        # ------------------------------------

        results = []

        # 1. Найкраща здогадка (Best Guess)
        if data.best_guess_labels:
            guess = data.best_guess_labels[0].label
            results.append(f" Моя здогадка: {guess}")

        # 2. Ключові сутності (Entities) - шукаємо назви з великої літери
        if data.web_entities:
            # Беремо перші 5 тегів, які не є порожніми
            tags = [e.description for e in data.web_entities if e.description][:5]
            if tags:
                results.append(f"Теги: {', '.join(tags)}")

        # 3. Заголовки сторінок (Pages) - ТУТ ЧАСТО ХОВАЄТЬСЯ НАЗВА
        if data.pages_with_matching_images:
            # Беремо заголовки перших 3 сайтів, де знайшлося це фото
            sites = []
            for page in data.pages_with_matching_images[:3]:
                if page.page_title:
                    sites.append(f"• {page.page_title}")
            
            if sites:
                results.append("Знайдено на сайтах:**\n" + "\n".join(sites))

        if not results:
            return "🤷‍♂️ ШІ проаналізував фото, але не знайшов точних збігів у базі даних фільмів."

        return "\n\n".join(results)

    except Exception as e:
        print(f"ПОМИЛКА API: {e}")
        return "Сталася помилка при зверненні до Google."