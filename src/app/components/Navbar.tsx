// components/Navbar.tsx
"use client";
import Link from "next/link";

export default function Navbar(){
  return (
    <nav className="flex items-center justify-between px-6 py-4">
      <div className="flex items-center gap-3">
        <img src="/images/logo.png" alt="Blackline Systems" className="h-10 w-10 object-contain" />
        <span className="font-semibold text-lg text-slate-100">Blackline Systems</span>
      </div>
      <div className="flex items-center gap-3">
        <Link href="/tools" className="text-sm text-slate-300 hover:text-white">Tools</Link>
        <Link href="/admin" className="text-sm px-3 py-1 border rounded-md text-slate-200">Admin</Link>
      </div>
    </nav>
  );
}
