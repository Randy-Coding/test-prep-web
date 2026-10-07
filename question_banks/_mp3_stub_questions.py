"""Open-response questions for the public MP3 homework stubs.

The excerpts were reviewed against the supplied student source and are stored
with the bank for static builds. The instructor-provided codec and private
helpers are outside this set.
"""

import re

from question_banks._mp3_source_excerpts import EXCERPTS

# file, function, parameter roles, short answer, explanation, revealing lines.
# These are the public functions declared by the homework headers and defined
# in student source. Later helper declarations with no matching source function
# are deliberately absent.
_STUBS = [
    ("util.c", "read_u32_be", "buf: four bytes in network (big-endian) order", "Combines four bytes into one unsigned 32-bit big-endian integer.", "It shifts successive bytes by 24, 16, 8, and 0 bits and ORs them. The helper lets ID3v2.3 frame parsing interpret a stored length; a null pointer returns zero in this implementation.", ("<< 24", "return result")),
    ("util.c", "read_u32_syncsafe", "buf: four bytes of a synchsafe integer", "Decodes a four-byte synchsafe unsigned integer.", "It masks off each byte's high bit and shifts the seven-bit payloads by 21, 14, 7, and 0 bits. ID3v2 tag size and ID3v2.4 frame size use this representation; a null pointer returns zero here.", ("0x7F", "return result")),
    ("util.c", "util_read_file", "path: file to read; out_data: resulting owned byte buffer; out_size: byte count", "Reads an entire binary file into allocated memory and returns its bytes and size through output pointers.", "It opens in binary mode, seeks to determine length, allocates a buffer, rewinds, reads the bytes, and returns 0 on success or -1 on failure. The caller owns the returned buffer and must free it.", ("fopen(path", "ftell", "malloc", "fread", "*out_data")),
    ("util.c", "util_write_file", "path: output filename; data: bytes to write; size: byte count", "Writes the supplied bytes to a binary output file.", "It opens the path in binary write mode, writes exactly the requested count, checks the close, and returns 0 or -1. The edit functions use it to save the tag-plus-new-audio buffer.", ("fopen(path", "fwrite", "fclose", "return 0")),
    ("mp3_sections.c", "mp3_mpeg_version_str", "version: encoded MPEG version field", "Maps a version field to a human-readable MPEG version label.", "The code selects MPEG 1, 2, or 2.5 for the supported bit patterns and labels other values reserved. The returned pointer refers to a string literal and is not caller-owned.", ("version == 3", "version == 2", "version == 0", "return \"reserved\"")),
    ("mp3_sections.c", "mp3_layer_str", "layer: encoded MPEG layer field", "Maps a layer field to a readable layer name.", "Layer values 1, 2, and 3 are rendered as Layer III, II, and I respectively; the other value is reserved. The caller uses the returned constant text when printing a parsed header.", ("layer == 1", "layer == 2", "layer == 3", "return \"reserved\"")),
    ("mp3_sections.c", "mp3_channel_mode_str", "mode: encoded channel-mode field", "Maps the two-bit channel-mode value to its label.", "The code distinguishes Stereo, Joint Stereo, Dual Channel, and Mono. It returns constant text for display, not a newly allocated string.", ("mode == 0", "mode == 1", "mode == 2", "mode == 3")),
    ("mp3_sections.c", "mp3_emphasis_str", "emphasis: encoded emphasis field", "Maps the emphasis field to a readable label.", "The implementation recognizes none, 50/15 ms, and CCIT J.17; the remaining encoded value is labeled reserved. This is display conversion for a parsed MPEG header.", ("emphasis == 0", "emphasis== 1", "emphasis == 2", "emphasis == 3")),
    ("mp3_sections.c", "mp3_is_sync", "buf: bytes at a possible MPEG frame start", "Tests whether the first 11 MPEG sync bits are set.", "It requires first byte 0xFF and the top three bits of the second byte to be ones, returning 1 or 0. This is only a candidate check: the complete header parser must still reject invalid version, layer, or rate fields.", ("0xFF", "0xE0")),
    ("mp3_sections.c", "mp3_parse_frame_header", "buf: four header bytes; out: decoded frame-header structure", "Validates and decodes an MPEG Layer III frame header, including frame size.", "After the sync check it extracts fields with masks and shifts, rejects reserved version/layer/rate indexes, uses version-dependent bitrate and sample-rate tables, and computes the byte length with coefficient 144 or 72 plus padding. Success fills out and returns 0; failure returns -1.", ("mp3_is_sync", "int version", "bitrate_index", "sample_rate_index", "frame_coeff", "out->frame_size", "return 0")),
    ("mp3_id3.c", "mp3_has_id3v2", "data: file bytes; size: available byte count", "Checks for an ID3 marker at the beginning of a file.", "This implementation tests for at least three bytes and compares the first three with ID3, returning 1 when present and 0 otherwise. It is a signature test, not validation of the full tag length.", ("size >=3", "data[0]", "return 1", "return 0")),
    ("mp3_id3.c", "mp3_has_id3v1", "data: file bytes; size: available byte count", "Checks for a trailing 128-byte ID3v1 tag.", "The first three bytes of the last 128-byte region must spell TAG. It returns 1 for that marker and 0 when absent or too short, allowing the audio-end logic to exclude the suffix.", ("size >=128", "size - 128", "return 1", "return 0")),
    ("mp3_id3.c", "mp3_id3v2_total_size", "data: file bytes; size: available byte count", "Computes the total byte span of a leading ID3v2 tag.", "When the ID3 marker and ten-byte header are present, it decodes the four synchsafe size bytes at offsets 6–9 and adds the ten-byte header. This implementation returns zero when absent and does not itself confirm that the declared total fits the file.", ("size < 10", "mp3_has_id3v2", "tag_size", "return 10 + tag_size")),
    ("mp3_id3.c", "mp3_id3v1_offset", "data: file bytes; size: available byte count", "Finds the starting byte offset of a trailing ID3v1 tag.", "If the last 128 bytes begin with TAG, the function returns size minus 128. In this supplied implementation it returns zero when no tag is found; callers that need the audio end use mp3_mpeg_audio_end to substitute the full file size.", ("mp3_has_id3v1", "size -128", "return 0")),
    ("mp3_id3.c", "mp3_mpeg_audio_start", "data: file bytes; size: available byte count", "Returns the starting byte offset of the MPEG region.", "It delegates to the leading ID3v2 total-size function, so audio starts just after that tag when present and at offset zero otherwise. This is a byte offset, not a PCM time or sample index.", ("mp3_id3v2_total_size",)),
    ("mp3_id3.c", "mp3_mpeg_audio_end", "data: file bytes; size: available byte count", "Returns the exclusive ending byte offset of the MPEG region.", "When a trailing ID3v1 marker exists it returns the tag's starting offset; otherwise it returns the file size. Together with the audio start, it lets callers pass only compressed MPEG bytes to the codec.", ("mp3_has_id3v1", "mp3_id3v1_offset", "return size")),
    ("mp3_id3.c", "mp3_extract_metadata", "filename: MP3 path; out: metadata result to fill", "Extracts the available ID3v1 and ID3v2 metadata into one output structure.", "It reads the file, marks which tag generations are present, copies fixed-width ID3v1 fields, then walks ID3v2 frames using version-specific size decoding. It allocates a frame list and text values, returns 0 or -1, and makes the caller responsible for mp3_free_metadata after success.", ("util_read_file", "out->has_v1", "out->has_v2", "memcpy(out->v1.title", "read_u32_syncsafe", "extract_frame_value", "out->v2.frames")),
    ("mp3_id3.c", "mp3_free_metadata", "meta: metadata result whose owned ID3v2 values should be released", "Frees the allocated ID3v2 values and frame list in a metadata result.", "It loops over stored v2 frames to free each value, then frees the array. The fixed-size ID3v1 fields live inside the structure and need no separate free. The function has no return value and accepts a null pointer.", ("meta == NULL", "frame_count", "free(meta->v2.frames[i].value)", "free(meta->v2.frames)")),
    ("mp3_id3.c", "mp3_id3v1_genre_name", "genre: numeric ID3v1 genre code", "Looks up a display name for an ID3v1 genre code.", "The implementation indexes a fixed table for codes through 125 and returns Unknown outside that range. It returns a pointer to constant text; the caller must not free it.", ("static const char *genres", "genre <= 125", "return genres[genre]", "return \"Unknown\"")),
    ("mp3_reader.c", "mp3_open", "path: MP3 filename to open", "Opens an MP3 file as a binary input stream.", "It checks the path, calls fopen with rb, and returns the FILE pointer or NULL. Callers use the stream for raw header/section reading and close it afterward.", ("path == NULL", "fopen(path", "return fileptr")),
    ("mp3_reader.c", "mp3_summary", "filename: MP3 path; out_summary: resulting section array; out_count: number of sections", "Enumerates the file's ID3 and MPEG sections for the section-summary command.", "It opens the file, optionally records an ID3v2 header and frames, advances through MPEG frames by each parsed frame size, detects a trailing ID3v1 tag, and fills an allocated section array plus count. It returns 0 on success or -1 on failure; the caller releases the array with mp3_free_sections.", ("mp3_open(filename)", "read_u32_syncsafe", "\"ID3H\"", "\"ID3F\"", "mp3_parse_frame_header", "\"MPEG\"", "\"ID3V1\"", "*out_summary =")),
    ("mp3_reader.c", "mp3_extract_frame_header", "filename: MP3 path; out: first MPEG frame header result", "Finds and decodes the first MPEG frame header in a file.", "It opens the file, skips a leading ID3v2 tag when present, reads four MPEG header bytes, checks synchronization, and delegates field decoding to mp3_parse_frame_header. It reports status and fills out on success; it does not decode PCM audio.", ("mp3_open(filename)", "read_u32_syncsafe", "fseek(fileptr", "fread(mpeg_header", "mp3_is_sync", "mp3_parse_frame_header")),
    ("mp3_reader.c", "mp3_free_sections", "sections: owned section array; count: number of initialized sections", "Releases a section-summary array and its per-section payloads.", "Each section may own a data buffer, so the loop frees those before freeing the containing array. The function returns no value and accepts a null array.", ("sections != NULL", "i < count", "free(sections[i].data)", "free(sections)")),
    ("mp3_trim.c", "mp3_get_duration", "path: MP3 input file; out_seconds: computed duration", "Decodes an MP3's MPEG region and reports its audio duration in seconds.", "It reads the file, isolates audio bytes, decodes to interleaved PCM, divides sample_count by channel count to get time frames, then divides by sample rate. It frees file and PCM storage and returns 0 or -1; seconds are placed in the output pointer.", ("util_read_file", "mp3_mpeg_audio_start", "mp3_codec_decode", "sample_count", "*out_seconds", "mp3_codec_free_pcm")),
    ("mp3_trim.c", "mp3_get_loudest_timestamp", "path: MP3 input file; out_seconds: timestamp of the peak", "Reports the timestamp of the first loudest PCM frame.", "After decoding the MPEG region, it scans absolute sample magnitudes across channels. A strictly larger peak updates the saved sample index, so an equal later peak does not win. It converts that index to a PCM frame and then seconds, frees buffers, and returns status.", ("mp3_codec_decode", "abs(pcm_buffer.samples", "curr > temp", "loudest_frame", "*out_seconds")),
    ("mp3_trim.c", "mp3_trim_audio", "input_path: source MP3; start_sec/end_sec: half-open time range; output_path: destination", "Writes a new MP3 containing audio from the half-open interval [start_sec, end_sec).", "It decodes MPEG to PCM, truncates seconds times sample rate to frame indexes, copies the chosen interleaved samples, re-encodes, and writes original tag bytes around the new audio. Its integer return is a success/failure status, not a duration.", ("util_read_file", "mp3_codec_decode", "start_frame", "end_frame", "memcpy(trimmed_samples", "mp3_codec_encode", "util_write_file")),
    ("mp3_overlay.c", "mp3_overlay_audio", "base_path: original track; overlay_path: replacement clip; start_sec: insertion time; output_path: destination", "Writes an MP3 with overlay audio replacing the base audio from a chosen start time.", "It decodes both MPEG regions, computes the start in base PCM frames, resamples and converts the overlay to the base format, copies base audio before and after the replacement window, encodes the result, and preserves the base file's ID3 bytes. It returns 0 or -1.", ("util_read_file(base_path", "mp3_codec_decode", "base_start_frame", "resampled_frames", "resample_overlay", "prepare_audio_after_overlay", "mp3_codec_encode", "util_write_file")),
    ("main.c", "main", "argc: number of command-line arguments; argv: their strings", "Runs the MP3 command-line program and returns a process success or failure status.", "It first locates the input file and help request, then interprets requested flags and calls the relevant parsing, analysis, or editing functions. It prints results or errors using the provided macros and releases returned metadata or sections. Successful completion returns EXIT_SUCCESS; invalid input or a failed feature returns EXIT_FAILURE.", ("strcmp(argv[i], \"-f\")", "PRINT_USAGE", "mp3_extract_frame_header", "mp3_summary", "mp3_extract_metadata", "mp3_trim_audio", "mp3_overlay_audio", "return EXIT_SUCCESS")),
]


def _signature(source):
    return source[:source.index("{")].strip()


def _parameter_names(signature):
    inside = signature[signature.index("(") + 1:signature.rindex(")")]
    if inside.strip() == "void":
        return []
    return [re.search(r"[A-Za-z_]\w*$", item.strip()).group() for item in inside.split(",")]


def _rename_parameters(code, names):
    for index, name in enumerate(names, 1):
        code = re.sub(r"\b" + re.escape(name) + r"\b", f"arg{index}", code)
    return code


def build_questions():
    questions = {}
    for filename, name, parameters, purpose, mechanism, _clues in _STUBS:
        excerpt = EXCERPTS[name]
        signature = _signature(excerpt)
        names = _parameter_names(signature)
        source_path = f"cse320/MP3_HW/src/{filename}"
        header_path = f"cse320/MP3_HW/include/{filename[:-2]}.h"
        sources = [source_path, header_path] if filename != "main.c" else [source_path, "cse320/MP3_HW/README.md"]
        common = {"subcategory": "Professor stub", "sources": sources}

        obfuscated_name = re.sub(r"\b" + re.escape(name) + r"\b", "foo", excerpt)
        questions[f"What assigned function is shown as `foo`? Explain its purpose and result.\n```c\n{obfuscated_name}\n```"] = {
            **common,
            "answer": f"`{name}`. {purpose}",
            "explanation": mechanism,
        }

        obfuscated_parameters = _rename_parameters(excerpt, names)
        questions[f"In `{name}`, what does each obfuscated parameter represent, and what result does the function produce?\n```c\n{obfuscated_parameters}\n```"] = {
            **common,
            "answer": f"{parameters}. {purpose}",
            "explanation": mechanism,
        }

        questions[f"What does `{name}` do, and how does this implementation work?\nHeader:\n```c\n{signature};\n```\nImplementation excerpt:\n```c\n{excerpt}\n```"] = {
            **common,
            "answer": purpose,
            "explanation": mechanism,
        }
    return questions
