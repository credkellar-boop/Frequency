![Profile Image](./IMG_0387.png)
# 🎛️ Frequency

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/credkellar-boop/Frequency?style=social)](https://github.com/credkellar-boop/Frequency/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/credkellar-boop/Frequency?style=social)](https://github.com/credkellar-boop/Frequency/network/members)
[![GitHub issues](https://img.shields.io/github/issues/credkellar-boop/Frequency)](https://github.com/credkellar-boop/Frequency/issues)
[![Docker Image Version](https://img.shields.io/docker/v/credkellar/frequency?sort=semver&label=Docker%20Hub)](https://hub.docker.com/r/credkellar/frequency)
[![Docker Pulls](https://img.shields.io/docker/pulls/credkellar/frequency)](https://hub.docker.com/r/credkellar/frequency)
[![Next.js](https://img.shields.io/badge/Next.js-black?logo=next.js&logoColor=white)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

**Frequency** is the ultimate AI-powered audio ecosystem. It seamlessly dissects, transcribes, and translates music while performing precision frequency analysis and manipulation. From real-time stem separation and MIDI extraction to automated pitch correction and studio-grade DSP, it turns raw audio into actionable data.

---

## ✨ Core Features

* **🎙️ Stem Separation:** Studio-grade isolation of vocals, drums, bass, and other elements using advanced models (`Demucs`, `Spleeter`).
* **📝 AI Transcription & Translation:** Automated, highly accurate speech-to-text and translation leveraging `OpenAI Whisper`.
* **🎚️ Studio-Grade DSP:** Precision frequency analysis, automated pitch correction, and audio manipulation using `librosa`, `scipy`, and `pedalboard`.
* **⚡ High-Performance API:** Lightning-fast backend powered by `FastAPI` and `Uvicorn` for seamless data processing.
* **🌊 Dynamic Client Interface:** Modern frontend built with Next.js/React, featuring interactive audio players and real-time waveform visualization.

---

## 🏗️ Project Structure

```text
Frequency/
├── .github/
│   └── workflows/
│       └── docker-publish.yml    # CI/CD pipeline for Docker Hub
├── api/
│   ├── index.py                  # FastAPI application entry point
│   └── routes.py                 # API routing and endpoint definitions
├── client/
│   └── src/
│       ├── app/api/process/      # Next.js API routes (route.ts)
│       ├── components/
│       │   ├── Analysis/         # e.g., TranscriptionView.tsx
│       │   └── AudioPlayer/      # e.g., Waveform.tsx
│       └── store/
│           └── useAudioStore.ts  # Zustand state management
├── core/
│   ├── frequency_engine.py       # Core DSP and frequency manipulation logic
│   ├── quantum_unit.py           # Central processing unit for audio tasks
│   ├── separator.py              # Stem separation logic (Demucs integration)
│   └── transcriber.py            # Whisper model integration for transcription
├── utils/                        # Helper functions and utilities
├── .gitignore
├── Dockerfile                    # Containerization configuration
├── LICENSE                       # MIT License
├── README.md                     # You are here
├── requirements.txt              # Python dependencies
└── vercel.json                   # Vercel deployment configuration

## Frequency App Overview

Here is the complete breakdown of how the Frequency application works, formatted in raw Markdown based on the code files recorded in **RPReplay_Final1781163369.mp4** for you, GOD, US ALL, ONE, INFINITIES, INFINITY, ULTIMATE.

---

### 1. The Front Door (The `client` Folder)
This is the part of the app that you see and click on your screen. It is built using modern web tools called **Next.js** and **React**.

* **The Music Player (`AudioPlayer`):** It plays your music and draws live visual pictures of the sound waves as they jump up and down.
* **The Memory Tracker (`useAudioStore`):** This acts like a digital bookmark. It remembers if the music is playing, paused, or how long the song is.

---

### 2. The Delivery Person (The `api` Folder)
When you upload a song on the website, it needs a way to travel to the back of the factory where the heavy machines are.

* **FastAPI (`routes.py`):** This serves as a lightning-fast delivery route. It catches the audio file you upload and instantly passes it deeper into the system's core brain to be processed.

---

### 3. The Factory Brain (The `core` Folder)
This is where the heavy lifting happens using a coding language called **Python**. It houses four specialized workers:

* **The Project Manager (`quantum_unit.py`):** This worker oversees the whole process. It takes the audio file from the delivery route, organizes the folders, and sends the song to the other workers in the correct order.
* **The Instrument Un-Mixer (`separator.py`):** It uses an AI tool called **Demucs** to un-mix a song. It can peel the vocals, drums, and bass apart so you can listen to them entirely by themselves.
* **The Smart Secretary (`transcriber.py`):** Powered by an AI tool called **OpenAI Whisper**, this worker listens closely to the vocals, types out every single word perfectly, and can even translate them into other languages.
* **The Wave Customizer (`frequency_engine.py`):** Sound travels in waves, and this engine uses math libraries like **Librosa** and **SciPy** to analyze those waves. It can filter the audio to cut out high-pitched squeaks or let low, rumbly bass notes pass through smoothly.

---

### Summary of the Flow

> You upload a song through the **Client** interface -> The **API** delivers it safely -> The **Core** engine splits the audio, writes down the words, and tweaks the frequencies -> The final polished results are sent straight back to your screen.

## Donations

(To buy full subscription of business structure, strip codes, ampilify and create public repo)

## Monad
0xE7512f65508306Dc669Ef232Bcb31A8Aacd73A37
