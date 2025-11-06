"""Video generation with overlays and audio."""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
try:
    # MoviePy 2.x imports
    from moviepy import ImageClip, AudioFileClip, CompositeVideoClip, TextClip, concatenate_videoclips
except ImportError:
    # MoviePy 1.x fallback
    from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, TextClip, concatenate_videoclips
import config

def create_background_image(width=1920, height=1080):
    """Create a beautiful gradient background image."""
    # Create gradient from warm orange to soft blue (sunrise colors)
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Create sunrise gradient
    for y in range(height):
        # Interpolate between colors
        ratio = y / height

        # Morning colors: warm orange/pink to light blue
        r = int(255 * (1 - ratio) + 135 * ratio)
        g = int(180 * (1 - ratio) + 206 * ratio)
        b = int(100 * (1 - ratio) + 235 * ratio)

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img

def create_text_overlay(text, position='center', fontsize=60, color='white', bg_color=None):
    """Create a text overlay clip."""
    try:
        txt_clip = TextClip(
            text,
            fontsize=fontsize,
            color=color,
            font='Arial-Bold',
            method='caption',
            size=(1600, None),
            align='center'
        ).set_position(position)

        return txt_clip
    except Exception as e:
        print(f"Error creating text overlay: {e}")
        return None

def split_text_for_display(text, max_chars=200):
    """Split long text into multiple screens."""
    if len(text) <= max_chars:
        return [text]

    # Split by sentences or newlines
    parts = []
    current = ""

    sentences = text.replace('\n', '. ').split('. ')

    for sentence in sentences:
        if len(current) + len(sentence) < max_chars:
            current += sentence + ". "
        else:
            if current:
                parts.append(current.strip())
            current = sentence + ". "

    if current:
        parts.append(current.strip())

    return parts if parts else [text]

def create_video(motivation, agenda_text, prayer, audio_path, output_path=None):
    """Create the complete morning motivation video."""
    try:
        print("Creating video...")

        # Set output path
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(config.OUTPUT_DIR, f"morning_video_{timestamp}.mp4")

        # Get audio duration
        audio = AudioFileClip(audio_path)
        duration = audio.duration

        # Create background
        bg_image = create_background_image(config.VIDEO_WIDTH, config.VIDEO_HEIGHT)
        bg_path = os.path.join(config.OUTPUT_DIR, "temp_bg.png")
        bg_image.save(bg_path)

        # Create video clip from background
        bg_clip = ImageClip(bg_path).set_duration(duration)

        # Create text content
        today = datetime.now().strftime("%A, %B %d, %Y")

        # Split duration into sections
        section_duration = duration / 4  # 4 sections: intro, motivation, agenda, prayer

        text_clips = []

        # Section 1: Greeting
        greeting_text = f"GOOD MORNING!\n\n{today}"
        txt1 = create_text_overlay(greeting_text, 'center', 70, 'white')
        if txt1:
            txt1 = txt1.set_start(0).set_duration(section_duration)
            text_clips.append(txt1)

        # Section 2: Motivation
        motivation_text = f"MOTIVATION\n\n{motivation}"
        txt2 = create_text_overlay(motivation_text, 'center', 50, 'white')
        if txt2:
            txt2 = txt2.set_start(section_duration).set_duration(section_duration)
            text_clips.append(txt2)

        # Section 3: Agenda
        if agenda_text and agenda_text.strip():
            # Clean agenda text for display
            agenda_display = agenda_text.replace("TODAY'S AGENDA:", "").strip()
            agenda_formatted = f"TODAY'S AGENDA\n\n{agenda_display}"
            txt3 = create_text_overlay(agenda_formatted, 'center', 45, 'white')
            if txt3:
                txt3 = txt3.set_start(section_duration * 2).set_duration(section_duration)
                text_clips.append(txt3)

        # Section 4: Prayer
        prayer_text = f"{prayer['name'].upper()}\n\n{prayer['text'][:200]}"
        txt4 = create_text_overlay(prayer_text, 'center', 40, 'white')
        if txt4:
            txt4 = txt4.set_start(section_duration * 3).set_duration(section_duration)
            text_clips.append(txt4)

        # Composite video
        if text_clips:
            video = CompositeVideoClip([bg_clip] + text_clips)
        else:
            video = bg_clip

        # Add audio
        video = video.set_audio(audio)

        # Write video file
        print("Rendering video (this may take a minute)...")
        video.write_videofile(
            output_path,
            fps=config.VIDEO_FPS,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile=os.path.join(config.OUTPUT_DIR, 'temp-audio.m4a'),
            remove_temp=True,
            logger=None
        )

        # Cleanup
        audio.close()
        video.close()
        if os.path.exists(bg_path):
            os.remove(bg_path)

        print(f"✓ Video created: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error creating video: {e}")
        import traceback
        traceback.print_exc()
        return None
