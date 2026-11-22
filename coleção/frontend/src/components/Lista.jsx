function Lista({ itens, busca, setBusca }) {
  const filtrados = itens.filter((item) =>
    item.titulo.toLowerCase().includes(busca.toLowerCase())
  );

  return (
    <div>
      <h2>Álbuns Cadastrados</h2>

      <input
        type="text"
        placeholder="Buscar por título..."
        value={busca}
        onChange={(e) => setBusca(e.target.value)}
      />

      {filtrados.length === 0 ? (
        <p>Nenhum item encontrado</p>
      ) : (
        filtrados.map((item) => (
          <p key={item.id}>
            {item.titulo} — {item.artista} ({item.ano}) — {item.avaliacao}
          </p>
        ))
      )}
    </div>
  );
}

export default Lista;