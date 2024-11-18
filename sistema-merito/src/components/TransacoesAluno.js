import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const TransacoesAluno = () => {
  const [transacoes, setTransacoes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchTransacoes = async () => {
      if (!token) {
        alert("Token não encontrado. Faça login novamente.");
        navigate("/login");
        return;
      }

      try {
        const response = await axios.get("http://localhost:8000/alunos/transacoes", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setTransacoes(response.data);
      } catch (err) {
        console.error("Erro ao carregar transações:", err);
        setError("Não foi possível carregar as transações. Tente novamente mais tarde.");
      } finally {
        setLoading(false);
      }
    };

    fetchTransacoes();
  }, [token, navigate]);

  if (loading) {
    return <p>Carregando transações...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  if (!transacoes || transacoes.length === 0) {
    return <p>Nenhuma transação encontrada.</p>;
  }

  return (
    <div className="transacoes-container">
      <h2>Transações</h2>
      <ul>
        {transacoes.map((transacao, index) => (
          <li key={index} className="transacao-item">
            {transacao.motivo ? (
              <>
                <p>Transação com Professor</p>
                <p>Motivo: {transacao.motivo}</p>
                <p>Valor: {transacao.valor} moedas</p>
                <p>Data: {new Date(transacao.data_transacao).toLocaleDateString()}</p>
              </>
            ) : (
              <>
                <p>Transação com Empresa</p>
                <p>Vantagem ID: {transacao.vantagem_id}</p>
                <p>Valor: {transacao.valor} moedas</p>
                <p>Data: {new Date(transacao.data_transacao).toLocaleDateString()}</p>
              </>
            )}
          </li>
        ))}
      </ul>
      <button onClick={() => navigate("/aluno")} className="voltar-home">
        Voltar para Home
      </button>
    </div>
  );
};

export default TransacoesAluno;
