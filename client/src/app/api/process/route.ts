import { NextResponse } from 'next/server';

const BACKEND_URL = process.env.PYTHON_BACKEND_URL || 'http://localhost:8000';

export async function POST(request: Request) {
  try {
    const formData = await request.formData();

    // Forward the file/data to the Python FastAPI engine
    const response = await fetch(`${BACKEND_URL}/process/`, {
      method: 'POST',
      body: formData, // Forwards the audio file directly
    });

    const data = await response.json();
    
    return NextResponse.json(data);
  } catch (error) {
    console.error('Proxy Error:', error);
    return NextResponse.json(
      { error: 'Failed to communicate with the frequency engine' },
      { status: 500 }
    );
  }
}
const BACKEND_URL = process.env.PYTHON_BACKEND_URL || 'https://[YOUR_RUNPOD_URL]';
