import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';

interface Telemetry {
  timestamp: string;
  voltage: number;
  current: number;
  temperature: number;
  soc: number;
}

const TelemetryChart: React.FC<{ data: Telemetry[] }> = ({ data }) => (
  <LineChart width={800} height={300} data={data}>
    <CartesianGrid strokeDasharray="3 3" />
    <XAxis dataKey="timestamp" />
    <YAxis yAxisId="left" />
    <YAxis yAxisId="right" orientation="right" />
    <Tooltip />
    <Legend />
    <Line yAxisId="left" type="monotone" dataKey="voltage" stroke="#8884d8" />
    <Line yAxisId="left" type="monotone" dataKey="current" stroke="#82ca9d" />
    <Line yAxisId="right" type="monotone" dataKey="temperature" stroke="#ff7300" />
    <Line yAxisId="right" type="monotone" dataKey="soc" stroke="#387908" />
  </LineChart>
);

export default TelemetryChart;
