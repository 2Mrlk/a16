import React, { useState, useEffect } from 'react';
import { SplashScreen } from '@capacitor/splash-screen';
import {
  Droplets,
  Sparkles,
  Plus,
  Leaf,
  Calendar,
  Sun,
  Search,
  CheckCircle2,
  AlertTriangle,
  Info,
  X,
  Compass,
  Trash2,
} from 'lucide-react';
import { Plant, FilterType } from './types';
import { INITIAL_PLANTS } from './initialData';

export const App: React.FC = () => {
  const [plants, setPlants] = useState<Plant[]>(() => {
    const saved = localStorage.getItem('floracare_plants');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        return INITIAL_PLANTS;
      }
    }
    return INITIAL_PLANTS;
  });

  const [activeFilter, setActiveFilter] = useState<FilterType>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [showTips, setShowTips] = useState(false);
  const [feedbackToast, setFeedbackToast] = useState<string | null>(null);

  // Formulário de nova planta
  const [newName, setNewName] = useState('');
  const [newScientific, setNewScientific] = useState('');
  const [newLocation, setNewLocation] = useState('Sala de Estar');
  const [newLight, setNewLight] = useState<'Sol Pleno' | 'Meia Sombra' | 'Luz Difusa / Sombra'>('Meia Sombra');
  const [newWaterDays, setNewWaterDays] = useState('3');
  const [newFertilizeDays, setNewFertilizeDays] = useState('30');
  const [newNotes, setNewNotes] = useState('');
  const [newEmoji, setNewEmoji] = useState('🌿');

  // Inicializa SplashScreen
  useEffect(() => {
    const hideSplash = async () => {
      try {
        await SplashScreen.hide();
      } catch (err) {
        // Ignora no navegador web
      }
    };
    hideSplash();
  }, []);

  // Salvar no localStorage
  useEffect(() => {
    localStorage.setItem('floracare_plants', JSON.stringify(plants));
  }, [plants]);

  const triggerToast = (msg: string) => {
    setFeedbackToast(msg);
    setTimeout(() => {
      setFeedbackToast(null);
    }, 2500);
  };

  // Funções de Cálculo de Dias
  const getDaysDiff = (dateStr: string) => {
    const past = new Date(dateStr).getTime();
    const now = new Date().getTime();
    return Math.floor((now - past) / (1000 * 60 * 60 * 24));
  };

  const getWaterStatus = (plant: Plant) => {
    const elapsed = getDaysDiff(plant.lastWateredDate);
    const remaining = plant.waterIntervalDays - elapsed;
    const progress = Math.max(0, Math.min(100, Math.round(((plant.waterIntervalDays - elapsed) / plant.waterIntervalDays) * 100)));
    return {
      elapsed,
      remaining,
      progress,
      needsWater: remaining <= 0,
    };
  };

  const getFertilizeStatus = (plant: Plant) => {
    const elapsed = getDaysDiff(plant.lastFertilizedDate);
    const remaining = plant.fertilizeIntervalDays - elapsed;
    const progress = Math.max(0, Math.min(100, Math.round(((plant.fertilizeIntervalDays - elapsed) / plant.fertilizeIntervalDays) * 100)));
    return {
      elapsed,
      remaining,
      progress,
      needsFertilize: remaining <= 0,
    };
  };

  // Ações
  const handleWater = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setPlants((prev) =>
      prev.map((p) => (p.id === id ? { ...p, lastWateredDate: new Date().toISOString() } : p))
    );
    triggerToast('💧 Planta regada com sucesso!');
  };

  const handleFertilize = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setPlants((prev) =>
      prev.map((p) => (p.id === id ? { ...p, lastFertilizedDate: new Date().toISOString() } : p))
    );
    triggerToast('🌱 Adubação registrada com sucesso!');
  };

  const handleDeletePlant = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (confirm('Deseja realmente remover esta planta?')) {
      setPlants((prev) => prev.filter((p) => p.id !== id));
      triggerToast('Planta removida.');
    }
  };

  const handleAddPlant = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newName.trim()) return;

    const newPlant: Plant = {
      id: Date.now().toString(),
      name: newName.trim(),
      scientificName: newScientific.trim() || 'Espécie botânica',
      category: 'Planta de Interior',
      location: newLocation.trim() || 'Casa',
      lightRequirement: newLight,
      waterIntervalDays: Math.max(1, parseInt(newWaterDays, 10) || 3),
      fertilizeIntervalDays: Math.max(1, parseInt(newFertilizeDays, 10) || 30),
      lastWateredDate: new Date().toISOString(),
      lastFertilizedDate: new Date().toISOString(),
      notes: newNotes.trim(),
      imageEmoji: newEmoji,
    };

    setPlants((prev) => [newPlant, ...prev]);
    setIsAddModalOpen(false);
    setNewName('');
    setNewScientific('');
    setNewNotes('');
    triggerToast('🌿 Nova planta cadastrada com sucesso!');
  };

  // Estatísticas
  const waterCount = plants.filter((p) => getWaterStatus(p).needsWater).length;
  const fertilizeCount = plants.filter((p) => getFertilizeStatus(p).needsFertilize).length;

  // Filtragem
  const filteredPlants = plants.filter((p) => {
    const matchesSearch =
      p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      p.scientificName.toLowerCase().includes(searchQuery.toLowerCase()) ||
      p.location.toLowerCase().includes(searchQuery.toLowerCase());

    if (!matchesSearch) return false;

    if (activeFilter === 'needs-water') return getWaterStatus(p).needsWater;
    if (activeFilter === 'needs-fertilizer') return getFertilizeStatus(p).needsFertilize;
    if (activeFilter === 'healthy') {
      return !getWaterStatus(p).needsWater && !getFertilizeStatus(p).needsFertilize;
    }
    return true;
  });

  return (
    <div className="app-container">
      {/* Toast Notification */}
      {feedbackToast && (
        <div className="toast-notification">
          <span>{feedbackToast}</span>
        </div>
      )}

      {/* Top Header */}
      <header className="header">
        <div className="header-brand">
          <div className="header-logo-badge">
            <Leaf className="brand-icon" size={24} />
          </div>
          <div>
            <h1 className="brand-title">FloraCare</h1>
            <p className="brand-subtitle">Lembrete Inteligente de Plantas</p>
          </div>
        </div>

        <button
          className="btn-add-circle"
          onClick={() => setIsAddModalOpen(true)}
          title="Adicionar nova planta"
        >
          <Plus size={22} />
        </button>
      </header>

      {/* Dashboard Stats */}
      <div className="stats-row">
        <div
          className={`stat-card ${waterCount > 0 ? 'alert' : ''}`}
          onClick={() => setActiveFilter('needs-water')}
        >
          <div className="stat-icon-wrapper water">
            <Droplets size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-number">{waterCount}</span>
            <span className="stat-label">Regar Hoje</span>
          </div>
        </div>

        <div
          className={`stat-card ${fertilizeCount > 0 ? 'warning' : ''}`}
          onClick={() => setActiveFilter('needs-fertilizer')}
        >
          <div className="stat-icon-wrapper fertilize">
            <Sparkles size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-number">{fertilizeCount}</span>
            <span className="stat-label">Adubar Hoje</span>
          </div>
        </div>

        <div className="stat-card" onClick={() => setShowTips(!showTips)}>
          <div className="stat-icon-wrapper tips">
            <Compass size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-number">{plants.length}</span>
            <span className="stat-label">Minhas Plantas</span>
          </div>
        </div>
      </div>

      {/* Dicas Botânicas Acordeon */}
      {showTips && (
        <div className="botanical-guide-card">
          <div className="guide-header">
            <div className="guide-title">
              <Info size={18} className="guide-icon" />
              <h3>Guia Botânico Rápido</h3>
            </div>
            <button className="guide-close" onClick={() => setShowTips(false)}>
              <X size={18} />
            </button>
          </div>
          <ul className="guide-list">
            <li>
              <strong>Teste do Dedo:</strong> Enfie o dedo 2 cm na terra. Só regue se sair totalmente seco.
            </li>
            <li>
              <strong>Horário Ideal:</strong> Regue pela manhã cedinho para que as raízes absorvam a água com o sol.
            </li>
            <li>
              <strong>Adubação Inteligente:</strong> Adube sempre com o solo previamente úmido para não queimar as raízes.
            </li>
          </ul>
        </div>
      )}

      {/* Search Bar */}
      <div className="search-box">
        <Search size={18} className="search-icon" />
        <input
          type="text"
          placeholder="Buscar por nome, espécie ou local..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        {searchQuery && (
          <button className="clear-search" onClick={() => setSearchQuery('')}>
            <X size={16} />
          </button>
        )}
      </div>

      {/* Filter Tabs */}
      <div className="filter-tabs">
        <button
          className={`filter-btn ${activeFilter === 'all' ? 'active' : ''}`}
          onClick={() => setActiveFilter('all')}
        >
          Todas ({plants.length})
        </button>
        <button
          className={`filter-btn ${activeFilter === 'needs-water' ? 'active' : ''}`}
          onClick={() => setActiveFilter('needs-water')}
        >
          💧 Regar ({waterCount})
        </button>
        <button
          className={`filter-btn ${activeFilter === 'needs-fertilizer' ? 'active' : ''}`}
          onClick={() => setActiveFilter('needs-fertilizer')}
        >
          🌱 Adubar ({fertilizeCount})
        </button>
        <button
          className={`filter-btn ${activeFilter === 'healthy' ? 'active' : ''}`}
          onClick={() => setActiveFilter('healthy')}
        >
          ✨ Saudáveis
        </button>
      </div>

      {/* Plants Grid / List */}
      <div className="plants-list">
        {filteredPlants.length === 0 ? (
          <div className="empty-state">
            <Leaf size={48} className="empty-icon" />
            <p className="empty-title">Nenhuma planta encontrada</p>
            <p className="empty-desc">
              {searchQuery
                ? 'Tente pesquisar com outro termo ou limpe o campo.'
                : 'Toque no botão "+" acima para cadastrar sua primeira companheira verde!'}
            </p>
          </div>
        ) : (
          filteredPlants.map((plant) => {
            const water = getWaterStatus(plant);
            const fert = getFertilizeStatus(plant);

            return (
              <div key={plant.id} className="plant-card">
                <div className="card-top">
                  <div className="plant-emoji-badge">{plant.imageEmoji}</div>
                  <div className="plant-names">
                    <h3 className="plant-main-name">{plant.name}</h3>
                    <span className="plant-scientific-name">{plant.scientificName}</span>
                    <div className="plant-tags">
                      <span className="tag-location">{plant.location}</span>
                      <span className="tag-light">
                        <Sun size={12} /> {plant.lightRequirement}
                      </span>
                    </div>
                  </div>
                  <button
                    className="btn-delete"
                    onClick={(e) => handleDeletePlant(plant.id, e)}
                    title="Remover planta"
                  >
                    <Trash2 size={16} />
                  </button>
                </div>

                {plant.notes && <p className="plant-notes">"{plant.notes}"</p>}

                {/* Status de Rega */}
                <div className="progress-section">
                  <div className="progress-labels">
                    <span className="progress-title">
                      <Droplets size={14} className="text-cyan" /> Umidade do Solo
                    </span>
                    <span
                      className={`status-pill ${
                        water.needsWater ? 'urgent' : water.remaining <= 1 ? 'warning' : 'ok'
                      }`}
                    >
                      {water.needsWater
                        ? '⚠️ Regar Hoje!'
                        : water.remaining === 1
                        ? 'Amanhã'
                        : `em ${water.remaining} dias`}
                    </span>
                  </div>
                  <div className="progress-bar-bg">
                    <div
                      className={`progress-bar-fill water ${water.needsWater ? 'empty' : ''}`}
                      style={{ width: `${water.progress}%` }}
                    />
                  </div>
                </div>

                {/* Status de Adubação */}
                <div className="progress-section">
                  <div className="progress-labels">
                    <span className="progress-title">
                      <Sparkles size={14} className="text-amber" /> Nutrientes / Adubo
                    </span>
                    <span className={`status-pill ${fert.needsFertilize ? 'urgent' : 'ok'}`}>
                      {fert.needsFertilize
                        ? '🌱 Adubar Hoje!'
                        : `em ${fert.remaining} dias`}
                    </span>
                  </div>
                  <div className="progress-bar-bg">
                    <div
                      className={`progress-bar-fill fert ${fert.needsFertilize ? 'empty' : ''}`}
                      style={{ width: `${fert.progress}%` }}
                    />
                  </div>
                </div>

                {/* Botões de Ação */}
                <div className="card-actions">
                  <button
                    className={`btn-action water ${water.needsWater ? 'pulse' : ''}`}
                    onClick={(e) => handleWater(plant.id, e)}
                  >
                    <Droplets size={16} />
                    <span>Regar Agora</span>
                  </button>
                  <button
                    className="btn-action fertilize"
                    onClick={(e) => handleFertilize(plant.id, e)}
                  >
                    <Sparkles size={16} />
                    <span>Adubar</span>
                  </button>
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* Modal Adicionar Planta */}
      {isAddModalOpen && (
        <div className="modal-backdrop" onClick={() => setIsAddModalOpen(false)}>
          <div className="modal-dialog" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Cadastrar Nova Planta</h3>
              <button className="btn-close" onClick={() => setIsAddModalOpen(false)}>
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleAddPlant} className="modal-form">
              <div className="form-group">
                <label>Emoji da Planta</label>
                <div className="emoji-picker">
                  {['🌿', '🌱', '🪴', '🌾', '🌳', '🌵', '🌺', '🍃'].map((em) => (
                    <button
                      type="button"
                      key={em}
                      className={`emoji-choice ${newEmoji === em ? 'selected' : ''}`}
                      onClick={() => setNewEmoji(em)}
                    >
                      {em}
                    </button>
                  ))}
                </div>
              </div>

              <div className="form-group">
                <label>Nome Popular *</label>
                <input
                  type="text"
                  placeholder="Ex: Jiboia, Monstera, Suculenta"
                  required
                  value={newName}
                  onChange={(e) => setNewName(e.target.value)}
                />
              </div>

              <div className="form-group">
                <label>Nome Científico (opcional)</label>
                <input
                  type="text"
                  placeholder="Ex: Epipremnum aureum"
                  value={newScientific}
                  onChange={(e) => setNewScientific(e.target.value)}
                />
              </div>

              <div className="form-row">
                <div className="form-group half">
                  <label>Regar a cada (dias)</label>
                  <input
                    type="number"
                    min="1"
                    max="60"
                    value={newWaterDays}
                    onChange={(e) => setNewWaterDays(e.target.value)}
                  />
                </div>
                <div className="form-group half">
                  <label>Adubar a cada (dias)</label>
                  <input
                    type="number"
                    min="1"
                    max="180"
                    value={newFertilizeDays}
                    onChange={(e) => setNewFertilizeDays(e.target.value)}
                  />
                </div>
              </div>

              <div className="form-group">
                <label>Necessidade de Luz</label>
                <select
                  value={newLight}
                  onChange={(e) => setNewLight(e.target.value as any)}
                >
                  <option value="Sol Pleno">Sol Pleno (luz solar direta)</option>
                  <option value="Meia Sombra">Meia Sombra (luz solar suave)</option>
                  <option value="Luz Difusa / Sombra">Luz Difusa / Sombra (luz indireta)</option>
                </select>
              </div>

              <div className="form-group">
                <label>Localização na Casa</label>
                <input
                  type="text"
                  placeholder="Ex: Sala de Estar, Varanda, Quarto"
                  value={newLocation}
                  onChange={(e) => setNewLocation(e.target.value)}
                />
              </div>

              <div className="form-group">
                <label>Dicas de Cuidado / Notas</label>
                <textarea
                  placeholder="Ex: Borrifar água nas folhas, não deixar água no pratinho..."
                  rows={2}
                  value={newNotes}
                  onChange={(e) => setNewNotes(e.target.value)}
                />
              </div>

              <div className="modal-actions">
                <button
                  type="button"
                  className="btn-cancel"
                  onClick={() => setIsAddModalOpen(false)}
                >
                  Cancelar
                </button>
                <button type="submit" className="btn-submit">
                  Salvar Planta
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
