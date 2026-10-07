"""Reviewed excerpts from the supplied MP3_HW/src implementations.

These are stored with the bank because MP3_HW is a local ignored directory and
is unavailable to the static-site builder after checkout.
"""

EXCERPTS = {
    "main": """int main(int argc, char **argv)
{
    const char *file = NULL;
    /* ... */
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0) {
            help = 1;
    /* ... */
            file = argv[i + 1];
    /* ... */
    if (help) {
        PRINT_USAGE(argv[0]);
    /* ... */
        if (mp3_extract_frame_header(file, &header)!= 0){
    /* ... */
        if (mp3_trim_audio(file, start, end, output) != 0) {
    /* ... */
    return EXIT_SUCCESS;
}""",
    "mp3_mpeg_version_str": "const char *mp3_mpeg_version_str(int version)\n{\n    if (version == 3) {\n        return \"MPEG 1\";\n    } else if (version == 2){\n        return \"MPEG 2\";\n    } else if (version == 0) {\n        return \"MPEG 2.5\";\n    }\n    return \"reserved\";\n}",
    "mp3_layer_str": "const char *mp3_layer_str(int layer)\n{\n    if (layer == 1) {\n        return \"Layer III\";\n    } else if (layer == 2){\n        return \"Layer II\";\n    } else if (layer == 3) {\n        return \"Layer I\";\n    }\n    return \"reserved\";\n}",
    "mp3_channel_mode_str": "const char *mp3_channel_mode_str(int mode)\n{\n    if (mode == 0) {\n        return \"Stereo\";\n    } else if (mode == 1) {\n        return \"Joint Stereo\";\n    } else if (mode == 2) {\n        return \"Dual Channel\";\n    } else if (mode == 3) {\n        return \"Mono\";\n    }\n    return \"reserved\";\n}",
    "mp3_emphasis_str": "const char *mp3_emphasis_str(int emphasis)\n{\n    if (emphasis == 0) {\n        return \"none\";\n    } else if (emphasis== 1) {\n        return \"50/15 ms\";\n    } else if (emphasis == 2) {\n        return \"reserved\";\n    } else if (emphasis == 3) {\n        return \"CCIT J.17\";\n    }\n    return \"reserved\";\n}",
    "mp3_is_sync": "int mp3_is_sync(const uint8_t *buf)\n{\n    if (buf == NULL) {return 0;}\n    if (buf[0] == 0xFF && (buf[1] & 0xE0) == 0xE0) {return 1;} else\n    return 0;\n}",
    "mp3_parse_frame_header": "int mp3_parse_frame_header(const uint8_t *buf, mp3_frame_header_t *out)\n{\n    /* ... */\n    if (!mp3_is_sync(buf)) {return -1;}\n    int version = (buf[1] & 0x18) >> 3;\n    /* ... */\n    int bitrate_index = (buf[2] & 0xF0) >> 4;\n    /* ... */\n    int sample_rate_index = (buf[2] & 0x0C) >> 2;\n    /* ... */\n    int frame_coeff;\n    /* ... */\n    out->frame_size = (frame_coeff * out->bitrate_kbps *1000) / out->sample_rate_hz + out->padding;\n    /* ... */\n    return 0;\n}",
    "mp3_has_id3v2": "int mp3_has_id3v2(const uint8_t *data, size_t size)\n{\n    if (data != NULL && size >=3) {\n        if (data[0] == 0x49 && data[1] == 0x44 && data[2] == 0x33) {\n            return 1;\n        }\n    }\n    return 0;\n}",
    "mp3_has_id3v1": "int mp3_has_id3v1(const uint8_t *data, size_t size)\n{\n    if (data != NULL && size >=128) {\n        if (data[size - 128] == 0x54 && data[size - 127] == 0x41 && data[size - 126] == 0x47) {\n            return 1;\n        }\n    }\n    return 0;\n}",
    "mp3_id3v2_total_size": "size_t mp3_id3v2_total_size(const uint8_t *data, size_t size)\n{\n    if (data == NULL || size < 10) {\n        return 0;\n    }\n    if (mp3_has_id3v2(data, size)) {\n        uint32_t tag_size = ((data[6] & 0x7F) << 21) | ((data[7] & 0x7F)<< 14) | ((data[8] & 0x7F) << 7) | (data[9] & 0x7F);\n        return 10 + tag_size;\n    }\n    return 0;\n}",
    "mp3_id3v1_offset": "size_t mp3_id3v1_offset(const uint8_t *data, size_t size)\n{\n    if (mp3_has_id3v1(data, size)) {\n        return size -128;\n    }\n    return 0;\n}",
    "mp3_mpeg_audio_start": "size_t mp3_mpeg_audio_start(const uint8_t *data, size_t size)\n{\n    return mp3_id3v2_total_size(data, size);\n}",
    "mp3_mpeg_audio_end": "size_t mp3_mpeg_audio_end(const uint8_t *data, size_t size)\n{\n    if (mp3_has_id3v1(data, size)) {\n        return mp3_id3v1_offset(data, size);\n    }\n    return size;\n}",
    "mp3_extract_metadata": "int mp3_extract_metadata(const char *filename, mp3_metadata_t *out)\n{\n    /* ... */\n    if (util_read_file(filename, &data, &size) != 0) {\n    /* ... */\n    out->has_v1 = mp3_has_id3v1(data, size);\n    out->has_v2 = mp3_has_id3v2(data, size) && size >= 10;\n    /* ... */\n        memcpy(out->v1.title, data + start + 3, 30);\n    /* ... */\n                frame_size = read_u32_syncsafe(data + pos + 4);\n    /* ... */\n            frames[frame_count].value = extract_frame_value(frames[frame_count].frame_id, data + pos + 10, frame_size);\n    /* ... */\n        out->v2.frames = frames;\n    /* ... */\n    return 0;\n}",
    "mp3_free_metadata": "void mp3_free_metadata(mp3_metadata_t *meta)\n{\n    if (meta == NULL) {return;}\n    for (size_t i = 0; i < meta->v2.frame_count; i++) {\n            free(meta->v2.frames[i].value);\n        }\n        free(meta->v2.frames);\n}",
    "mp3_id3v1_genre_name": "const char *mp3_id3v1_genre_name(uint8_t genre)\n{\n    static const char *genres[] = {\n    /* ... */\n    if (genre <= 125) {\n        return genres[genre];\n    /* ... */\n    return \"Unknown\";\n}",
    "mp3_open": "FILE *mp3_open(const char *path)\n{\n    if (path == NULL) {return NULL;}\n    FILE *fileptr = fopen(path, \"rb\");\n    if (fileptr == NULL) {return NULL;} else return fileptr;\n}",
    "mp3_summary": "int mp3_summary(const char *filename, mp3_section_t **out_summary, size_t *out_count)\n{\n    /* ... */\n    FILE *fileptr = mp3_open(filename);\n    /* ... */\n        uint32_t tag_size = read_u32_syncsafe(header + 6);\n    /* ... */\n        strcpy(section[0].type, \"ID3H\");\n    /* ... */\n            strcpy(section[section_index].type, \"ID3F\");\n    /* ... */\n                if (mp3_parse_frame_header(mpeg_header, &header) == 0) {\n    /* ... */\n                    strcpy(section[section_index].type, \"MPEG\");\n    /* ... */\n                    strcpy(section[section_index].type, \"ID3V1\");\n    /* ... */\n        *out_summary = section;\n    /* ... */\n        return 0;\n}",
    "mp3_extract_frame_header": "int mp3_extract_frame_header(const char *filename, mp3_frame_header_t *out)\n{\n    /* ... */\n    FILE *fileptr = mp3_open(filename);\n    /* ... */\n        uint32_t tag_size = read_u32_syncsafe(header + 6);\n        if (fseek(fileptr, 10 + tag_size, SEEK_SET) != 0) {\n    /* ... */\n    size_t  mpeg_header_read = fread(mpeg_header, 1, 4, fileptr);\n    /* ... */\n    if (!mp3_is_sync(mpeg_header)) {\n    /* ... */\n    return mp3_parse_frame_header(mpeg_header, out);\n}",
    "mp3_free_sections": "void mp3_free_sections(mp3_section_t *sections, size_t count)\n{\n    if (sections != NULL) {\n        for (size_t i = 0; i < count; i++) {\n            free(sections[i].data);\n        }\n        free(sections);\n    }\n}",
    "mp3_get_duration": "int mp3_get_duration(const char *path, double *out_seconds)\n{\n    /* ... */\n    if (util_read_file(path, &data, &size) != 0) {\n    /* ... */\n    size_t start = mp3_mpeg_audio_start(data, size);\n    /* ... */\n    if (mp3_codec_decode(data + start, end - start, &pcm_buffer) != 0){\n    /* ... */\n        mp3_codec_free_pcm(&pcm_buffer);\n    /* ... */\n    size_t total_frames = pcm_buffer.sample_count / pcm_buffer.channels;\n    /* ... */\n    return 0;\n}",
    "mp3_get_loudest_timestamp": "int mp3_get_loudest_timestamp(const char *path, double *out_seconds)\n{\n    /* ... */\n    if (mp3_codec_decode(data + start, end - start, &pcm_buffer) != 0){\n    /* ... */\n        int curr = abs(pcm_buffer.samples[i]);\n        if (curr > temp) {\n    /* ... */\n    size_t loudest_frame = loudest/pcm_buffer.channels;\n    /* ... */\n    return 0;\n}",
    "mp3_trim_audio": "int mp3_trim_audio(const char *input_path, double start_sec, double end_sec,\n                   const char *output_path)\n{\n    /* ... */\n    if (util_read_file(input_path, &data, &size) != 0) {\n    /* ... */\n    if (mp3_codec_decode(data + start, end - start, &pcm_buffer) != 0){\n    /* ... */\n    size_t start_frame = (size_t)(start_sec  * pcm_buffer.sample_rate_hz);\n    size_t end_frame = (size_t)(end_sec * pcm_buffer.sample_rate_hz);\n    /* ... */\n    memcpy(trimmed_samples, pcm_buffer.samples + (start_frame * pcm_buffer.channels),(trimmed * sizeof(int16_t)));\n    /* ... */\n    int result = mp3_codec_encode(&pcm, &encoded, &encoded_size);\n    /* ... */\n    result = util_write_file(output_path, final, final_size);\n    /* ... */\n    return result;\n}",
    "mp3_overlay_audio": "int mp3_overlay_audio(const char *base_path, const char *overlay_path, double start_sec,\n                      const char *output_path)\n{\n    /* ... */\n    if (util_read_file(base_path, &base_data, &base_size) != 0) {\n    /* ... */\n    if (mp3_codec_decode(base_data + base_start, base_end - base_start, &base_pcm) != 0){\n    /* ... */\n    size_t base_start_frame = (size_t)(start_sec  * base_pcm.sample_rate_hz);\n    /* ... */\n    size_t resampled_frames = (size_t)(overlay_total_frame * ratio);\n    /* ... */\n    resample_overlay(&overlay_pcm, &base_pcm, final,base_start_frame, resampled_frames, ratio);\n    prepare_audio_after_overlay(&base_pcm, final, overlay_end_frame, base_total_frame);\n    /* ... */\n    int result = mp3_codec_encode(&final_pcm, &encoded, &encoded_size);\n    /* ... */\n    result = util_write_file(output_path, output, final_size);\n    /* ... */\n    return result;\n}",
}
