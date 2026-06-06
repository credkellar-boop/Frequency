import subprocess
import os
from pathlib import Path

def separate_audio(input_file: str, output_dir: str = "data/stems"):
    """
    Uses Demucs to separate audio into stems.
    Requires demucs to be installed: pip install demucs
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Command to run Demucs
    # -n htdemucs: Use the high-quality hybrid model
    # -o: Output directory
    # --mp3: Saves space (remove if you want lossless WAV)
    cmd = [
        "python3", "-m", "demucs.separate",
        "-n", "htdemucs",
        "-o", output_dir,
        input_file
    ]
    
    print(f"--- 🎼🌐Frequency: Separating {input_file} ---")
    
    try:
        # Run the command and wait for completion
        process = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Separation complete!")
        return output_dir
    except subprocess.CalledProcessError as e:
        print(f"Error during separation: {e.stderr}")
        return None

# Example usage:
# if __name__ == "__main__":
#     separate_audio("data/uploads/my_song.mp3")
