import streamlit as st
import datetime

# --- Configuration ---
CHARS_PER_BLOCK = 500
WORDS_MIN_BLOCK = 80
WORDS_MAX_BLOCK = 100
BLOCK_DURATION = 30  # seconds
GAP_BETWEEN_BLOCKS = 10  # seconds
GAP_BETWEEN_SCRIPTS = 60  # seconds

# --- SRT Utilities ---
def format_time(seconds):
    time = datetime.timedelta(seconds=seconds)
    time_str = str(time)
    if '.' not in time_str:
        time_str += '.000000'
    hours, minutes, sec_ms = time_str.split(':')
    secs, ms = sec_ms.split('.')
    return f"{int(hours):02}:{int(minutes):02}:{int(secs):02},{int(ms[:3]):03}"

def format_srt_block(index, start_time, text):
    end_time = start_time + BLOCK_DURATION
    return f"{index}\n{format_time(start_time)} --> {format_time(end_time)}\n{text.strip()}\n\n"

def convert_to_srt(scripts):
    srt_output = ''
    index = 1
    total_time = 0

    for i, script in enumerate(scripts):
        words = script.strip().split()
        current_block = ''
        words_in_block = 0

        for word in words:
            if len(current_block) + len(word) <= CHARS_PER_BLOCK and words_in_block < WORDS_MAX_BLOCK:
                current_block += word + ' '
                words_in_block += 1
            else:
                # Try breaking at the last period
                last_period = current_block.rfind('.')
                if last_period != -1 and last_period != len(current_block) - 1:
                    leftover = current_block[last_period + 1:].strip()
                    current_block = current_block[:last_period + 1]
                    srt_output += format_srt_block(index, total_time, current_block)
                    index += 1
                    total_time += BLOCK_DURATION + GAP_BETWEEN_BLOCKS
                    current_block = leftover + ' ' + word + ' '
                    words_in_block = len(current_block.strip().split())
                else:
                    srt_output += format_srt_block(index, total_time, current_block)
                    index += 1
                    total_time += BLOCK_DURATION + GAP_BETWEEN_BLOCKS
                    current_block = word + ' '
                    words_in_block = 1

        if current_block.strip():
            srt_output += format_srt_block(index, total_time, current_block)
            index += 1
            total_time += BLOCK_DURATION + GAP_BETWEEN_BLOCKS

        # Add a longer gap between scripts
        if i < len(scripts) - 1:
            total_time += GAP_BETWEEN_SCRIPTS - GAP_BETWEEN_BLOCKS

    return srt_output.strip()

# --- Streamlit UI ---
st.set_page_config(page_title="Multi-Script to SRT Converter", layout="centered")
st.title("Multi-Script to SRT Converter")

st.markdown("Paste your scripts below. Click **'Add Script'** to add more script boxes. When done, click **'Generate SRT'**.")

if 'script_boxes' not in st.session_state:
    st.session_state.script_boxes = ['']

# Add or remove scripts
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Add Script"):
        st.session_state.script_boxes.append('')
with col2:
    if st.button("🗑️ Clear All"):
        st.session_state.script_boxes = ['']

# Text areas for all scripts
scripts = []
for i in range(len(st.session_state.script_boxes)):
    script = st.text_area(f"Script {i+1}", st.session_state.script_boxes[i], key=f'script_{i}')
    scripts.append(script)

# Generate SRT
if st.button("🚀 Generate SRT"):
    non_empty_scripts = [s for s in scripts if s.strip()]
    if non_empty_scripts:
        srt_result = convert_to_srt(non_empty_scripts)
        st.text_area("Generated SRT", srt_result, height=300)
        st.download_button("📥 Download .srt file", srt_result, file_name="subtitles.srt", mime="text/plain")
    else:
        st.warning("Please paste at least one script before generating.")
