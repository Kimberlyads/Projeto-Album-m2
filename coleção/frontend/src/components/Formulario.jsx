import { useState } from 'react';

const API = `${import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'}/api/albuns/`;

function Formulario({ onSucesso, onErro, erro }) {
  const [titulo, setTitulo] = useState('');
  const [artista, setArtista] = useState('');
  const [ano, setAno] = useState('');
  const [avaliacao, setAvaliacao] = useState('');

  function cadastrar(evento) {
    evento.preventDefault();

    fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        titulo: titulo,
        artista: artista,
        ano: Number(ano),
        avaliacao: Number(avaliacao)
      })
    })
    .then(async (res) => {
      if (res.status === 201) {
        setTitulo('');
        setArtista('');
        setAno('');
        setAvaliacao('');
        onSucesso();
      } else if (res.status === 400) {
        const dados = await res.json();
        onErro(dados.erro);
      }
    });
  }

  return (
    <div className="pagina">
      <h2>Cadastro de Álbum</h2>

      {erro && (
        <p style={{ color: 'red', fontWeight: 'bold' }}>
          {erro}
        </p>
      )}

      <form onSubmit={cadastrar}>
        <input
          placeholder="Título"
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          required
        />
        <input
          placeholder="Artista"
          value={artista}
          onChange={(e) => setArtista(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Ano"
          value={ano}
          onChange={(e) => setAno(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Avaliação"
          step="any"
          value={avaliacao}
          onChange={(e) => setAvaliacao(e.target.value)}
          required
        />
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
}

export default Formulario;