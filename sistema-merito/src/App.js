import React from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import RegisterStudent from "./pages/RegisterStudent";
import RegisterCompany from "./pages/RegisterCompany";
import AlunoHome from "./components/AlunoHome";
import EmpresaVantagens from "./components/EmpresaVantagens";
import TransacoesAluno from "./components/TransacoesAluno";
import ProfessorHome from "./components/ProfessorHome";
import DoacaoMoeda from "./components/DoacaoMoeda";
import TransacoesProfessor from "./components/TransacoesProfessor";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/register-student" element={<RegisterStudent />} />
      <Route path="/register-company" element={<RegisterCompany />} />
      <Route path="/aluno" element={<AlunoHome />} />
      <Route path="/aluno/empresas/:empresaId/vantagens" element={<EmpresaVantagens />} />
      <Route path="/aluno" element={<AlunoHome />} />
      <Route path="/aluno/transacoes" element={<TransacoesAluno />} />
      <Route path="/professor" element={<ProfessorHome />} />
  <Route path="/professor/doacao/:alunoId" element={<DoacaoMoeda />} />
  <Route path="/professor/transacoes" element={<TransacoesProfessor />} />
    </Routes>
  );
}

export default App;
