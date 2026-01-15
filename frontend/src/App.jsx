import React, { useState, useEffect } from 'react';
import Chat from './components/Chat';
import Ingest from './components/Ingest';
import { Database, Activity, Loader2 } from 'lucide-react';
import api from './api';
import { ThemeProvider } from './context/ThemeContext';
import ThemeToggle from './components/ThemeToggle';
import './App.css'; 

function App() {
  const [status, setStatus] = useState({
    mongodb: 'Checking...',
    faiss_index: 'Checking...'
  });
  const [loadingStatus, setLoadingStatus] = useState(true);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await api.get('/system-status');
        setStatus(response.data);
      } catch (error) {
        console.error("Failed to fetch system status", error);
        setStatus({ mongodb: 'Error', faiss_index: 'Error' });
      } finally {
        setLoadingStatus(false);
      }
    };

    fetchStatus();
    
    const interval = setInterval(fetchStatus, 30000);
    return () => clearInterval(interval);
  }, []);

  const getStatusColor = (currentStatus) => {
    if (currentStatus === 'Connected' || currentStatus === 'Active') return 'text-emerald-700 bg-emerald-50 border-emerald-100';
    if (currentStatus === 'Checking...') return 'text-slate-600 bg-slate-50 border-slate-100';
    return 'text-red-700 bg-red-50 border-red-100';
  };

  return (
    <ThemeProvider>
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-50 font-sans transition-colors duration-200">
      
      <header className="sticky top-0 z-20 bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 transition-colors duration-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-white dark:bg-slate-800 p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
               <Database size={18} className="text-brand-600 dark:text-brand-400" />
            </div>
            <h1 className="text-base font-semibold text-slate-900 dark:text-slate-50 tracking-tight">
              Customer Support <span className="text-slate-500 dark:text-slate-400 font-normal">Knowledge Base Assistant</span>
            </h1>
          </div>
          <ThemeToggle />
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6 h-[calc(100vh-3.5rem)]">
        
        <div className="lg:col-span-3 space-y-4 flex flex-col h-full overflow-hidden">
          <div className="bg-white dark:bg-slate-900 p-4 rounded-xl shadow-sm border border-slate-200 dark:border-slate-800 flex flex-col gap-3 transition-colors duration-200">
             <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
                <h3 className="font-medium text-slate-900 dark:text-slate-100 text-sm flex items-center gap-2">
                  <Activity size={14} className="text-slate-400 dark:text-slate-500" />
                  System Status
                </h3>
                {loadingStatus ? (
                  <Loader2 size={12} className="animate-spin text-slate-400" />
                ) : (
                  <span className="flex h-2 w-2 relative">
                     <span className={`relative inline-flex rounded-full h-2 w-2 ${status.mongodb === 'Connected' ? 'bg-emerald-500' : 'bg-red-500'}`}></span>
                  </span>
                )}
             </div>
             
             <div className="space-y-2">
               <div className="flex items-center justify-between text-xs">
                 <span className="text-slate-500 dark:text-slate-400">FAISS Index</span>
                 <span className={`px-2 py-0.5 rounded-md text-xs font-medium border ${getStatusColor(status.faiss_index)}`}>
                    {status.faiss_index}
                 </span>
               </div>
               <div className="flex items-center justify-between text-xs">
                 <span className="text-slate-500 dark:text-slate-400">MongoDB</span>
                 <span className={`px-2 py-0.5 rounded-md text-xs font-medium border ${getStatusColor(status.mongodb)}`}>
                    {status.mongodb}
                 </span>
               </div>
             </div>
          </div>
          
          <Ingest />
        </div>

        <div className="lg:col-span-9 h-[600px] lg:h-full">
            <Chat />
        </div>
      </main>
    </div>
    </ThemeProvider>
  );
}

export default App;
