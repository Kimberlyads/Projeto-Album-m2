function Resumo({ total, media, melhor }) {
  return (
    <section className="card">
      <h2>Resumo dos Álbuns</h2>
      <p>Total: {total}</p>
      <p>Média: {media}</p>
      <p>Melhor: {melhor}</p>
    </section>
  );
}

export default Resumo;