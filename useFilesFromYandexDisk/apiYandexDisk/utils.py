# File type detection function
def get_file_type(file_name: str) -> str:
    extension: str = file_name.split(".")[-1].lower()
    # Images
    if extension in ["jpg", "jpeg", "png", "gif", "bmp", "tiff"]:
        return "image"
    # Documents
    elif extension in ["pdf", "doc", "docx", "txt", "odt", "xls", "xlsx", "ppt", "pptx"]:
        return "document"
    # Archives
    elif extension in ["zip", "rar", "7z", "tar", "gz"]:
        return "archive"
    # Media files
    elif extension in ["mp3", "wav", "aac", "flac", "mp4", "mkv", "avi", "mov"]:
        return "media"
    # Executable files
    elif extension in ["exe", "msi", "bat", "sh", "bin"]:
        return "executable"
    # Other file types
    return "other"