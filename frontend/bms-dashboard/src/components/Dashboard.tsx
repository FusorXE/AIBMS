import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TelemetryChart from './TelemetryChart';

interface Telemetry {
  timestamp: string;
  voltage: number;
  current: number;
  temperature: number;
  soc: number;
}

const Dashboard: React.FC = () => {
  const [data, setData] = useState<Telemetry[]>([]);

  useEffect(() => {
    // Placeholder: fetch latest telemetry
    const fake = Array.from({ length: 10 }).map((_, i) => ({
      timestamp: new Date(Date.now() - i * 60000).toISOString(),
      voltage: Math.random() * 50 + 300,
      current: Math.random() * 10 + 20,
      temperature: Math.random() * 10 + 25,
      soc: Math.random() * 20 + 80,
    }));
    setData(fake.reverse());
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-xl font-semibold mb-2">Telemetry</h1>
      <TelemetryChart data={data} />
    </div>
  );
};

export default Dashboard;
