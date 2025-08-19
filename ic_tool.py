import gzip, zlib, brotli, json, sys, os

def decode_ic(file_in, file_out):
    with open(file_in, "rb") as f:
        data = f.read()

    decoded = None
    method = None

    # Try gzip
    try:
        decoded = gzip.decompress(data).decode("utf-8")
        method = "gzip"
    except:
        pass

    # Try zlib
    if decoded is None:
        try:
            decoded = zlib.decompress(data).decode("utf-8")
            method = "zlib"
        except:
            pass

    # Try brotli
    if decoded is None:
        try:
            decoded = brotli.decompress(data).decode("utf-8")
            method = "brotli"
        except:
            pass

    if decoded is None:
        print("[-] Could not decode with gzip, zlib, or brotli.")
        return None

    # Try pretty-print JSON
    try:
        parsed = json.loads(decoded)
        with open(file_out, "w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=4, ensure_ascii=False)
        print(f"[+] Decoded with {method} and saved as {file_out}")
    except:
        with open(file_out, "w", encoding="utf-8") as f:
            f.write(decoded)
        print(f"[!] Decoded with {method}, but not JSON. Saved raw text to {file_out}")

    return method


def encode_ic(file_in, file_out, method):
    with open(file_in, "r", encoding="utf-8") as f:
        text = f.read()

    # If JSON, compact it
    try:
        parsed = json.loads(text)
        text = json.dumps(parsed, separators=(",", ":"))
    except:
        pass

    text_bytes = text.encode("utf-8")

    if method == "gzip":
        data = gzip.compress(text_bytes)
    elif method == "zlib":
        data = zlib.compress(text_bytes)
    elif method == "brotli":
        data = brotli.compress(text_bytes)
    else:
        print("[-] Unknown method, cannot encode.")
        return

    with open(file_out, "wb") as f:
        f.write(data)

    print(f"[+] Re-encoded as {file_out} using {method}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Decode: python ic_tool.py save.ic save.json")
        print("  Encode: python ic_tool.py save.json save.ic --encode <method>")
        sys.exit(1)

    file_in = sys.argv[1]
    file_out = sys.argv[2]

    if "--encode" in sys.argv:
        idx = sys.argv.index("--encode")
        method = sys.argv[idx + 1]
        encode_ic(file_in, file_out, method)
    else:
        method = decode_ic(file_in, file_out)
        if method:
            print(f"To re-encode after editing: python ic_tool.py {file_out} new_save.ic --encode {method}")
