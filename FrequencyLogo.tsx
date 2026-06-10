'use client';

import { motion } from 'framer-motion';

export default function FrequencyLogo() {
  return (
    <div className="relative flex flex-col items-center justify-center w-full py-32 bg-black overflow-hidden">
      
      {/* Ambient Background Core Glow */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.5 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 2, ease: "easeOut" }}
        className="absolute w-[600px] h-[150px] bg-cyan-600/15 blur-[100px] rounded-[100%]" 
      />

      {/* Main Cinematic Text */}
      <motion.h1
        initial={{ opacity: 0, y: 30, filter: 'blur(12px)' }}
        animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
        transition={{ duration: 1.5, ease: 'easeOut', delay: 0.2 }}
        className="relative z-10 text-6xl md:text-8xl font-black uppercase tracking-[0.25em] text-transparent bg-clip-text bg-gradient-to-r from-zinc-400 via-cyan-100 to-zinc-500 text-center ml-[0.25em]"
      >
        Frequency
      </motion.h1>

      {/* Technical Data Stream / Subtitle Overlay */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 2, delay: 1.5 }}
        className="relative z-10 mt-6 flex items-center gap-3"
      >
        <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" />
        <span className="text-cyan-400/60 text-xs md:text-sm tracking-[0.4em] font-mono uppercase">
          Node Active
        </span>
        <span className="w-12 h-[1px] bg-gradient-to-r from-cyan-400/60 to-transparent" />
      </motion.div>
      
    </div>
  );
}
