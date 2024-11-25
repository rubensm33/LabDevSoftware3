import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";

const ManageVantagens = () => {
  const [vantagens, setVantagens] = useState([]);
  const [formData, setFormData] = useState({
    descricao: "",
    foto: "",
    custo_moedas: "",
  });
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
        const userResponse = await axios.get("http://localhost:8000/users/me", {
          headers: { Authorization: `Bearer ${token}` },
        });

        let empresaId = userResponse.data.id
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

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleVantagemChange = (index, e) => {
    const newVantagens = [...vantagens];
    if (e.target.name === "foto") {
      const file = e.target.files[0];
      const reader = new FileReader();
      reader.onloadend = () => {
        newVantagens[index][e.target.name] = reader.result.split(",")[1]; // Base64
        setVantagens(newVantagens);
      };
      reader.readAsDataURL(file);
    } else {
      newVantagens[index][e.target.name] = e.target.value;
      setVantagens(newVantagens);
    }
  };

  const handleAddVantagem = async () => {
    try {
      const userResponse = await axios.get("http://localhost:8000/users/me", {
        headers: { Authorization: `Bearer ${token}` },
      });

      let empresaId = userResponse.data.id
      const response = await axios.post(
        `http://localhost:8000/empresas/${empresaId}/vantagens`,
        formData,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      setVantagens([...vantagens, response.data]);
      setFormData({ descricao: "", foto: "", custo_moedas: "" });
    } catch (err) {
      console.error("Erro ao adicionar vantagem:", err);
      setError("Não foi possível adicionar a vantagem. Tente novamente.");
    }
  };

  const handleUpdateVantagem = async (index) => {
    const vantagem = vantagens[index];
    try {
      await axios.put(
        `http://localhost:8000/empresas/vantagens/${vantagem.id}`,
        vantagem,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      alert("Vantagem atualizada com sucesso!");
    } catch (err) {
      console.error("Erro ao atualizar vantagem:", err);
      setError("Não foi possível atualizar a vantagem. Tente novamente.");
    }
  };

  if (loading) {
    return <p>Carregando vantagens...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  return (
    <div className="manage-vantagens-page">
      <h2>Gerenciar Vantagens</h2>
      <div className="vantagens-form">
        <input
          type="text"
          name="descricao"
          placeholder="Descrição"
          value={formData.descricao}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="custo_moedas"
          placeholder="Custo em Moedas"
          value={formData.custo_moedas}
          onChange={handleChange}
          required
        />
        <input
          type="file"
          name="foto"
          accept="image/*"
          onChange={handleChange}
        />
        <button onClick={handleAddVantagem}>Adicionar Vantagem</button>
      </div>
      <div className="vantagens-list">
        {vantagens.map((vantagem, index) => (
          <div key={vantagem.id} className="vantagem-item">
            <input
              type="text"
              name="descricao"
              value={vantagem.descricao}
              onChange={(e) => handleVantagemChange(index, e)}
              required
            />
            <input
              type="number"
              name="custo_moedas"
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
            <button onClick={() => handleUpdateVantagem(index)}>Atualizar</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ManageVantagens;