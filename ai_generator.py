"""AI-powered content generation for morning motivation."""
import random
from datetime import datetime
import config

def generate_motivation():
    """Generate motivational content using AI or fallback quotes."""

    # Try AI generation first
    if config.AI_PROVIDER == 'anthropic':
        try:
            from anthropic import Anthropic
            client = Anthropic(api_key=config.ANTHROPIC_API_KEY)

            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=200,
                messages=[{
                    "role": "user",
                    "content": "Generate a brief, powerful motivational message for someone starting their day. Keep it under 50 words. Make it inspiring, actionable, and positive. Focus on themes like purpose, strength, gratitude, or growth."
                }]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"AI generation failed: {e}")

    elif config.AI_PROVIDER == 'openai':
        try:
            from openai import OpenAI
            client = OpenAI(api_key=config.OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[{
                    "role": "user",
                    "content": "Generate a brief, powerful motivational message for someone starting their day. Keep it under 50 words. Make it inspiring, actionable, and positive. Focus on themes like purpose, strength, gratitude, or growth."
                }]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"AI generation failed: {e}")

    # Fallback to curated quotes if AI is not available
    fallback_quotes = [
        "Today is a gift. Embrace it with courage and joy. You have the strength within you to overcome any challenge and make a positive impact.",
        "This is your day to shine. Let your faith guide you, your hope inspire you, and your love transform the world around you.",
        "Each morning brings new opportunities. Trust in God's plan, believe in yourself, and take bold action toward your dreams.",
        "You are capable of incredible things. Start this day with gratitude, move through it with purpose, and end it with peace.",
        "Today, choose to be a light in someone's darkness. Your kindness, your smile, your presence matters more than you know.",
        "Wake up with determination. Go to bed with satisfaction. Today is your canvas - paint it with colors of faith, hope, and love.",
        "God has given you this day for a reason. Use it wisely, love deeply, serve generously, and trust completely in His guidance.",
        "You are stronger than your struggles, braver than your fears, and more blessed than you realize. Make today count!",
    ]

    return random.choice(fallback_quotes)

def get_greeting():
    """Get time-appropriate greeting."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"
