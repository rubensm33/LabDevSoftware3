import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const ProfessorHome = () => {
  const [alunos, setAlunos] = useState([]);
  const [saldo, setSaldo] = useState(0);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchProfessorData = async () => {
      if (!token) {
        alert("Token não encontrado. Faça login novamente.");
        navigate("/login");
        return;
      }

      try {
        const saldoResponse = await axios.get("http://localhost:8000/professores/saldo", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setSaldo(saldoResponse.data.saldo_moedas);

        const alunosResponse = await axios.get("http://localhost:8000/professores/alunos", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setAlunos(alunosResponse.data);
      } catch (err) {
        console.error("Erro ao carregar dados:", err);
        setError("Não foi possível carregar os dados. Tente novamente mais tarde.");
      }
    };

    fetchProfessorData();
  }, [token, navigate]);

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div className="professor-home">
      {}
      <aside className="menu-lateral">
        <h3>Menu</h3>
        <ul>
          <li onClick={() => navigate("/professor/transacoes")}>Transações</li>
        </ul>
      </aside>

      {}
      <main className="professor-main">
        <header>
          <h2>Bem-vindo, Professor</h2>
          <p>Saldo: {saldo} moedas</p>
        </header>
        <section className="alunos-list">
          <h3>Lista de Alunos</h3>
          <ul>
            {alunos.map((aluno) => (
              <li key={aluno.id} className="aluno-item">
                <span>{aluno.nome}</span>
                <button
                  onClick={() => navigate(`/professor/doacao/${aluno.id}`)}
                  className="doar-moeda-btn"
                >
                  Doar Moeda
                </button>
              </li>
            ))}
          </ul>
        </section>
      </main>
    </div>
  );
};

export default ProfessorHome;
