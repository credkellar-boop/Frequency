'use client';
import { useEffect, useRef } from 'react';
import WaveSurfer from 'wavesurfer.js';
import { useAudioStore } from '@/store/useAudioStore';

export default function Waveform({ url }: { url: string }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const wavesurfer = useRef<WaveSurfer | null>(null);
  const { setIsPlaying, setCurrentTime, setDuration } = useAudioStore();

  useEffect(() => {
    if (!containerRef.current) return;

    wavesurfer.current = WaveSurfer.create({
      container: containerRef.current,
      waveColor: '#4F4A85',
      progressColor: '#3B4FD8',
      height: 128,
      url: url,
    });

    wavesurfer.current.on('ready', () => setDuration(wavesurfer.current!.getDuration()));
    wavesurfer.current.on('play', () => setIsPlaying(true));
    wavesurfer.current.on('pause', () => setIsPlaying(false));
    wavesurfer.current.on('timeupdate', (time) => setCurrentTime(time));

    return () => wavesurfer.current?.destroy();
  }, [url]);

  return <div ref={containerRef} className="w-full h-32 bg-gray-900 rounded-lg" />;
}
