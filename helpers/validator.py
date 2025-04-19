
import imghdr

def is_probably_decrypted(data):
    # Check for common file signatures (magic bytes)
    # PDF
    if data.startswith(b'%PDF'):
        return True
    # PNG
    if data.startswith(b'\x89PNG'):
        return True
    # ZIP (used by DOCX, XLSX, etc.)
    if data.startswith(b'PK\x03\x04'):
        return True
    # JPEG
    if data.startswith(b'\xFF\xD8'):
        return True
    # TXT (basic check for mostly printable characters)
    if sum(c > 31 and c < 127 or c in (10, 13) for c in data[:100]) > 80:
        return True
    # Check for known image types
    try:
        if imghdr.what(None, h=data):
            return True
    except:
        pass
    return False
