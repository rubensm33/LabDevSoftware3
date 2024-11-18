import React from "react";
import { useNavigate } from "react-router-dom";

const RegisterOptions = () => {
  const navigate = useNavigate();

  return (
    <div className="register-options">
      <h2>Cadastre-se</h2>
      <button onClick={() => navigate("/register-student")}>Como Aluno</button>
      <button onClick={() => navigate("/register-company")}>Como Empresa</button>
    </div>
  );
};

export default RegisterOptions;
