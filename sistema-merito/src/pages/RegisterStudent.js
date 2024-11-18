import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const RegisterStudent = () => {
  const [formData, setFormData] = useState({
    nome: "",
    email: "",
    cpf: "",
    hashed_password: "",
    rg: "",
    instituicao: "",
    curso: "",
  });
  const [instituicoes, setInstituicoes] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchInstituicoes = async () => {
      try {
        setIsLoading(true);
        const response = await axios.post("http://localhost:8000/instituicoes");
        setInstituicoes(response.data);
        setIsLoading(false);
      } catch (err) {
        console.error("Erro ao buscar instituições:", err.response?.data || err.message);
        setError("Erro ao carregar as instituições. Tente novamente mais tarde.");
        setIsLoading(false);
      }
    };

    fetchInstituicoes();
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await axios.post("http://localhost:8000/alunos", formData);
      console.log("Aluno cadastrado com sucesso:", response.data);
      navigate("/");
    } catch (err) {
      console.error("Erro ao cadastrar aluno:", err.response?.data || err.message);
      setError(err.response?.data?.detail || "Erro ao cadastrar aluno.");
    }
  };

  return (
    <div className="register-page">
      <h2 className="register-title">Cadastro de Aluno</h2>
      {error && <p className="error-message">{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="nome"
          placeholder="Nome"
          value={formData.nome}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="cpf"
          placeholder="CPF"
          value={formData.cpf}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="hashed_password"
          placeholder="Senha"
          value={formData.hashed_password}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="rg"
          placeholder="RG"
          value={formData.rg}
          onChange={handleChange}
          required
        />
        <select
          name="instituicao"
          value={formData.instituicao}
          onChange={handleChange}
          disabled={isLoading || instituicoes.length === 0}
          required
        >
          <option value="">Selecione uma instituição</option>
          {instituicoes.map((instituicao) => (
            <option key={instituicao.id} value={instituicao.nome}>
              {instituicao.nome}
            </option>
          ))}
        </select>
        {isLoading && <p>Carregando instituições...</p>}
        <input
          type="text"
          name="curso"
          placeholder="Curso"
          value={formData.curso}
          onChange={handleChange}
          required
        />
        <div className="button-container">
          <button type="submit">Cadastrar</button>
          <button
            type="button"
            onClick={() => navigate("/")}
          >
            Cancelar
          </button>
        </div>
      </form>
    </div>
  );
};

export default RegisterStudent;
