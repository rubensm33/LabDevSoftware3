import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const RegisterCompany = () => {
  const [formData, setFormData] = useState({
    nome: "",
    email: "",
    senha: "",
    vantagens: [
      {
        descricao: "",
        foto: "",
        custo_moedas: "",
      },
    ],
  });

  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleVantagemChange = (index, e) => {
    const newVantagens = [...formData.vantagens];
    if (e.target.name === "foto") {
      const file = e.target.files[0];
      const reader = new FileReader();
      reader.onloadend = () => {
        newVantagens[index][e.target.name] = reader.result.split(",")[1]; // Base64
        setFormData({ ...formData, vantagens: newVantagens });
      };
      reader.readAsDataURL(file);
    } else {
      newVantagens[index][e.target.name] = e.target.value;
      setFormData({ ...formData, vantagens: newVantagens });
    }
  };
  const handleAddVantagem = () => {
    if (formData.vantagens.length < 5) {
      setFormData({
        ...formData,
        vantagens: [
          ...formData.vantagens,
          { descricao: "", foto: "", custo_moedas: "" },
        ],
      });
    } else {
      setError("Você pode cadastrar no máximo 5 vantagens.");
    }
  };

  const handleRemoveVantagem = (index) => {
    const newVantagens = formData.vantagens.filter((_, i) => i !== index);
    setFormData({ ...formData, vantagens: newVantagens });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await axios.post("http://localhost:8000/empresas", formData);
      console.log("Empresa cadastrada com sucesso:", response.data);
      navigate("/");
    } catch (err) {
      console.error("Erro ao cadastrar empresa:", err.response?.data || err.message);
      setError(err.response?.data?.detail || "Erro ao cadastrar empresa.");
    }
  };

  return (
    <div className="register-page">
      <h2 className="register-title">Cadastro de Empresa</h2>
      {error && <p className="error-message">{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="nome"
          placeholder="Nome da Empresa"
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
          type="password"
          name="senha"
          placeholder="Senha"
          value={formData.senha}
          onChange={handleChange}
          required
        />

        <h3>Vantagens</h3>
        {formData.vantagens.map((vantagem, index) => (
          <div key={index} className="vantagem-container">
            <input
              type="text"
              name="descricao"
              placeholder="Descrição"
              value={vantagem.descricao}
              onChange={(e) => handleVantagemChange(index, e)}
              required
            />
            <input
              type="number"
              name="custo_moedas"
              placeholder="Custo em Moedas"
              value={vantagem.custo_moedas}
              onChange={(e) => handleVantagemChange(index, e)}
              required
            />
            <input
              type="file"
              name="foto"
              accept="image/*"
              onChange={(e) => handleVantagemChange(index, e)}
            />
            {formData.vantagens.length > 1 && (
              <button
                type="button"
                className="remove-btn"
                onClick={() => handleRemoveVantagem(index)}
              >
                Remover
              </button>
            )}
          </div>
        ))}

        {formData.vantagens.length < 5 && (
          <button
            type="button"
            className="add-btn"
            onClick={handleAddVantagem}
          >
            + Adicionar Vantagem
          </button>
        )}

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

export default RegisterCompany;
