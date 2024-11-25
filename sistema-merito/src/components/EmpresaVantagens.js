import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";

const EmpresaVantagens = () => {
  const [vantagens, setVantagens] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { empresaId } = useParams();
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchVantagens = async () => {
      if (!token) {
        alert("Token não encontrado. Faça login novamente.");
        navigate("/login");
        return;
      }

      try {
        const response = await axios.get(
          `http://localhost:8000/empresas/${empresaId}/vantagens`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        if (response.data && Array.isArray(response.data)) {
          setVantagens(response.data);
        } else if (response.data.vantagens && Array.isArray(response.data.vantagens)) {
          setVantagens(response.data.vantagens);
        } else {
          setError("Formato inesperado de resposta da API.");
        }
      } catch (err) {
        console.error("Erro ao carregar vantagens:", err);
        setError("Não foi possível carregar as vantagens. Tente novamente mais tarde.");
      } finally {
        setLoading(false);
      }
    };

    fetchVantagens();
  }, [empresaId, token, navigate]);

  const handleCompra = async (vantagemId) => {
    if (!token) {
      alert("Token não encontrado. Faça login novamente.");
      navigate("/login");
      return;
    }

    try {
      await axios.post(
        `http://localhost:8000/transacoes/compra?vantagem_id=${vantagemId}`,
        null,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      alert("Vantagem comprada com sucesso!");
    } catch (err) {
      console.error("Erro ao comprar vantagem:", err);
      alert("Não foi possível comprar a vantagem. Tente novamente.");
    }
  };

  if (loading) {
    return <p>Carregando vantagens...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  if (!vantagens || vantagens.length === 0) {
    return <p>Nenhuma vantagem encontrada para esta empresa.</p>;
  }

  return (
    <div className="empresa-vantagens-page">
      {}
      <aside className="vantagens-menu-lateral">
        <h3>Menu</h3>
        <ul>
          <li onClick={() => navigate(`/empresa/${empresaId}/manage-vantagens`)}>Gerenciar Vantagens</li>
          <li onClick={() => navigate("/aluno/transacoes")}>Transações</li>
        </ul>
        <p onClick={() => navigate("/aluno")} className="vantagens-voltar-home">
          Voltar para a Home
        </p>
      </aside>

      {}
      <div className="vantagens-container">
        <header className="vantagens-header">
          <h2>Vantagens</h2>
        </header>
        <div className="vantagens-grid">
          {vantagens.map((vantagem) => (
            <div key={vantagem.id} className="vantagens-card">
              {vantagem.foto && <img src={vantagem.foto} alt={vantagem.descricao} />}
              <h4>{vantagem.descricao}</h4>
              <p>{vantagem.custo_moedas} moedas</p>
              <button onClick={() => handleCompra(vantagem.id)}>Comprar Vantagem</button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default EmpresaVantagens;
