import React from 'react';
import Chat from './components/Chat';
import Ingest from './components/Ingest';
import { Database, MessageSquare } from 'lucide-react';
import './App.css'; 

function App() {
  return (
    <div className="min-h-screen bg-slate-100 text-slate-900 font-sans">
      
      <header className="bg-white border-b border-slate-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="bg-blue-600 text-white p-2 rounded-lg">
              <Database size={20} />
            </div>
            <h1 className="text-lg font-bold text-slate-800">Knowledge Base Assistant</h1>
          </div>
          <nav className="hidden md:flex gap-6">
            <a href="#" className="flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-blue-600">
               Dashboard
            </a>
            <a href="#" className="flex items-center gap-2 text-sm font-medium text-slate-600 hover:text-blue-600">
               Settings
            </a>
          </nav>
        </div>
      </header>

     
      <main className="max-w-7xl mx-auto px-4 py-8 grid grid-cols-1 md:grid-cols-12 gap-8 h-[calc(100vh-4rem)]">
        
        
        <div className="md:col-span-4 lg:col-span-3 space-y-6">
          <Ingest />
          
          <div className="bg-white p-6 rounded-lg shadow-sm border border-slate-200">
            <h3 className="font-semibold text-slate-800 mb-2">System Status</h3>
            <div className="flex items-center gap-2 text-sm text-green-600">
              <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
              Operational
            </div>
             <p className="text-xs text-slate-400 mt-2">FAISS Index: Active<br/>MongoDB: Connected</p>
          </div>
        </div>

        
        <div className="md:col-span-8 lg:col-span-9 h-[600px] md:h-full">
            <Chat />
        </div>
      </main>
    </div>
  );
}

export default App;
