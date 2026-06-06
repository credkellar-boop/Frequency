# requirements.txt
demucs
spleeter
openai-whisper
librosa
scipy
pedalboard
pyrubberband
pydub
numpy
fastapi
uvicorn

Frequency/
├── api/
│   ├── index.py
│   └── routes.py
├── core/
│   ├── quantum_unit.py
│   ├── separator.py
│   ├── transcriber.py
│   └── frequency_engine.py
├── utils/
│   ├── dsp_modifiers.py
│   └── file_handler.py
├── data/
│   ├── uploads/
│   ├── stems/
│   └── outputs/
├── requirements.txt
├── vercel.json
└── .gitignore
