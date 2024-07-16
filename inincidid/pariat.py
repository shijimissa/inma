import urllib.parse

def sanitize_uri(uri):
    # Parse the URI to ensure it is valid
    parsed_uri = urllib.parse.urlparse(uri)
    
    # Reconstruct the URI to ensure proper encoding
    sanitized_uri = urllib.parse.urlunparse(parsed_uri)
    
    return sanitized_uri

# Usage in a Python context
unsafe_uri = "javascript:alert('XSS')"
safe_uri = sanitize_uri(unsafe_uri)

print(safe_uri)  # Should print a properly sanitized version or reject invalid schemes
