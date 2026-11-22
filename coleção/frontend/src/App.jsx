import { useState, useEffect } from 'react';
import './App.css';
import Formulario from './components/Formulario';
import Lista from './components/Lista';
import Resumo from './components/Resumo';

const API = `${import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'}/api/albuns/`;
const RESUMO_API = `${import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'}/api/albuns/resumo/`;

function App() {
  const [itens, setItens] = useState([]);
  const [resumo, setResumo] = useState({
    total: 0,
    media_avaliacao: 0,
    melhor: ''
  });
  const [erro, setErro] = useState('');
  const [busca, setBusca] = useState('');

  function carregarItens() {
    fetch(API)
      .then(res => res.json())
      .then(dados => setItens(dados));
  }

  function carregarResumo() {
    fetch(RESUMO_API)
      .then(res => res.json())
      .then(dados => setResumo(dados));
  }

  useEffect(() => {
    carregarItens();
    carregarResumo();
  }, []);

  function aoCadastrarComSucesso() {
    setErro('');
    carregarItens();
    carregarResumo();
  }

  function aoErro(mensagem) {
    setErro(mensagem);
  }

  return (
    <>
      <header>
        <h1>Meus Álbuns</h1>
      </header>
      <main>
        <Resumo 
          total={resumo.total} 
          media={resumo.media_avaliacao} 
          melhor={resumo.melhor} 
        />

        <Formulario 
          onSucesso={aoCadastrarComSucesso} 
          onErro={aoErro} 
          erro={erro} 
        />

        <Lista 
          itens={itens} 
          busca={busca} 
          setBusca={setBusca} 
        />
      </main>

      <footer>Desenvolvimento Web</footer>
    </>
  );
}

export default App;