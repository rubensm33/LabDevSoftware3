import React from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const HomePage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = React.useState({ username: "", password: "" });
  const [error, setError] = React.useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const body = new URLSearchParams();
      body.append("grant_type", "password");
      body.append("username", formData.username);
      body.append("password", formData.password);

      const response = await axios.post("http://localhost:8000/token", body, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });

      localStorage.setItem("token", response.data.access_token); 
      const token = response.data.access_token;
      const userResponse = await axios.get("http://localhost:8000/users/me", {
        headers: { Authorization: `Bearer ${token}` },
      });

      const user = userResponse.data;
      if (user.role === "professor") {
        navigate("/professor");
      } else if (user.role === "aluno") {
        navigate("/aluno");
      } else {
        throw new Error("Função desconhecida. Contate o administrador.");
      }
    } catch (err) {
      setError("Credenciais inválidas. Tente novamente.");
    }
  };

  return (
    <div className="homepage-container">
      <div className="register-section">
        <h2>Cadastre-se</h2>
        <div className="register-options">
          <button onClick={() => navigate("/register-student")}>Como Aluno</button>
          <button onClick={() => navigate("/register-company")}>Como Empresa</button>
        </div>
      </div>
      <div className="login-section">
        <h2>Login</h2>
        {error && <p className="error-message">{error}</p>}
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="username"
            placeholder="Email"
            value={formData.username}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Senha"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <button type="submit">Entrar</button>
        </form>
      </div>
    </div>
  );
};

export default HomePage;
