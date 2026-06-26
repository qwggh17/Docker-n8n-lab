items = _items

binary = items[0]["binary"]["data"]
text = binary["data"]

sentences = []

for sentence in text.split("."):
    sentence = sentence.strip()
    if sentence:
        sentences.append(sentence)

result = "\n\n".join(sentences)

return [{
    "json": {
        "status": "done",
        "sentences": len(sentences)
    },
    "binary": {
        "data": {
            "data": result.encode("utf-8").decode("latin1"),
            "fileName": "out.doc",
            "mimeType": "text/plain"
        }
    }
}]
