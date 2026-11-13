import { Plant } from './types';

const today = new Date();
const daysAgo = (days: number) => {
  const d = new Date(today);
  d.setDate(d.getDate() - days);
  return d.toISOString();
};

export const INITIAL_PLANTS: Plant[] = [
  {
    id: '1',
    name: 'Costela-de-Adão',
    scientificName: 'Monstera Deliciosa',
    category: 'Folhagem Tropical',
    lightRequirement: 'Meia Sombra',
    location: 'Sala de Estar',
    waterIntervalDays: 4,
    fertilizeIntervalDays: 30,
    lastWateredDate: daysAgo(4), // Regar hoje!
    lastFertilizedDate: daysAgo(15),
    notes: 'Borrifar água nas folhas nos dias secos e limpar a poeira.',
    imageEmoji: '🌿',
  },
  {
    id: '2',
    name: 'Jiboia Dourada',
    scientificName: 'Epipremnum aureum',
    category: 'Trepadeira / Pendente',
    lightRequirement: 'Luz Difusa / Sombra',
    location: 'Estante do Quarto',
    waterIntervalDays: 5,
    fertilizeIntervalDays: 20,
    lastWateredDate: daysAgo(2), // 3 dias restantes
    lastFertilizedDate: daysAgo(21), // Adubar hoje!
    notes: 'Tolera ambientes internos e ajuda a purificar o ar.',
    imageEmoji: '🌱',
  },
  {
    id: '3',
    name: 'Espada-de-São-Jorge',
    scientificName: 'Sansevieria trifasciata',
    category: 'Suculenta Resistente',
    lightRequirement: 'Luz Difusa / Sombra',
    location: 'Hall de Entrada',
    waterIntervalDays: 14,
    fertilizeIntervalDays: 45,
    lastWateredDate: daysAgo(5),
    lastFertilizedDate: daysAgo(10),
    notes: 'Muito resistente. Cuidado com excesso de água nas raízes.',
    imageEmoji: '🪴',
  },
  {
    id: '4',
    name: 'Samambaia Americana',
    scientificName: 'Nephrolepis exaltata',
    category: 'Pendente Tropical',
    lightRequirement: 'Meia Sombra',
    location: 'Varanda Integrada',
    waterIntervalDays: 2,
    fertilizeIntervalDays: 15,
    lastWateredDate: daysAgo(2), // Regar hoje!
    lastFertilizedDate: daysAgo(7),
    notes: 'Gosta de substrato úmido constante, nunca encharcado.',
    imageEmoji: '🌾',
  },
  {
    id: '5',
    name: 'Figueira Lira',
    scientificName: 'Ficus Lyrata',
    category: 'Árvore Ornamental',
    lightRequirement: 'Sol Pleno',
    location: 'Janela da Sala',
    waterIntervalDays: 7,
    fertilizeIntervalDays: 30,
    lastWateredDate: daysAgo(6),
    lastFertilizedDate: daysAgo(28),
    notes: 'Precisa de boa claridade direta pela manhã.',
    imageEmoji: '🌳',
  },
];
