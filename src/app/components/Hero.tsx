// components/Hero.tsx
"use client";
import { motion } from "framer-motion";

export default function Hero({ title = "Blackline Systems", subtitle = "Secure tools. Simple downloads." }: { title?:string; subtitle?:string }) {
  return (
    <section className="min-h-[60vh] flex items-center justify-center px-6">
      <motion.div
        initial={{ opacity:0, y:20 }}
        animate={{ opacity:1, y:0 }}
        transition={{ duration:0.6 }}
        className="max-w-4xl text-center bg-overlay p-8 rounded-2xl"
      >
        <h1 className="text-4xl md:text-6xl font-bold text-white">{title}</h1>
        <p className="mt-4 text-lg text-slate-300">{subtitle}</p>
      </motion.div>
    </section>
  );
}
