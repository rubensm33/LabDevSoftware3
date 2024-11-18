import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const AlunoHome = () => {
  const [aluno, setAluno] = useState({ nome: "", saldo: 0 });
  const [empresas, setEmpresas] = useState([]);
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  useEffect(() => {
    const fetchAlunoData = async () => {
      try {
 
        const saldoResponse = await axios.get("http://localhost:8000/alunos/saldo", {
          headers: { Authorization: `Bearer ${token}` },
        });

        const userResponse = await axios.get(
          `http://localhost:8000/users/${saldoResponse.data.aluno_id}`,
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );

        setAluno({
          nome: userResponse.data.nome,
          saldo: saldoResponse.data.saldo_moedas,
        });

        const empresasResponse = await axios.get("http://localhost:8000/empresas", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setEmpresas(empresasResponse.data);
      } catch (err) {
        console.error("Erro ao carregar dados:", err);
      }
    };

    fetchAlunoData();
  }, [token]);

  return (
    <div className="aluno-home">
      <aside className="menu-lateral">
        <h3>Menu</h3>
        <ul>
          <li onClick={() => navigate("/aluno/transacoes")}>Transações</li>
          {}
        </ul>
      </aside>
      <main className="aluno-main">
        <header className="aluno-header">
          <h2>Bem-vindo, {aluno.nome}</h2>
          <p>Saldo: {aluno.saldo} moedas</p>
        </header>
        <section className="empresas">
          {empresas.map((empresa) => (
            <div key={empresa.id} className="empresa-card">
              <h3>{empresa.nome}</h3>
              <button
                onClick={() => navigate(`/aluno/empresas/${empresa.id}/vantagens`)}
              >
                Ver Vantagens
              </button>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
};

export default AlunoHome;
