import { create } from 'zustand';

interface AudioState {
  isPlaying: boolean;
  currentTime: number;
  duration: number;
  metadata: { bpm: number; key: string } | null;
  
  // Actions
  setIsPlaying: (playing: boolean) => void;
  setCurrentTime: (time: number) => void;
  setDuration: (duration: number) => void;
  setMetadata: (data: { bpm: number; key: string }) => void;
}

export const useAudioStore = create<AudioState>((set) => ({
  isPlaying: false,
  currentTime: 0,
  duration: 0,
  metadata: null,
  
  setIsPlaying: (playing) => set({ isPlaying: playing }),
  setCurrentTime: (time) => set({ currentTime: time }),
  setDuration: (duration) => set({ duration }),
  setMetadata: (data) => set({ metadata: data }),
}));
