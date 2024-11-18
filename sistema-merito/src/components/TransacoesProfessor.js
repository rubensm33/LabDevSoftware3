import React, { useEffect, useState } from "react";
import axios from "axios";

const TransacoesProfessor = () => {
  const [transacoes, setTransacoes] = useState([]);
  const [loading, setLoading] = useState(true);
  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchTransacoes = async () => {
      try {
        const response = await axios.get("http://localhost:8000/professores/transacoes", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setTransacoes(response.data);
      } catch (err) {
        console.error("Erro ao carregar transações:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchTransacoes();
  }, [token]);

  if (loading) {
    return <p>Carregando transações...</p>;
  }

  if (!transacoes || transacoes.length === 0) {
    return <p>Nenhuma transação encontrada.</p>;
  }

  return (
    <div className="transacoes-container">
      <h2>Transações Realizadas</h2>
      <div className="transacoes-grid">
        {transacoes.map((transacao, index) => (
          <div key={index} className="transacao-item">
            <p><strong>Aluno ID:</strong> {transacao.aluno_id}</p>
            <p><strong>Valor:</strong> {transacao.valor} moedas</p>
            <p><strong>Motivo:</strong> {transacao.motivo}</p>
            <p><strong>Data:</strong> {new Date(transacao.data_transacao).toLocaleDateString()}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TransacoesProfessor;
