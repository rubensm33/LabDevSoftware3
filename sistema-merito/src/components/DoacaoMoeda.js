import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";

const DoarMoedas = () => {
  const { alunoId } = useParams();
  const [valor, setValor] = useState("");
  const [motivo, setMotivo] = useState("");
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleDoacao = async (e) => {
    e.preventDefault();

    try {
      await axios.post(
        `http://localhost:8000/transacoes/professor_aluno`,
        { aluno_id: alunoId, valor: parseInt(valor), motivo },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert("Doação realizada com sucesso!");
      navigate("/professor");
    } catch (err) {
      console.error("Erro ao realizar doação:", err);
      alert("Não foi possível realizar a doação. Tente novamente.");
    }
  };

  return (
    <div className="doar-moeda-container">
      <h2>Doar Moedas</h2>
      <form onSubmit={handleDoacao} className="doar-moeda-form">
        <label>
          Valor:
          <input
            type="number"
            value={valor}
            onChange={(e) => setValor(e.target.value)}
            required
          />
        </label>
        <label>
          Motivo:
          <textarea
            value={motivo}
            onChange={(e) => setMotivo(e.target.value)}
            required
          />
        </label>
        <button type="submit">Doar</button>
      </form>
    </div>
  );
};

export default DoarMoedas;
