'use client';
import { useAudioStore } from '@/store/useAudioStore';

export default function TranscriptionView({ segments }: { segments: any[] }) {
  const currentTime = useAudioStore((state) => state.currentTime);

  return (
    <div className="p-6 overflow-y-auto h-[400px] border border-gray-800 rounded-xl bg-black text-gray-400">
      {segments.map((segment, index) => {
        // Highlight if the current time falls within this segment's window
        const isActive = currentTime >= segment.start && currentTime <= segment.end;
        
        return (
          <p 
            key={index} 
            className={`mb-4 transition-colors duration-300 ${
              isActive ? 'text-white font-semibold text-lg' : 'text-gray-500'
            }`}
          >
            {segment.text}
          </p>
        );
      })}
    </div>
  );
}
