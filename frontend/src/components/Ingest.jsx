import React, { useState } from 'react';
import { Upload, FileText, CheckCircle, AlertCircle, Loader2 } from 'lucide-react';
import api from '../api';

const Ingest = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('idle'); 
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setStatus('idle');
      setMessage('');
    }
  };

  const handleUpload = async () => {
    if (!file) return;

    setStatus('uploading');
    const formData = new FormData();
    formData.append('file', file);

    try {
      await api.post('/ingest', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setStatus('success');
      setMessage('Document ingested successfully!');
      setFile(null);
    } catch (error) {
      console.error('Upload error:', error);
      setStatus('error');
      setMessage(error.response?.data?.detail || 'Failed to upload document.');
    }
  };

  return (
    <div className="bg-white dark:bg-slate-900 p-6 rounded-lg shadow-sm border border-slate-200 dark:border-slate-800 transition-colors duration-200">
      <h2 className="text-xl font-semibold text-slate-800 dark:text-slate-100 mb-4 flex items-center gap-2">
        <Upload size={20} />
        Add Knowledge
      </h2>
      
      <div className="border-2 border-dashed border-slate-300 dark:border-slate-700 rounded-lg p-8 text-center hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors">
        <input
          type="file"
          id="file-upload"
          className="hidden"
          onChange={handleFileChange}
          accept=".pdf,.docx,.txt"
        />
        <label
          htmlFor="file-upload"
          className="cursor-pointer flex flex-col items-center justify-center gap-2"
        >
          <div className="bg-blue-100 dark:bg-blue-900/40 text-blue-600 dark:text-blue-400 p-3 rounded-full">
            <FileText size={24} />
          </div>
          <span className="text-slate-600 dark:text-slate-400 font-medium">
            {file ? file.name : 'Click to select a file (PDF, DOCX, TXT)'}
          </span>
          <span className="text-xs text-slate-400 dark:text-slate-500">Max size 10MB</span>
        </label>
      </div>

      {status === 'uploading' && (
        <div className="mt-4 flex items-center gap-2 text-blue-600 bg-blue-50 p-3 rounded-md">
          <Loader2 className="animate-spin" size={18} />
          <span className="text-sm font-medium">Processing document...</span>
        </div>
      )}

      {status === 'success' && (
        <div className="mt-4 flex items-center gap-2 text-green-600 bg-green-50 p-3 rounded-md">
          <CheckCircle size={18} />
          <span className="text-sm font-medium">{message}</span>
        </div>
      )}

      {status === 'error' && (
        <div className="mt-4 flex items-center gap-2 text-red-600 bg-red-50 p-3 rounded-md">
          <AlertCircle size={18} />
          <span className="text-sm font-medium">{message}</span>
        </div>
      )}

      <button
        onClick={handleUpload}
        disabled={!file || status === 'uploading'}
        className="w-full mt-6 py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        Upload Document
      </button>
    </div>
  );
};

export default Ingest;
