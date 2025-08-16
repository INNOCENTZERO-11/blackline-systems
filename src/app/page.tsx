import Image from "next/image";
import Hero from "./components/Hero";

export default function Home() {
  return (
        <>
      <Hero title="Blackline Systems" subtitle="Secure tools & reliable downloads" />
      <section className="max-w-4xl mx-auto p-6 text-slate-300">
        <p>Welcome — this is Day 1 scaffold. Continue building tools, admin and downloads next.</p>
      </section>
    </>
  );
}