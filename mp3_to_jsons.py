import whisper
import json
import os

model = whisper.load_model("medium", device= "cuda")

audios = os.listdir("audios")

for audio in audios:
    if(("_") in audio):
        name = os.path.splitext(audio)[0]
        number = name.split("_")[0]
        title = name.split("_", 1)[1].replace("_", " ")

        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}",
        # result = model.transcribe(audio = "audios/sample.mp3",
                                language = "hi",
                                task = "translate",
                                word_timestamps=False)

        chunks = []
        for segment in result["segments"]:
            chunks.append({"number":number, "title":title, "start":segment["start"], "end":segment["end"], "text":segment["text"]})

        chunks_with_metadata = {"chunks":chunks, "text":result["text"]}

        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata, f)