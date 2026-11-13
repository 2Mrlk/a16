export interface Plant {
  id: string;
  name: string;
  scientificName: string;
  category: string;
  lightRequirement: 'Sol Pleno' | 'Meia Sombra' | 'Luz Difusa / Sombra';
  location: string;
  waterIntervalDays: number;
  fertilizeIntervalDays: number;
  lastWateredDate: string; // ISO string
  lastFertilizedDate: string; // ISO string
  notes?: string;
  imageEmoji: string;
}

export type FilterType = 'all' | 'needs-water' | 'needs-fertilizer' | 'healthy';
